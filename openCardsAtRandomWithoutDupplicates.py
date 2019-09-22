import os
import glob
import random
import csv
from typing import Set

path = 'D:\\Bureau\\Drive\\Xmind'
dataFilePath = 'D:\\Bureau\\Drive\\Xmind\\alreadyViewedFiles.csv'

def writeValuesInFile(datas, mode):
     with open(dataFilePath, mode, newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for data in datas:
            spamwriter.writerow([data])
            
def addNewValuesInFile(datas):
   writeValuesInFile(datas, 'a+')

def writeNewValuesInFile(datas):
   writeValuesInFile(datas, 'w')

def resetAlreadyViewedFiles():
   writeNewValuesInFile(set())
   
def getAlreadyReviewedFiles():
    try:
        with open(dataFilePath, 'r') as readFile:
            alreadyReviewedFiles = set()
            reader = csv.reader(readFile)
            for read in reader:
                alreadyReviewedFiles.add(read[0])
            return alreadyReviewedFiles

    except Exception as e:
        print('Error retrieving data')
        print(e)
    return set()

def filesWithoutReviewedFilesAlready(allFiles, alreadyReviewedFiles):
    return allFiles.difference(alreadyReviewedFiles)


def getAllXmindFilesFromFolder():
    allFiles = set()
    for root, directories, files in os.walk(path):
        for file in files:
            if '.xmind' in file:
                allFiles.add(os.path.join(root, file))
    return allFiles

def selectRandomFilesList(datas):
    if len(datas) == 0:
        return []
    if len(datas) <= 2:
        return random.sample(datas, len(datas))
    return random.sample(datas, 3)

        
alreadyReviewedFiles = getAlreadyReviewedFiles()
allFiles = getAllXmindFilesFromFolder()
toBeReviewedFiles = filesWithoutReviewedFilesAlready(allFiles, alreadyReviewedFiles)
toBeReviewedRandomSelection = selectRandomFilesList(toBeReviewedFiles)


if len(toBeReviewedRandomSelection) == 0:
    resetAlreadyViewedFiles()
    print('il reste ' + str(len(allFiles)) + ' cartes a revoir')
elif len(toBeReviewedRandomSelection) <= 2:
    resetAlreadyViewedFiles()
    for randomFile in toBeReviewedRandomSelection:    
        os.startfile(randomFile)
    print('il reste ' + str(len(allFiles)) + ' cartes a revoir')
else:
    for randomFile in toBeReviewedRandomSelection:
        os.startfile(randomFile)
    addNewValuesInFile(toBeReviewedRandomSelection)
    print('il reste ' + str(len(allFiles.difference(alreadyReviewedFiles)) - len(toBeReviewedRandomSelection)) + ' cartes a revoir')




