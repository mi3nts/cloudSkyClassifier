# Random Forest Classifier

The following instructions will guide you on using the Cloud Sky Classifier module.

## 1.0 Dowoading the Model File 

- The Random Forest model can be downloaded from this [link](https://utdallas.box.com/s/bhldpjgyvyq62ckk1efzol9rhimy5b48)
- Make sure to save the model file in an appropriate folder.

## 2.0 Installing Dependancies
-  The following [link](https://github.com/mi3nts/cloudSkyClassifier/blob/master/dependencies.md) provides instructions on installing  the necessary dependancies.

## 3.0 Running the python module

- Clone the Cloud Sky Classification repo
```git clone https://github.com/mi3nts/cloudSkyClassifier.git```</br>
**Make sure you have installed git**
- Navigate to RandomForest Directory  
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
│   │   └── randomForest<----------------------------------------------
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
``` python3 cloudSkyClassifierRF.py```
- Give the image path and the path to the model file on the first and 2nd promts respectively:
```
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------
Enter the path to image file: samples/0001.png <----
-----------------------------------------------------
Enter the path to model file: /media/teamlary/Team_Lary_1/gitGubRepos/data/cloudSkyClassifierModels/randomForest.sav <----
-----------------------------------------------------
```
On this example, image path and the model path is given as: `samples/0001.png` and  `/media/teamlary/Team_Lary_1/gitGubRepos/data/cloudSkyClassifierModels/randomForest.sav` repectively. 

## 4.0 Reading the results 

- The results should read as follows:
```
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------
Prediction Accuracy  :  80.76048129799186%
------------------------------
Cloud Pecentage      :  75.12388888888889%
------------------------------
Sky Red              :  69.41574915693324
Sky Green            :  95.66514058556848
Sky Blue             :  133.13537083770686
------------------------------
Cloud Red            :  155.06702262189125
Cloud Green          :  165.0728648232919
Cloud Blue           :  182.7029573371394
-----------------------------------------------------
Preiction time is 26.83636736869812 Seconds
-----------------------------------------------------
Multi-scale Integrated Sensing and Simulation (MINTS)
-----------------------------------------------------

```
- The module will also write a separate image with a post script of 'BinaryRF.png' where white pixels will define cloud+sun pixels while the sky pixels will be denoted by black pixels. 







