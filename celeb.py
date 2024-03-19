import cv2
import face_recognition
import numpy as np
import dlib
from celeb2 import celebrity_feature_dataset
def extract_face_features(face_image):
    face_landmarks = face_recognition.face_encodings(face_image)
    if len(face_landmarks) == 0:
        return None
    face_features = np.array(face_landmarks[0])
    return face_features

def find_celebrity_look_alikes(user_face_features, celebrity_database, N):
    similarities = np.linalg.norm(celebrity_database - user_face_features, axis=1)
    sorted_indices = np.argsort(similarities)
    top_matches_indices = sorted_indices[:N]
    return top_matches_indices
celebrity_database = celebrity_feature_dataset

user_face_image = cv2.imread(r"C:\Users\Sahil\Downloads\NEW\Sahil\90.jpg")
user_face_features = extract_face_features(user_face_image)
N = 5
top_matches_indices = find_celebrity_look_alikes(user_face_features, celebrity_database, N)
'''for idx in top_matches_indices:
    celebrity_image = load_celebrity_image_from_index(idx)
    cv2.imshow(f"Celebrity Look-Alike {idx}", celebrity_image)'''
cv2.waitKey(0)
cv2.destroyAllWindows()
print(top_matches_indices)