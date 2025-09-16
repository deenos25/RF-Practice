# https://github.com/benjaminlewis-afrl/SAMPLE_dataset_public
import cv2
import os
import numpy as np
from preprocess_data import Preprocess
from sklearn.model_selection import train_test_split

# Load saved data
data = np.load('data/SAR/real_raw_dataset.npz')
images, labels = data['img_arr'], data['labels']

# Preprocess Data
images_norm, ohe_labels = Preprocess(images, labels).full_pipeline_process()
# Train, Validation, and Test Splits
train_val_images, test_images, train_val_labels, test_labels = train_test_split(images_norm, ohe_labels, test_size=0.2, random_state=0)
train_images, val_images, train_labels, val_labels = train_test_split(train_val_images, train_val_labels, test_size=0.25, random_state=0)