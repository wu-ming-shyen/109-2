# -*- coding: utf-8 -*-
"""Onsite Exam.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qvxq6NtSEb_nSaHherNmqUWfg8Myrom2
"""

#B10856012 吳明軒
import os
  
indexs = []
index = input('Please input a value:')

while (index != ''):
    indexs.append(index)
    index = input('Please input a value:')
    
search = input('Please input your search:')
while (search != ''):
    if (search in indexs):
        indexs.remove(search)
        print(indexs)
    else:
        print('unfind',search)
    search = input('Please input your search(enter to end):')


os.system("pause")