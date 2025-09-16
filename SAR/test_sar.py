# https://github.com/benjaminlewis-afrl/SAMPLE_dataset_public
import cv2
image_path = "data/SAR/real/t72/t72_real_A_elevDeg_016_azCenter_013_77_serial_812.png"
img = cv2.imread(image_path)
cv2.imshow("Tank Image", img)
cv2.waitKey(0)
print(img.shape)
