import shutil
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
mypath = "C:\\Users\\georgewagenknechtr\\Downloads\\SynthText\\bg_data\\bg_img.tar\\bg_img"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for file in onlyfiles:
    if file.find("_") > -1:
        foldername = file.split("_")
        dirname = str(foldername[0])
        if os.path.isdir(dirname) == True:
            print(file)
            Path(mypath + "\\" + str(file)).rename(mypath + str(foldername[0]) + "\\" + str(file))
        if os.path.isdir(dirname) == False:
            os.mkdir(dirname)
            print(file)
            Path(mypath + "\\" + str(file)).rename(mypath + str(foldername[0]) + "\\" + str(file))
            
