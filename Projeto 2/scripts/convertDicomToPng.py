import pydicom as dicom
import os
import cv2
import glob
# make it True if you want in PNG format
PNG = True
# Specify the .dcm folder path
folder_path = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\TRAIN\\CBIS-DDSM"
# Specify the output jpg/png folder path
jpg_folder_path = "C:\\Users\\Guilherme\\Desktop\\IMGMEDICAS\\JPG"
images_path = os.listdir(folder_path)

wildcard = r'C:/Users/Guilherme/Desktop/IMGMEDICAS/TRAIN/CBIS-DDSM/*/*/*/*'
i = 0
for file in glob.glob(wildcard):
    ds = dicom.dcmread(file, force=True)
    pixel_array_numpy = ds.pixel_array
    image = file.replace('.dcm', str(i) + '.png')
    cv2.imwrite(os.path.join(jpg_folder_path, image), pixel_array_numpy)
    print(i)
    i+=1


