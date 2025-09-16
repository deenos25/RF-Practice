import cv2
import os
import numpy as np

# Get directory of folders/files
root_dir = "data/SAR/real"
tank_types = os.listdir(root_dir)

# Loop through different type of tank folder and get images
img_arr, labels = [], []
for tank in tank_types:
    for png_file in os.listdir(os.path.join(root_dir, tank)):
        img = cv2.imread(os.path.join(root_dir, tank, png_file))
        img_arr.append(img)
        labels.append(tank)
img_arr, labels = np.array(img_arr), np.array(labels)

# Save images and labels
saved_file_name = 'data/SAR/real_raw_dataset.npz'
np.savez_compressed(saved_file_name, img_arr=img_arr, labels=labels)
print('Data saved under', saved_file_name)