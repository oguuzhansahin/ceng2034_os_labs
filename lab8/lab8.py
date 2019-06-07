import os
import json

currentDir=os.getcwd()
fileList=os.listdir(currentDir+"/files")
currentFolders=os.listdir(currentDir)
for takeFile in fileList:
  file = open(currentDir+"/files/"+takeFile, "rb").read(32)
  hex_bytes = " ".join(['{:02X}'.format(byte) for byte in file])
  #print(hex_bytes,takeFile,"\n")

  four=""
  for i in range(5):
    four=four+hex_bytes[i]
  if four=="FF D8":
    if "jpgFolder" not in currentFolders:
      os.mkdir("jpgFolder")
      currentFolders=os.listdir(currentDir)
    os.system("cp "+currentDir+"/files/"+takeFile+" jpgFolder")

  if four=="89 50":
    if "pngFolder" not in currentFolders:
      os.mkdir("pngFolder")
      currentFolders=os.listdir(currentDir)
    os.system("cp "+currentDir+"/files/"+takeFile+" pngFolder")

  if four=="78 79":
    if "txtFolder" not in currentFolders:
      os.mkdir("txtFolder")
      currentFolders=os.listdir(currentDir)
    os.system("cp "+currentDir+"/files/"+takeFile+" txtFolder")

  if four=="49 44":
    if "mp3Folder" not in currentFolders:
      os.mkdir("mp3Folder")
      currentFolders=os.listdir(currentDir)
    os.system("cp "+currentDir+"/files/"+takeFile+" mp3Folder")
