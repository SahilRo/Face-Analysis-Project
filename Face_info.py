'''import f_Face_info
import cv2
import time
import imutils
import argparse

parser = argparse.ArgumentParser(description="Face Info")
parser.add_argument('--input', type=str, default='webcam',
                    help="webcam or image")
parser.add_argument('--path_im', type=str,
                    help="path of image")
args = vars(parser.parse_args())

type_input = args['input']
if type_input == 'image':
    frame = cv2.imread(args['path_im'])
    out = f_Face_info.get_face_info(frame)
    res_img = f_Face_info.bounding_box(out, frame)
    cv2.imshow('Face info', res_img)
    cv2.waitKey(0)

if type_input == 'webcam':
    cv2.namedWindow("Face info")
    cam = cv2.VideoCapture(0)
    while True:
        star_time = time.time()
        ret, frame = cam.read()
        frame = imutils.resize(frame, width=720)
        out = f_Face_info.get_face_info(frame)
        res_img = f_Face_info.bounding_box(out, frame)

        end_time = time.time() - star_time
        FPS = 1 / end_time
        cv2.putText(res_img, f"FPS: {round(FPS, 3)}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Face info', res_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break'''


import cv2
import time
import imutils
import argparse
import dlib
import numpy as np

from f_Face_info import get_face_info, bounding_box
face_detector = dlib.get_frontal_face_detector()
landmark_predictor = dlib.shape_predictor(r"C:\Users\Sahil\Downloads\a.dat")

# Load the avatar image
avatar_image = cv2.imread(r"C:\Users\Sahil\Downloads\Screenshot 2023-07-26 193725.png")

parser = argparse.ArgumentParser(description="Face Info")
parser.add_argument('--input', type=str, default='webcam', help="webcam or image")
parser.add_argument('--path_im', type=str, help="path of image")
args = vars(parser.parse_args())

type_input = args['input']
if type_input == 'image':
    frame = cv2.imread(args['path_im'])
    out = get_face_info(frame)
    res_img = bounding_box(out, frame)
    cv2.imshow('Face info', res_img)
    cv2.waitKey(0)

if type_input == 'webcam':
    cv2.namedWindow("Face info")
    cam = cv2.VideoCapture(0)
    while True:
        star_time = time.time()
        ret, frame = cam.read()
        frame = imutils.resize(frame, width=720)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector(gray)

        for face in faces:
            landmarks = landmark_predictor(gray, face)

            # Overlay the avatar on the face (similar to previous example)
            points = np.array([[p.x, p.y] for p in landmarks.parts()])
            x, y, w, h = cv2.boundingRect(points)
            avatar_resized = cv2.resize(avatar_image, (w, h))
            frame[y:y + h, x:x + w] = avatar_resized

        out = get_face_info(frame)
        res_img = bounding_box(out, frame)

        end_time = time.time() - star_time
        FPS = 1 / end_time
        cv2.putText(res_img, f"FPS: {round(FPS, 3)}", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Face info', res_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
