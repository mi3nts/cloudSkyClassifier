# Naive Bayes Classifier

The following instructions will guide you on using the Cloud Sky Classifier module.

## 1.0 Installing Dependancies
-  The following [link](https://github.com/mi3nts/cloudSkyClassifier/blob/master/dependencies.md) provides instructions on installing the necessary dependancies.

 ## 2.0 Running the python module

- Clone the Cloud Sky Classification repo
```git clone https://github.com/mi3nts/cloudSkyClassifier.git```</br>
**Make sure you have installed git**
- Navigate to Naive Bayes Directory  
```
├── cloudSkyClassifier
│   ├── firmware
│   │   ├── cloudSkyClassification-80ac14316bf4.json
│   │   ├── cloudSkyClassifierXU4.py
│   │   ├── naiveBayes <----------------------------------------------
│   │   │   ├── cloudSkyClassifierNB.py
│   │   │   ├── naiveBayesModel.sav
│   │   │   ├── samples
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

`` python3 cloudSkyClassifierNB.py``

- Enter the image path when prompted. 
```
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------
------ Cloud Sky Classifier - Naive Bayes Model -----
-----------------------------------------------------
Enter the path to image file: samples/0001.png <---------------------------
-----------------------------------------------------
```
On this example the image path is given as: `samples/0001.png` 

## 3.0 Reading the results 

- The results should read as follows:
```
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------
------------------------------
Cloud Pecentage      :  68.57944444444445%
------------------------------
Sky Red              :  80.61723570910763
Sky Green            :  104.64380182824408
Sky Blue             :  137.0393143200665
------------------------------
Cloud Red            :  120.71166044247143
Cloud Green          :  135.02292961123757
Cloud Blue           :  157.25643819414628
-----------------------------------------------------
Preiction time is 8.005577325820923 Seconds
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------
```
- The module will also write a separate image with a post script of *'BinaryNB.png'* where white pixels will define cloud+sun pixels while the sky pixels will be denoted by black pixels. 
