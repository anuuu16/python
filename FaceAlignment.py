import sys

import dlib

# if len(sys.argv) != 3:
#     print(
#         "Call this program like this:\n"
#         "   ./face_alignment.py shape_predictor_5_face_landmarks.dat ../examples/faces/bald_guys.jpg\n"
#         "You can download a trained facial shape predictor from:\n"
#         "    http://dlib.net/files/shape_predictor_5_face_landmarks.dat.bz2\n")
#     exit()

predictor_path = 'D:/Projects/Python/Pre Trained Models/dlib-models\shape_predictor_5_face_landmarks.dat'
face_file_path = 'D:/Projects/Python/SampleImages/GroupFaces/2.jpg'

# Load all the models we need: a detector to find the faces, a shape predictor
# to find face landmarks so we can precisely localize the face
detector = dlib.get_frontal_face_detector()
sp = dlib.shape_predictor(predictor_path)

# Load the image using Dlib
img = dlib.load_rgb_image(face_file_path)

# Ask the detector to find the bounding boxes of each face. The 1 in the
# second argument indicates that we should upsample the image 1 time. This
# will make everything bigger and allow us to detect more faces.
dets = detector(img, 1)
window = dlib.image_window()
window.set_image(img)
num_faces = len(dets)
if num_faces == 0:
    print("Sorry, there were no faces found in '{}'".format(face_file_path))
    exit()
print("There were {} faces found in '{}'".format(len(dets),face_file_path))
# Find the 5 face landmarks we need to do the alignment.
faces = dlib.full_object_detections()
for detection in dets:
    faces.append(sp(img, detection))

window = dlib.image_window()
window.set_image(img)
# Get the aligned face images
# Optionally: 
# images = dlib.get_face_chips(img, faces, size=160, padding=0.25)
images = dlib.get_face_chips(img, faces, size=320)
for image in images:
    window.set_image(image)
    dlib.hit_enter_to_continue()

# It is also possible to get a single chip
image = dlib.get_face_chip(img, faces[0], size=160, padding=0.25)
window.set_image(image)
dlib.hit_enter_to_continue()