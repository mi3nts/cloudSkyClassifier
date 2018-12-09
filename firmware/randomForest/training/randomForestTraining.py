# MINTS
# Date: 20th of June, 2018

from sklearn.model_selection import train_test_split
import os, os.path
from skimage import io, color
import numpy as np
import cv2
import pickle
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestRegressor

def Generate_Features(input_path):
    # For a given Image a feature set is generated

    Input_Image = cv2.imread(input_path)

    # Gaining RGB Images
    Input_Image_RGB = cv2.cvtColor(Input_Image, cv2.COLOR_BGR2RGBA)

    # Gaining HSV Images
    Input_Image_HSV = cv2.cvtColor(Input_Image, cv2.COLOR_BGR2HSV)

    # Gaining LAB Images
    RGB_for_LAB = io.imread(input_path)
    Input_Image_LAB = color.rgb2lab(RGB_for_LAB)

    # Conversion to Arrays
    Image_Array_RGB = np.array(Input_Image_RGB)
    Image_Array_HSV = np.array(Input_Image_HSV)
    Image_Array_LAB = np.array(Input_Image_LAB)


    # Recording the Image Shapes
    Image_Shape = Image_Array_RGB.shape

    # Converting Each Image into 1D Vectors
    One_D_Image_Red = np.transpose(np.matrix(Image_Array_RGB[:, :, 0].ravel()))
    One_D_Image_Green = np.transpose(np.matrix(Image_Array_RGB[:, :, 1].ravel()))
    One_D_Image_Blue = np.transpose(np.matrix(Image_Array_RGB[:, :, 2].ravel()))



    One_D_Image_H = np.transpose(np.matrix(Image_Array_HSV[:, :, 0].ravel()))
    One_D_Image_S = np.transpose(np.matrix(Image_Array_HSV[:, :, 1].ravel()))
    One_D_Image_V = np.transpose(np.matrix(Image_Array_HSV[:, :, 2].ravel()))

    One_D_Image_L = np.transpose(np.matrix(Image_Array_LAB[:, :, 0].ravel()))
    One_D_Image_A = np.transpose(np.matrix(Image_Array_LAB[:, :, 1].ravel()))
    One_D_Image_B = np.transpose(np.matrix(Image_Array_LAB[:, :, 2].ravel()))


    # Recasting Variables for Negative Values Support
    One_D_Image_Red = One_D_Image_Red.astype(np.int16)
    One_D_Image_Green = One_D_Image_Green.astype(np.int16)
    One_D_Image_Blue = One_D_Image_Blue.astype(np.int16)


    # Getting the Chroma image
    One_D_RGB_Only = np.hstack((One_D_Image_Red, One_D_Image_Green, One_D_Image_Blue))
    Max_RGB = One_D_RGB_Only.max(1)
    Min_RGB = One_D_RGB_Only.min(1)
    One_D_Chroma = Max_RGB-Min_RGB

    # Writing the full Feature Vector One_D_Image_H, One_D_Image_S, One_D_Image_V, \One_D_Image_Red, One_D_Image_Green,One_D_Image_L, One_D_Image_A,
    One_D_Image = np.hstack((One_D_Image_Blue,\
                             One_D_Image_B, \
                             One_D_Image_Red/(One_D_Image_Blue+1), np.subtract(One_D_Image_Red, One_D_Image_Blue), \
                             (One_D_Image_Blue-One_D_Image_Red)/((One_D_Image_Blue+One_D_Image_Red)+1),\
                             One_D_Chroma
                             ))


    return One_D_Image, Image_Shape



def Generate_Targets(input_path):
    # For a Given Image a Target Vector is Generated
    Input_Image_Binary = cv2.imread(input_path)
    Image_Array_Binary = np.array(Input_Image_Binary)
    Image_Shape = Image_Array_Binary.shape
    One_D_Binary = np.transpose(np.matrix(Image_Array_Binary[:, :, 1].ravel()))
    One_D_Binary = One_D_Binary.astype(float) / 255
    return One_D_Binary, Image_Shape

def getPredictionMatrix(loadedModel,oneDImage):
    prediction       = loadedModel.predict(oneDImage)
    predictionBinary = np.transpose(np.matrix(np.array(prediction)))
    predictionBinary[predictionBinary < 0.5]  = 0
    predictionBinary[predictionBinary >= 0.5] = 1
    return predictionBinary,prediction


