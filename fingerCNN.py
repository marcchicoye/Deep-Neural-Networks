import os
import shutil
from zipfile import ZipFile
import requests

# URL = "https://www.kaggle.com/datasets/koryakinp/fingers"
# response = requests.get(URL)
# open("archive.zip", "wb").write(response.content)


fileDestination = "./cleanArchive"
fileOriginal = "./archive"

listOfFiles = os.listdir(fileOriginal)

os.makedirs(fileDestination, exist_ok=True)

# create same directory in cleanArchive
for directory in listOfFiles:
    if directory.find(".DS_Store") != -1 or directory.find("fingers") != -1:
        continue
    for fingerClass in range(0, 6):
        os.makedirs(fileDestination + "/" + directory + "/" + str(fingerClass), exist_ok=True)

for directory in listOfFiles:
    if directory.find(".DS_Store") != -1 or directory.find("fingers") != -1:
        continue
    for archive in os.listdir(fileOriginal + "/" + directory):
        if len(archive) == 0:
            continue
        if archive.find(".DS_Store") != -1:
            continue
        print(f'{fileOriginal}/{directory}/{archive} ==> {fileDestination}/{directory}/{archive[-6:-5]}/{archive}')
        shutil.copy2(fileOriginal + "/" + directory + "/" + archive,
                     fileDestination + "/" + directory + "/" + archive[-6: -5] + "/" + archive)
