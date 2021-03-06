
# Testing
The following instructions can be followed in testing a Naive Bayes classifier designed to classify between cloud and sky pixels.

## 1. Completion of the training phase.
- The instructions on completing the training phase can be found [here](https://github.com/mi3nts/cloudSkyClassifier/tree/master/firmware/naiveBayes/training)

## 2. Running the python module

- Navigate to *naiveBayes/testing* Directory within the git Repo:

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
│   │   │   ├── testing <----------------------------------------------
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
│   │       └── training 
│   │           └── randomForestTraining.py
│   ├── instructionsXU4.md
│   └── readMe.md
```
- On the Unix Terminal type in the following:
``` python3 naiveBayesTesting.py```

- Enter the path to the data Set when prompted: 
```
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------
-Cloud Sky Classifier - Testing - Random Forest Model -
-----------------------------------------------------
Enter the Data Set Path:/media/teamlary/Team_Lary_1/gitGubRepos/data/swimseg/      <---------------
```
- In this example the data set was saved within a folder named */media/teamlary/Team_Lary_1/gitGubRepos/data/'.*
- The data set folder should have the following directory Structure(**prior to running this script**):

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
│   ├── naiveBayesModel.sav
│   ├── Train_Features.npy
│   ├── Train_Shapes.npy
│   ├── Train_Targets.npy
│   └── Train_Targets_Shapes.npy
```

## 3.Reading the Random Forest Module. 
- The current code will read the testing data as well as the Naive Bayes module from the given data set path. On this example it'll write to the following directory: 
```/media/teamlary/Team_Lary_1/gitGubRepos/data/swimseg/ ```
- The files named *Test_Features.npy, Test_Shapes.npy, Test_Targets.npy,* and *Test_Targets_Shapes.npy* will also be written within the same folder.
- The file directory should now look this:
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
│   ├── naiveBayesModel.sav
│   ├── Test_Features.npy
│   ├── Test_Shapes.npy
│   ├── Test_Targets.npy
│   ├── Test_Targets_Shapes.npy
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
Confusion Matrix for Naive Bayes Classifier - Testing
[[459437   4949]
 [124161 491453]]
-----------------------------------------------------
Testing Accuracy for Naive Bayes Classifier: 88.05%
-----------------------------------------------------
Testing Done.........................................
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------
```
