# Training 
The following instructions can be followed in training a Random Forest model in classifying between cloud and sky pixels.

## 1. Downloading the data set.
The data set used for the study can be downloaded on request from this [link](http://vintage.winklerbros.net/swimseg.html)

## 2. Running the python module

- Clone the Cloud Sky Classification repo (if you haven't already done so already)</br>
```git clone https://github.com/mi3nts/cloudSkyClassifier.git```</br>
**Make sure you have installed git**
- Navigate to RandomForest/training Directory  
```
├── cloudSkyClassifier
│   ├── firmware
│   │   ├── cloudSkyClassification-80ac14316bf4.json
│   │   ├── cloudSkyClassifierXU4.py
│   │   ├── naiveBayes
│   │   │   ├── cloudSkyClassifierNB.py
│   │   │   ├── naiveBayesModel.sav
│   │   │   ├── samples
│   │   │   │   ├── 0001BinaryNP.png
│   │   │   │   ├── 0001.png
│   │   │   │   ├── 0003.png
│   │   │   │   └── 0007.png
│   │   │   ├── testing
│   │   │   │   └── naiveBayesTesting.py
│   │   │   └── training
│   │   │       └── naiveBayesTraining.py
│   │   ├── naiveBayesModel.sav
│   │   └── randomForest
│   │       ├── cloudSkyClassifierRF.py
│   │       ├── samples
│   │       │   ├── 0001BinaryRF.png
│   │       │   ├── 0001.png
│   │       │   ├── 0003.png
│   │       │   └── 0007.png
│   │       ├── testing
│   │       │   └── randomForestTesting.py
│   │       └── training <----------------------------------------------
│   │           └── randomForestTraining.py
│   ├── instructionsXU4.md
│   └── readMe.md
```
- On the Unix Terminal type in the following:
``` python3 randomForestTraining.py```

- Enter the data Set path when prompted: 
```
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------
-Cloud Sky Classifier -Training- Random Forest Model-
-----------------------------------------------------
Enter the Data Set Path: /media/teamlary/Team_Lary_1/gitGubRepos/data/swimseg/   <---------------------
```
- In this example the data set was saved within a folder named '/media/teamlary/Team_Lary_1/gitGubRepos/data/'. 
- The data set folder should have the following directory Structure:
```
├── swimseg
│   ├── GTmaps
│   │   ├── 0001_GT.png
│   │   ├── 0002_GT.png
│   │   ├── 0003_GT.png
│   │   ├── ............................
│   ├── images
│   │   ├── 0001.png
│   │   ├── 0002.png
│   │   ├── 0003.png
│   │   ├── ............................
```

## 3.Writing the Random Forest Module. 
- In completion of the previous command the randon forest module will be written on the Data Set Path. On this example it'll write to the following directory: 
```/media/teamlary/Team_Lary_1/gitGubRepos/data/swimseg/ ```
- The files named Train_Features.npy, Train_Shapes.npy, Train_Targets.npy, Train_Targets_Shapes.npy will also be written within the same folder.
- The file directory should now look like as follows:
```
├── swimseg
│   ├── GTmaps
│   │   ├── 0001_GT.png
│   │   ├── 0002_GT.png
│   │   ├── 0003_GT.png
│   │   ├── ............................
│   ├── images
│   │   ├── 0001.png
│   │   ├── 0002.png
│   │   ├── 0003.png
│   │   ├── ............................
│   ├── randomForestModel.sav
│   ├── Train_Features.npy
│   ├── Train_Shapes.npy
│   ├── Train_Targets.npy
│   └── Train_Targets_Shapes.npy
````

## 4.Reading the testing performance of the classifier:
- The module will return a confusion matrix and a prediction accuracy statistic once completed.
```
-----------------------------------------------------
Gaining Confusion Matrices...........................
-----------------------------------------------------
Confusion Matrix for Random Forest Classifier - Training
[[ 962547   80731]
 [  65240 1411482]]
-----------------------------------------------------
Training Accuracy for Random Forest Classifier: 94.21%
-----------------------------------------------------
Training Done........................................
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)

```

## 5.Moving forward to the testing phase:
- The instructions on testing can be found [here](https://github.com/mi3nts/cloudSkyClassifier/firmware/randomForest/testing)
