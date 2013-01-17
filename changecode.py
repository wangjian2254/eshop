#coding=utf-8
__author__ = '王健'
import os

for filename in os.listdir(os.getcwd()):
    file=open('m\\'+filename,'w')
    dwt=open(filename,'r')
    for line in dwt:
        file.write(line.decode('gbk').encode('utf-8'))
  