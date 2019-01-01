# -*- coding: utf-8 -*-
import os
from os import walk
from os.path import isfile

'''files_n_dirs = os.listdir(path=".")
files = [f for f in files_n_dirs if isfile(f)]
# print(files)

files_n_dirs = []
for (dirpath, dirnames, filenames) in walk('.'):
	print(dirpath)
	print(dirnames)
	print(filenames)
	print('- - -')
'''

ignore = ['virus.py', 'code.txt', 'tests.py']
path= '.'
files_n_dirs= ['code.txt', 'dir', 'tests.py', 'virus.py']

files = [path+'/'+f for f in files_n_dirs if isfile(path+'/'+f) and f not in ignore]
print(files)
