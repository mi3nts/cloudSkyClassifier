from shutil import copyfile
from datetime import date

import urllib.request
import time
import tarfile
import os
import datetime
import csv
from os import listdir
import shutil
from os import walk
import numpy as np
import pprint as pp
from operator import itemgetter
import cv2


def main():
    dataFolder    = '../../../../data/'
    subFolder  = dataFolder + "webCamSnaps/"
    numOfPics = 10

    start = time.time()
    getSnaps(numOfPics,subFolder)
    timeTaken('Pics taken in ',start)

def getSnaps(numOfPics,folderIn):

    directoryCheck(folderIn)
    camera = cv2.VideoCapture(0)
    i = 0
    if numOfPics >=1:
        while i < numOfPics:
            return_value, image = camera.read()
            print(image)
            cv2.imwrite(folderIn+ 'testSnaps'+str(i)+'.png', image)
            i=i+1
    else:
        print(str(numOfPics) + "is not a valid number")

    del(camera)



def dataFolderCleaner(dailyDownloadLocation):
    if os.path.exists(dailyDownloadLocation):
         shutil.rmtree(dailyDownloadLocation)
    os.makedirs(dailyDownloadLocation)


def downloadFile(url,localLocation):
    directoryCheck(localLocation)
    urllib.request.urlretrieve(url,localLocation)

def directoryCheck(outputPath):
    directoryIn = os.path.dirname(outputPath)
    if not os.path.exists(directoryIn):
        os.makedirs(directoryIn)

def unzipFile(localLocation,dailyDownloadLocation):
  destinationName = os.path.dirname(localLocation)+'/GASP.complete'
  if os.path.exists(destinationName):
      print("The folder does exist")
      shutil.rmtree(destinationName)
  else:
      print("The folder does not exist")
  unzipper(localLocation)
  directoryPaths,directoryNames,directoryFiles=  gainDirectoryInfo(dailyDownloadLocation)
  sourceName = dailyDownloadLocation + directoryNames[0]
  os.rename(sourceName, destinationName)


def unzipper(localLocation):
  tar = tarfile.open(localLocation, "r:")
  tar.extractall(os.path.dirname(localLocation))
  tar.close()

def gainDirectoryInfo(dailyDownloadLocation):
    directoryPaths = []
    directoryNames = []
    directoryFiles = []
    for (dirpath, dirnames, filenames) in walk(dailyDownloadLocation):
        directoryPaths.extend(dirpath)
        directoryNames.extend(dirnames)
        directoryFiles.extend(filenames)

    return directoryPaths,directoryNames,directoryFiles;


def fileDeleter(fileDirectory,fileExtension):
    files = os.listdir(fileDirectory)
    for item in files:
        if item.endswith(fileExtension):
            os.remove(os.path.join(fileDirectory, item))


def fileDeleterFromPath(pathIn):
    if os.path.exists(pathIn):
        os.remove(pathIn)

def getLocationList(directory, suffix=".csv"):
    filenames = listdir(directory)
    dateList = [ filename for filename in filenames if filename.endswith( suffix ) ]
    return sorted(dateList)

def sendCopy(seekPath,sendPath):

    fileNameSend  = os.path.basename(seekPath)
    directorySend = os.path.dirname(sendPath)
    sendPathAddress = os.path.join(directorySend,fileNameSend)
    directoryCheck(sendPathAddress)
    # fileDeleterFromPath(sendPathAddress)

    try:
        copyfile(seekPath,    sendPathAddress)
    except IOError as e:
        print("Error: %s - Trying Again" % e)
    try:
        copyfile(seekPath,sendPathAddress)
    except IOError as e:
        print("Unable to copy file. %s" % e)

def getUniqueList(mergedPre):
    merged = []
    seen = set()
    for d in mergedPre:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            merged.append(d)
    return merged

def getListDictionaryFromPathAsIs(dirPath):

    print('Reading from :' + dirPath)
    reader = csv.DictReader(open(dirPath))
    reader = list(reader)
    return reader;

def getListDictionary(inputPath,nodeID):
    reader = csv.DictReader(open(inputPath))
    reader = list(reader)
    reader = [v for v in reader if v['node_id'] == nodeID]
    keys = ['timestamp','node_id','subsystem','sensor','parameter','value_raw','value_hrf']
    return reader,keys;

def writeCSV(reader,keys,outputPath):
    directoryCheck(outputPath)
    csvWriter(outputPath,reader,keys)


def csvWriter(writePath,organizedData,keys):
    if len(organizedData)>0:
        with open(writePath,'w') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=keys)
            writer.writeheader()
            writer.writerows(organizedData)

def nanCorrection(organizedData,keys):
    organizedDataFinal = []
    for  organizedDataLine in organizedData:
         organizedDataNaN = nanCorrectionSingleDictionary(organizedDataLine,keys)
         organizedDataFinal.append(organizedDataNaN)
    # print(organizedDataFinal)
    return organizedDataFinal

def nanCorrectionSingleDictionary(organizedDataLine,keysIn):
#  Modyfying Each item for a single Dictionary
    dictNaN = {}
    for keyIn in keysIn:
            dictNaN[keyIn] =  'NaN'

    for key, value in organizedDataLine.items():
        dictNaN[key] = value

    return dictNaN

def timeTaken(message,start):
    print(message+str(time.time()-start)+' Seconds')


def gzExtractor(gzLocation):
    os.system('gzip -f ' +gzLocation)

if __name__ == "__main__":
   main()
