#!/usr/local/bin/python

import os
import sys
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)
filename = sys.argv[1]

def searchfile(filename):
  openfile2 = open(filename, 'r')
  openfile = openfile2.read()
  openfile1 = openfile.replace('idan','shlomi')
  valuewwrite = open(filename, 'w')
  valuewwrite.write(openfile1)
  logging.warning(filename+"\n\n"+openfile1)



if __name__ == '__main__':
    searchfile(filename)
