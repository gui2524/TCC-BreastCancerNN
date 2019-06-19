import csv
import glob
import shutil

with open('C:\\Users\\Guilherme\\Desktop\\TCC\\TCC-BreastCancerNN\\Projeto 2\\resources\\data_info\\calc_case_description_train_set.csv') as f: 
    reader = csv.reader(f)
    your_list = list(reader)
    
    
mal_dest_dir = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\TRAIN_DIV\\MALIGNANT\\"
ben_dest_dir = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\TRAIN_DIV\\BENIGN\\"  
ben_cb_dest_dir = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\TRAIN_DIV\\BENIGN_WO_CB\\"      
for item in your_list:
    wildcard = r'C:/Users/Guilherme/Desktop/IMGMEDICAS/TRAIN/CBIS-DDSM/' + '*' + str(item[0]) + '*' +'/*/*/*.png'
    for file in glob.glob(wildcard):
        if item[9] == 'MALIGNANT':
            dest_dir = mal_dest_dir
        elif item[9] == 'BENIGN':
            dest_dir = ben_dest_dir
        elif item[9] == 'BENIGN_WITHOUT_CALLBACK':
            dest_dir = ben_cb_dest_dir
        
        print(file + " copied")
        shutil.move(file, dest_dir)

