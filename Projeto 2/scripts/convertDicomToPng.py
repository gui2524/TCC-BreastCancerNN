import pydicom as dicom
import os
import cv2
import glob

txt = input("Type [1] for TRAIN or [2] for PREDICT: ") 


if txt == '1':
    folder = "TRAIN"
elif txt == '2':
    folder = "PREDICT"
else:
    print("Invalid option: " + txt)
    exit()
    
# Specify the .dcm folder path
folder_path = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\" + folder + "\\CBIS-DDSM"
# Specify the output jpg/png folder path
jpg_folder_path = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\JPG"
images_path = os.listdir(folder_path)

wildcard = r'C:/Users/Guilherme/Desktop/IMGMEDICAS/' + folder + '/CBIS-DDSM/*/*/*/*0.dcm'
i = 0
for file in glob.glob(wildcard):
        ds = dicom.dcmread(file, force=True)
        pixel_array_numpy = ds.pixel_array
        image = file.replace('.dcm', str(i) + '.png')
        cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
        print(i)


