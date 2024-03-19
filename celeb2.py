import numpy as np
import cv2
import face_recognition
import os

def extract_face_features(face_image):
    face_landmarks = face_recognition.face_encodings(face_image)
    if len(face_landmarks) == 0:
        return None
    face_features = np.array(face_landmarks[0])
    return face_features

def create_feature_dataset(celebrity_images):
    feature_dataset = []

    for image_path in celebrity_images:
        face_image = cv2.imread(image_path)
        face_features = extract_face_features(face_image)

        if face_features is not None:
            feature_dataset.append(face_features)
    feature_dataset = np.array(feature_dataset)

    return feature_dataset



dataset_directory = r"C:\Users\Sahil\Downloads\archive (8)"
file_names = os.listdir(dataset_directory)
your_dataset_paths = [os.path.join(dataset_directory, file_name) for file_name in file_names]
celebrity_feature_dataset = create_feature_dataset(your_dataset_paths)
print(celebrity_feature_dataset)