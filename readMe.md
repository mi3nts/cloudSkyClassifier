# Cloud Sky Classifier
## Introduction 
Portable particulate sensors are becoming quite popular in consumer markets. They usually rely on laser scattering technology. The current document proposes a device designed to gain particulate matter measurements(pm1, pm2.5 pm10) relying on the color of the sky which may lead to unexplored atmospheric conclusions on air quality.  

### Design Specifications  

1. Sensor Brain: [Odroid XU4](https://www.hardkernel.com/shop/odroid-xu4/)
-The XU4 runs on Ubuntu 16.04

2. Main Housing:
 -  The main cubicle enclosure will be equipped with a transparent lid.

3. Portable USB Camera: 
 - The 2.1mm Wide Angle Mjpeg 5 megapixel Hd Camera
   (HD USB Cam)[https://www.amazon.com/gp/product/B00KA83C8O/ref=oh_aui_search_detailpage?ie=UTF8&psc=1]

4. Power Usage:
- Uses between 3W - 12W

5. Date Storage: 
- The device stores both the original and classified images and the classified images within an onbaord SD Card.
 **On future iterations, both images will be uploaded to google drive via the google drive API**

6 - Web Connectivity: 
- The node will have a hardwired internet connection via a RJ45, Ethernet cable. 

7. Date Outage: 
- The device sends data packets to google drive doc which is updated live. A sample of such a document is given below.

| dateTime           | cloudPecentage    | skyRed      | skyBlue     | skyGreen    | cloudRed    | cloudGreen  | cloudBlue   |
|-------------------------|-------------------|-------------|-------------|-------------|-------------|-------------|-------------|
| 2018-11-16-1-3-52  | 99.9156 | 62.5550 | 19.7144 | 9.3899 | 206.7500 | 164.4323 | 163.6752 |
| 2018-11-16-1-36-11 | 99.9082 | 61.7375 | 19.7446 | 8.7836 | 205.9728 | 163.5578 | 163.3363 |
| 2018-11-16-1-36-45 | 99.9010 | 64.6513 | 20.2039 | 8.1907 | 206.1724 | 163.5491 | 162.2134 |
| 2018-11-17-0-39-35 | 87.5651 | 42.4589 | 35.5525 | 9.7457 | 118.6922 | 112.5238 |  97.7310 | 


8. Weight 
- weighs 0.4 Kg.

