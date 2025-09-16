import cv2
import numpy as np
from sklearn.preprocessing import OneHotEncoder

class Preprocess:

    def __init__(self, images, labels):
        self.images = images
        self.labels = labels

    @staticmethod
    def grayscale(images):
        gray_scaled_images = []
        for img in images:
            grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray_scaled_images.append(np.dstack(grayscale_img).T)
        return np.array(gray_scaled_images)

    def normalize(self):
        return (self.images - np.min(self.images)) / (np.max(self.images) - np.min(self.images))

    def one_hot_encoder(self):
        if len(self.labels.shape) == 1:
            return OneHotEncoder(sparse_output=False).fit_transform(self.labels.reshape(-1, 1))
        elif (len(self.labels.shape) == 2) and (self.labels.shape[-1] == 1):
            return OneHotEncoder(sparse_output=False).fit_transform(self.labels)
        else:
            print("Shape of labels should be (N,) or (N,1)")
            return None

    def full_pipeline_process(self):
        gray_scaled_images = Preprocess.grayscale(self.images)
        preprocess_obj = Preprocess(gray_scaled_images, self.labels)
        images_norm = preprocess_obj.normalize()
        ohe_labels = preprocess_obj.one_hot_encoder()
        return images_norm, ohe_labels




