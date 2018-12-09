
# Installing Dependancies for the Cloud Sky Classifier
On a Unix terminal type in the following scripts

## Intalling pip 
```sudo apt-get install python3-pip```

##  Installing numpy and scipy 
```
sudo apt-get install python3-numpy 
sudo apt-get install python3-scipy 
```

## Installing sklearn 
```sudo apt-get install scikit-learn ```

## Installing skimage 
```sudo apt-get install python3-skimage```

## Installing open CV 
-  This [link](http://www.python36.com/how-to-install-opencv340-on-ubuntu1604/) was used as a reference here. 
```
sudo apt-get install build-essential 
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran pylint
```

- On the follwoing command make sure to match the python installations within the XU4 
```sudo apt-get install python2.7-dev python3.5-dev```
For the current install of the Ubuntu image, python 2.7 and python 3.5 was embedded within.

- Download OpenCV 3.4.0  
```
wget https://github.com/opencv/opencv/archive/3.4.0.zip -O opencv-3.4.0.zip
wget https://github.com/opencv/opencv_contrib/archive/3.4.0.zip -O opencv_contrib-3.4.0.zip
```
- Install Unzip 
```sudo apt-get install unzip```
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
```make -j8```
8 is the number of cores present.  

Concluding the installation
```sudo make install```

- Reinitialize static libs 
```sudo ldconfig```

## Installing Sklearn

```
sudo apt-get install python3-matplotlib
pip3 install -U scikit-learn
sudo apt-get install build-essential python3-dev python3-setuptools python3-numpy python3-scipy libatlas-base-dev
```
