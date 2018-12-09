
# Cloudy_App_Via_Sklearn
# Description:
# The Application is designed to Test a Random Forest Classifier to Recognize Sky/Cloud Pixels. Pixel value sky will be
# given for a Cloud Pixel While a Pixel Value 0 will be give for a Sky Pixels. The Tested Model named
# Cloud_App_Via_Sklearn.sav will be written to the current folder
# Date: 20th of June, 2018

from sklearn.model_selection import train_test_split
import os, os.path
from skimage import io, color
import numpy as np
import cv2
import pickle
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix

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
    print("-Cloud Sky Classifier - Testing - Random Forest Model -")
    print('-----------------------------------------------------')

    i=1
    All_Data = []
    # Create  blank matrix

    # Make Sure to Set the Appropiate Paths


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
    #
    # Since the images are indexed from 1 to N separate data indexes are used to distinguish between testing and
    Train_Index, Test_Index = train_test_split((Indexes), test_size = 0.3, random_state = 42)
    Training_Indexes = sorted(Train_Index)
    Testing_Indexes = sorted(Test_Index)


    # Gaining Features for Testing
    print("Gaining Features for Testing.........................")
    print('-----------------------------------------------------')
    Test_Initial = 1;
    for i in Testing_Indexes:
        src = path + (str(i)).zfill(4) + ".png"
        print("Reading Testing Image: " + str(i) )
        if Test_Initial==1:
             All_Features_Testing = Generate_Features(src)[0]
             All_Shapes_Testing   = Generate_Features(src)[1]
             Testing_Beg_End=np.array([[0, len(All_Features_Testing)-1]])
             Last_Assign = len(All_Features_Testing)
             Test_Initial = 0
        else:
             All_Features_Testing = np.vstack((All_Features_Testing, Generate_Features(src)[0]))
             All_Shapes_Testing  = np.vstack((All_Shapes_Testing, Generate_Features(src)[1]))
             Beg_End = [Last_Assign, len(All_Features_Testing)-1]
             Testing_Beg_End = np.append(Testing_Beg_End, [Beg_End], 0)
             Last_Assign = len(All_Features_Testing)
             # print(All_Features_Testing.shape)

    # Gaining Targets for Testing
    print('-----------------------------------------------------')
    print("Gaining Targets for Testing..........................")
    print('-----------------------------------------------------')

    Target_Test_Initial = 1;
    for i in Testing_Indexes:

        print("Reading Target Image: " + str(i) )
        src = path_targets + (str(i)).zfill(4) +"_GT" + ".png"

        if Target_Test_Initial == 1:
           All_Targets_Testing = Generate_Targets(src)[0]
           All_Shapes_Targets_Testing = Generate_Targets(src)[1]
           Target_Testing_Beg_End = np.array([[0, len(All_Targets_Testing) - 1]])
           Last_Assign = len(All_Targets_Testing)
           Target_Test_Initial = 0

        else:
           All_Targets_Testing = np.vstack((All_Targets_Testing, Generate_Targets(src)[0]))
           All_Shapes_Targets_Testing = np.vstack((All_Shapes_Targets_Testing, Generate_Targets(src)[1]))
           Beg_End = [Last_Assign, len(All_Targets_Testing) - 1]
           Target_Testing_Beg_End = np.append(Target_Testing_Beg_End, [Beg_End], 0)
           Last_Assign = len(All_Targets_Testing)
           #print(All_Targets_Testing.shape)

    print('-----------------------------------------------------')
    print("Features and Targets Collected.......................")
    print('-----------------------------------------------------')

    # Saving the Date Set
    np.save(dataSetPath+'Test_Features.npy', All_Features_Testing)
    np.save(dataSetPath+'Test_Targets.npy', All_Targets_Testing)
    np.save(dataSetPath+'Test_Shapes.npy', All_Shapes_Testing)
    np.save(dataSetPath+'Test_Targets_Shapes.npy', All_Shapes_Targets_Testing)

    print("Features and Targets Saved...........................")
    print('-----------------------------------------------------')

    All_Features_Testing = np.load(dataSetPath+'Test_Features.npy')
    All_Targets_Testing  = np.load(dataSetPath+'Test_Targets.npy')
    All_Shapes_Testing   = np.load(dataSetPath+'Test_Targets.npy')

    # Testing and target sets are done
    print("Loading Random Forest Classifier.......................")
    print('-----------------------------------------------------')

    Model_Save_File_Name = dataSetPath + 'randomForestModel.sav'
    loadedModel = pickle.load(open(Model_Save_File_Name, 'rb'))
    testingPredictionBinary,testingPrediction = getPredictionMatrix(loadedModel,All_Features_Testing)

    print("Gaining Confusion Matrices...........................")
    print('-----------------------------------------------------')

    Confusion_Matrix_Testing_RF = confusion_matrix(All_Targets_Testing,testingPredictionBinary)

    print("Confusion Matrix for Random Forest Classifier - Testing")
    print(Confusion_Matrix_Testing_RF)
    print('-----------------------------------------------------')


    testingAccuracy  =round((Confusion_Matrix_Testing_RF[0][0]+ Confusion_Matrix_Testing_RF[1][1]) \
                           /(Confusion_Matrix_Testing_RF[0][0]+ Confusion_Matrix_Testing_RF[1][1] + \
                             Confusion_Matrix_Testing_RF[0][1]+ Confusion_Matrix_Testing_RF[1][0]),4)

    print("Testing Accuracy for Random Forest Classifier: "+str(round(testingAccuracy*100,2))+"%" )
    print("-----------------------------------------------------")
    print('Testing Done.........................................')
    print("-----------------------------------------------------")
    print("Multi-scale Integrated Sensing and Simulation (MINTS)")
    print('-----------------------------------------------------')
