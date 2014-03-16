#!/usr/bin/env python

import glob
import string
import png
import os
import project

databaseDir = 'database'
queryFileName = 'database/1a69.1.0.0.0.0.0.2.4.png'

def readPngBitString(pngName):
  '''read a png into a bitstring'''
  bitlist = []
  reader = png.Reader(pngName)
  for line in reader.read()[2]:
    bitlist.append(project.listToString(list(line)))
  bitstring = string.join(bitlist, '')
  return bitstring
  
querybits = readPngBitString(queryFileName)
for pngFileName in glob.iglob(os.path.join(databaseDir, '1*.png')):
  searchbits = readPngBitString(pngFileName)
  both = 0
  either = 0
  for count in xrange(len(querybits)):
    if querybits[count] == '1' and searchbits[count] == '1':
      both += 1
    if querybits[count] == '1' or searchbits[count] == '1':
      either += 1
  tanimoto = both/float(either)
  print tanimoto, pngFileName
  
