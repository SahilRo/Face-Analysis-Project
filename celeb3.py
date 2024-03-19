import os
import cv2
from celeb import top_matches_indices
directory_path = r"C:\Users\Sahil\Downloads\archive (8)"
all_files = os.listdir(directory_path)
image_files = [file for file in all_files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
image_file_paths = [os.path.join(directory_path, file) for file in image_files]
for index in top_matches_indices:
    celebrity_image_path = image_file_paths[index]
    celebrity_image = cv2.imread(celebrity_image_path)
    cv2.imshow('Celebrity Look-Alike', celebrity_image)
    cv2.waitKey(0)
cv2.destroyAllWindows()