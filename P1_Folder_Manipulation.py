# -*- coding: utf-8 -*-
"""Folder_Manipulation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a6NxIWKDa_dhI3ZbMRHR0DX5lh8WpwWF
"""

#In this script we will be seeing how to create folders using Python and manipuate them!

import os
import time

def createFolders(BASE_DIR):
    ''' This function creates folders '''
    for i in range(10):
            os.mkdir(BASE_DIR + str(i) + '-Folder')

def createFiles(BASE_DIR):
    ''' This function creates .txt files '''
    for i in range(10):
        f = open(BASE_DIR + str(i) + 'Folder.txt', 'w')
        f.close()

def renameFiles(BASE_DIR):
    ''' This function renames files '''
    os.chdir(BASE_DIR) #Change directory to list the files
    for i in os.listdir():
        fileName, fileExt = os.path.splitext(i)
        print(fileName, fileExt)
        os.rename(i, i.replace('Folder', '-Folder'))

if __name__ == '__main__':
    BASE_DIR = '/home/shrinivas/Downloads/PythonPrograms/Scripts/Tests/'
    #createFolders(BASE_DIR)
    createFiles(BASE_DIR)
    time.sleep(10)
    renameFiles(BASE_DIR)