# Instructions for the XU4 implementation of the Cloud Sky Classifier

The following instructions will guide you on using the Cloud Sky Classifier module with an [Odroid XU4](https://ameridroid.com/products/odroid-xu4).


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

-  The following [link](https://github.com/mi3nts/cloudSkyClassifier/blob/master/dependencies.md) provides instructions on installing  the necessary dependancies.

## Getting a backup done 

- check for connected devices ``df -h`` 
- Do the Back Up `sudo dd if=/dev/sdXX of=~/sd-card-copy.img`. Make sure to replace XX with the appropriate symbols. Example:
`sudo dd if=/dev/sde of=/media/teamlary/Team_Lary_1/gitGubRepos/data/images/GISNode/GISNode.img`
  
### SSH into the XU4 

### Installing nmap
run the following commands on the Linux Command Line
`sudo apt-get update`
`sudo apt-get install nmap` 

### get files from Xu4 
`scp -r teamlary@10.202.42.205:/home/teamlary/gitHubRepos/data/webCamSnaps ~/`

### Install PyDrive 
`sudo pip3 install PyDrive`


### Set UTC Time Zone 
Follow instructions given on this [link](https://www.tecmint.com/set-time-timezone-and-synchronize-time-using-timedatectl-command/)
 
 
 
 
 
 
 
 