if __name__ == '__main__':
    print("-----------------------------------------------------")
    print("Multi-scale Integrated Sensing and Simulation (MINTS)")
    print('-----------------------------------------------------')
    print("-Cloud Sky Classifier -Training- Random Forest Model-")
    print('-----------------------------------------------------')

    i=1
    All_Data = []


    dataSetPath  = "/media/teamlary/Team_Lary_1/gitGubRepos/data/swimseg2/"
    dataSetPath = input('Enter the Data Set Path:')
    print('-----------------------------------------------------')

    path = dataSetPath + "images/"
    path_targets =dataSetPath  +"GTmaps/"

    # Figuring out the number of images
    Num_of_Images = len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
    print("Number of images:" +str(Num_of_Images))
    print('-----------------------------------------------------')
    Indexes = list(range(1, Num_of_Images+1))

    Train_Index, Test_Index = train_test_split((Indexes), test_size = 0.3, random_state = 42)
    Training_Indexes = sorted(Train_Index)
    Testing_Indexes = sorted(Test_Index)


    # Gaining Features for Training
    print("Gaining Features for Training........................")
    print('-----------------------------------------------------')
    Train_Initial = 1;
    for i in Training_Indexes:
        src = path + (str(i)).zfill(4) + ".png"
        print("Reading Training Image: " + str(i) )
        if Train_Initial==1:
             All_Features_Training = Generate_Features(src)[0]
             All_Shapes_Training   = Generate_Features(src)[1]
             Training_Beg_End=np.array([[0, len(All_Features_Training)-1]])
             Last_Assign = len(All_Features_Training)
             Train_Initial = 0
        else:
             All_Features_Training = np.vstack((All_Features_Training, Generate_Features(src)[0]))
             All_Shapes_Training  = np.vstack((All_Shapes_Training, Generate_Features(src)[1]))
             Beg_End = [Last_Assign, len(All_Features_Training)-1]
             Training_Beg_End = np.append(Training_Beg_End, [Beg_End], 0)
             Last_Assign = len(All_Features_Training)
             # print(All_Features_Training.shape)

    # Gaining Targets for Training
    print('-----------------------------------------------------')
    print("Gaining Targets for Training.........................")
    print('-----------------------------------------------------')

    Target_Train_Initial = 1;
    for i in Training_Indexes:

        print("Reading Target Image: " + str(i) )
        src = path_targets + (str(i)).zfill(4) +"_GT" + ".png"

        if Target_Train_Initial == 1:
           All_Targets_Training = Generate_Targets(src)[0]
           All_Shapes_Targets_Training = Generate_Targets(src)[1]
           Target_Training_Beg_End = np.array([[0, len(All_Targets_Training) - 1]])
           Last_Assign = len(All_Targets_Training)
           Target_Train_Initial = 0

        else:
           All_Targets_Training = np.vstack((All_Targets_Training, Generate_Targets(src)[0]))
           All_Shapes_Targets_Training = np.vstack((All_Shapes_Targets_Training, Generate_Targets(src)[1]))
           Beg_End = [Last_Assign, len(All_Targets_Training) - 1]
           Target_Training_Beg_End = np.append(Target_Training_Beg_End, [Beg_End], 0)
           Last_Assign = len(All_Targets_Training)
           #print(All_Targets_Training.shape)
    print('-----------------------------------------------------')
    print("Features and Targets Collected.......................")
    print('-----------------------------------------------------')

    # Saving the Date Set
    np.save(dataSetPath+'Train_Features.npy', All_Features_Training)
    np.save(dataSetPath+'Train_Targets.npy', All_Targets_Training)
    np.save(dataSetPath+'Train_Shapes.npy', All_Shapes_Training)
    np.save(dataSetPath+'Train_Targets_Shapes.npy', All_Shapes_Targets_Training)

    print("Features and Targets Saved...........................")
    print('-----------------------------------------------------')

    All_Features_Training = np.load(dataSetPath+'Train_Features.npy')
    All_Targets_Training  = np.load(dataSetPath+'Train_Targets.npy')
    All_Shapes_Training   = np.load(dataSetPath+'Train_Targets.npy')

    # Training and target sets are done
    print("Training Random Forest Classifier....................")
    print('-----------------------------------------------------')


    Random_Forest_Model = RandomForestRegressor(n_estimators=10, random_state=42)
    Random_Forest_Model.fit(All_Features_Training, np.ravel(All_Targets_Training, order='C'))
    Model_Save_File_Name = dataSetPath +  'randomForestModel.sav'
    pickle.dump(Random_Forest_Model, open(Model_Save_File_Name, 'wb'))


    loadedModel = pickle.load(open(Model_Save_File_Name, 'rb'))
    trainingPredictionBinary,TrainingPrediction = getPredictionMatrix(loadedModel,All_Features_Training)

    print("Gaining Confusion Matrices...........................")
    print('-----------------------------------------------------')

    Confusion_Matrix_Training_RF = confusion_matrix(All_Targets_Training,trainingPredictionBinary)

    print("Confusion Matrix for Random Forest Classifier - Training")
    print(Confusion_Matrix_Training_RF)
    print('-----------------------------------------------------')


    TrainingAccuracy  =round((Confusion_Matrix_Training_RF[0][0]+ Confusion_Matrix_Training_RF[1][1]) \
                           /(Confusion_Matrix_Training_RF[0][0]+ Confusion_Matrix_Training_RF[1][1] + \
                             Confusion_Matrix_Training_RF[0][1]+ Confusion_Matrix_Training_RF[1][0]),4)

    print("Training Accuracy for Random Forest Classifier: "+str(round(TrainingAccuracy*100,2))+"%" )
    print("-----------------------------------------------------")
    print('Training Done........................................')
    print("-----------------------------------------------------")
    print("Multi-scale Integrated Sensing and Simulation (MINTS)")
    print('-----------------------------------------------------')
