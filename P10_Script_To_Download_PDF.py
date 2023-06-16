# -*- coding: utf-8 -*-
"""P10_Script_To_Download_PDF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a6NxIWKDa_dhI3ZbMRHR0DX5lh8WpwWF
"""

# This script is used to download any tutorial pdf from tutorials point

import urllib.request

def download(tutorialName):
    url = 'https://www.tutorialspoint.com/' + tutorialName + '/' + tutorialName + '_tutorial.pdf'
    downloadLocation = '/home/shrinivas/Downloads/'

    pdf = urllib.request.urlopen(url)
    saveFile = open(downloadLocation + tutorialName +  '.pdf', 'wb')  # because pdf is a binary file
    saveFile.write(pdf.read())
    saveFile.close()
    print('Downloaded!')

if __name__ == '__main__':
    tutorialName = input('Name of the tutorial pdf to be downloaded: ')
    download(tutorialName)