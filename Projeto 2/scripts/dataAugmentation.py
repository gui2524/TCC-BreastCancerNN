import os
from PIL import Image
import glob

images_path_benign = r"C:/Users/user/Desktop/tcc/classifying-cancer/cnn_image_classifier/images/train/benign/*"
images_path_malignant = r"C:/Users/user/Desktop/tcc/classifying-cancer/cnn_image_classifier/images/train/malignant/*"

i = 0
for file in glob.glob(images_path_benign):
        in_file, ext = os.path.splitext(file)
        image_obj = Image.open(file)
        rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
        rotated_image.save(in_file + "_t.png", "PNG")
        print(i)
        i+=1