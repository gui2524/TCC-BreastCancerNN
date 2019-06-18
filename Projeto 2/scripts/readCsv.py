# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import csv
import glob
import shutil

with open('C:\\Users\\Guilherme\\Desktop\\TCC\\TCC-BreastCancerNN\\Projeto 2\\resources\\data_info\\calc_case_description_train_set.csv') as f: 
    reader = csv.reader(f)
    your_list = list(reader)
    
mal_dest_dir = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\TRAIN_DIV\\MALIGNANT"
ben_dest_dir = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\TRAIN_DIV\\BENIGN"  
ben_cb_dest_dir = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\TRAIN_DIV\\BENIGN_WO_CB"      
for item in your_list:
    wildcard = r'C:/Users/Guilherme/Desktop/IMGMEDICAS/TRAIN/CBIS-DDSM/' + '*' + str(item[0]) + '*'
    for file in glob.glob(wildcard):  
        if item[9] == 'MALIGNANT':
            shutil.move(file, mal_dest_dir)
        elif item[9] == 'BENIGN':
            shutil.move(file, ben_dest_dir)
        elif item[9] == 'BENIGN_WITHOUT_CALLBACK':
            shutil.move(file, ben_cb_dest_dir)

