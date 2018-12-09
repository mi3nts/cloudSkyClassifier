# Random Forest Classifier

The following instructions will guide you on using the Cloud Sky Classifier module.

## 1.0 Dowoading the Model File 

- The Random Forest Model can be downloaded from this [link](https://utdallas.box.com/s/bhldpjgyvyq62ckk1efzol9rhimy5b48)
- Make sure to save the model file in an appropriate folder.

## 2.0 Installing Dependancies

### Intalling pip 
```
sudo apt-get install python3-pip
```

###  Installing numpy and scipy 
```
sudo apt-get install python3-numpy 
   sudo apt-get install python3-scipy 
```
### Installing sklearn 
```
sudo apt-get install scikit-learn 
```
### Installing skimage 
```
sudo apt-get install python3-skimage
```

### Installing open CV 

This [link](http://www.python36.com/how-to-install-opencv340-on-ubuntu1604/) was used as a reference here. 

```
sudo apt-get install build-essential 
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran pylint
```

- make sure to match the python installations on your Desktop 
```
sudo apt-get install python2.7-dev python3.5-dev
```
For the current install of the Ubuntu image python 2.7 and python 3.5 was embedded within.

- Download OpenCV 3.4.0  
```
wget https://github.com/opencv/opencv/archive/3.4.0.zip -O opencv-3.4.0.zip
wget https://github.com/opencv/opencv_contrib/archive/3.4.0.zip -O opencv_contrib-3.4.0.zip
```
- Install Unzip 
```
sudo apt-get install unzip
```
- Extracting the files 
```
unzip opencv-3.4.0.zip
unzip opencv_contrib-3.4.0.zip
```
- Creating the build directory inside OpenCV-3.4.0:
```
cd  opencv-3.4.0
mkdir build
cd build
```

- Configuring cmake:
```
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr/local -DOPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-3.4.0/modules -DOPENCV_ENABLE_NONFREE=True ..
```
- Finally doing the install 
```
make -j8
```
Here 8 is the number of cores present(On this example 8 cores are used).  

Concluding the installation
```
sudo make install
```
- Reinitialize static libs 
```
sudo ldconfig
```

### Installing Sklearn

```
sudo apt-get install python3-matplotlib
pip3 install -U scikit-learn
sudo apt-get install build-essential python3-dev python3-setuptools python3-numpy python3-scipy libatlas-base-dev
```


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







