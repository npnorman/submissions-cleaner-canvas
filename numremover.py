
import os
import shutil
import re

# remove name_xxx_xxx_(keep)_remove (1) and -1
# given a file name, remove (1), or -1
# save file in unique folder

inPath = "./in/"
outPath = "./out/"
uniqueOutPath = "Assignment " + input("Assignment # or Name: ")
uniqueOutPath = uniqueOutPath.strip()
uniqueOutPath = uniqueOutPath.replace(" ", "-")

blacklist = []
whitelist = []

# ensure uniqueness
keepGoing = True
index = 0
while keepGoing:
    outputDir = ".\\out\\" + uniqueOutPath + "\\"
    if os.path.exists(outputDir):
        uniqueOutPath += str(index)
        index += 1
    else:
        os.mkdir(outputDir)
        keepGoing = False

fileNames = os.listdir(inPath)

for fileName in fileNames:
    # save name and end
    parts = fileName.split("_")
    studentName = parts[0]
    newFileName = parts[-1]
    
    # for new File name,
    # replace  (1) and -1 with ""
    newFileName = re.sub(r"(-\d+| \(\d+\))", "", newFileName)
    
    # add to directory
    
    studentDirectory = outputDir + studentName + "\\"
    if os.path.exists(studentDirectory) == False:
        #create directory
        print("Creating directory " + studentDirectory)
        os.mkdir(studentDirectory)
    
    # move file and give new cleaned name
    shutil.move(".\\in\\" + fileName, studentDirectory + newFileName)
    
print("Completed files moved and cleaned :)")
    