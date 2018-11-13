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
 - on the command window of the XU4 type `sudo do-release-upgrade`
