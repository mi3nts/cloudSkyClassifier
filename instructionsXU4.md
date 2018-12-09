# Instructions

## Download and Install Linux Image on the XU4 
 - xu4 [Image](https://odroid.in/ubuntu_16.04lts/ubuntu-16.04.3-4.14-mate-odroid-xu4-20171212.img.xz) :
 The latest images can be found [here](https://wiki.odroid.com/odroid-xu4/os_images/linux/ubuntu/ubuntu)

## Download and install Etcher 
 - Download link can be found [here](https://www.balena.io/etcher/):
 - unzip and run(on Ubuntu)
 
## Mount the Ubuntu Image on to the SD Card 
 - Plug in the USD SD card reader 
 - Open Etcher 
 - Select the downloaded XU4 Image 
 - Cheose the relavent SD Card Reader 
 - Flash the image

## Install screen on the Linux Desktop and set up a UART 
 - On the linux command line type `sudo apt install screen`
 - connect the UART to the Desktop and type in `ls -l /dev/ttyUSB* `: 
 The presented line will state which address the USB is connected 
 - Open Screen for the UART:  
    `screen /dev/ttyUSB0 115200` Make sure you have the right address from the previous command. On this example the given address is /dev/ttyUSB0. 

## Boot up the XU4 with the Linux Image 
- Connect the UART to the XU4
- Have the Boot selector switch on the SD Card 
- power up the XU4 
- login with these Credentilas:
User Name : odroid
PW  : odroid 

## Update the current Ubuntu OS 
 - on the command window of the XU4 type `sudo do-release-upgrade`. This may take a few hours
 - These commands will update the current ubuntu version: </br>
 ```sudo apt-get update``` </br>
 ```sudo apt-get upgrade``` </br>
```sudo apt-get dist-upgrade``` </br>

## Create a new sudo User 
On the command window type the following commands and ener data as par instructed:
- Create user:
`sudo adduser teamlary` </br> 
- Provide sudo priviledges to the user: 
`sudo usermod -aG sudo teamlary`</br>
- Once the user is created, switch to the newly created user
`su - teamlary`
- Check for attained priveledges:
` sudo whoami`</br>
The output should be `root`

## Installing dependancies on the XU4 

## Intalling pip 
```
sudo apt-get install python3-pip
```

##  Installing numpy and scipy 
```
sudo apt-get install python3-numpy 
   sudo apt-get install python3-scipy 
```
## Installing sklearn 
```
sudo apt-get install scikit-learn 
```

## Installing skimage 
```
sudo apt-get install python3-skimage
```

## Installing open CV 

- Unfortunately open CV had to be installed from ground up(Probably because of the use of the reduced image).
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

- On the follwoing command make sure to match the python installations within the XU4 
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
Here 8 is the number of cores present(Since XU4 has 8 cores).  

Concluding the installation
```
sudo make install
```
- Reinitialize static libs 
```
sudo ldconfig
```

## Installing Sklearn

```
sudo apt-get install python3-matplotlib
```

```
pip3 install -U scikit-learn
```

```
sudo apt-get install build-essential python3-dev python3-setuptools \ python3-numpy python3-scipy \ libatlas-dev libatlas3-base 
```

## Getting a backup done 

- check for connected devices ``df -h`` 
- Do the Back `Up sudo dd if=/dev/sdXX of=~/sd-card-copy.img`. Make sure to replace XX with the appropriate symbols

  
### SSH into the XU4 

### Installing nmap
run the following commands on the Linux Command Line
`sudo apt-get update`
`sudo apt-get install nmap` 

### get files from Xu4 
`scp -r teamlary@10.202.42.205:/home/teamlary/gitHubRepos/data/webCamSnaps ~/`

### Install PyDrive 
`sudo pip3 install PyDrive`

 
 
 
 
 
 
 
 
 
 
