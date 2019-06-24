import csv
import glob
import shutil

txt = input("Type [1] for TRAIN or [2] for PREDICT: ") 


if txt == '1':
    folder = "TRAIN"
    with open('C:\\Users\\Guilherme\\Desktop\\TCC\\TCC-BreastCancerNN\\Projeto 2\\resources\\data_info\\calc_case_description_train_set.csv') as f: 
        reader = csv.reader(f)
        your_list = list(reader)
elif txt == '2':
    folder = "PREDICT"
    with open('C:\\Users\\Guilherme\\Desktop\\TCC\\TCC-BreastCancerNN\\Projeto 2\\resources\\data_info\\calc_case_description_test_set.csv') as f: 
        reader = csv.reader(f)
        your_list = list(reader)
else:
    print("Invalid option: " + txt)
    exit()
    
    
mal_dest_dir = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\" + folder + "_DIV\\MALIGNANT\\"
ben_dest_dir = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\" + folder + "_DIV\\BENIGN\\"  

for item in your_list:
        wildcard = r'C:/Users/Guilherme/Desktop/IMGMEDICAS/' + folder +'/CBIS-DDSM/' + '*' + str(item[0]) + '*' +'/*/*/*.png'
        for file in glob.glob(wildcard):
            if item[9] == 'MALIGNANT':
                dest_dir = mal_dest_dir
            elif item[9] == 'BENIGN':
                dest_dir = ben_dest_dir
            elif item[9] == 'BENIGN_WITHOUT_CALLBACK':
                dest_dir = ben_dest_dir 
        
            print(file + " moved")
            shutil.move(file, dest_dir)


