#


import face_recognition
import cv2
from IContact.FaceProcess import FaceProcess



def cropFace(rect):
    # take a bounding predicted by dlib and convert it
    # to the format (x, y, w, h) as we would normally do
    # with OpenCV
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    # return a tuple of (x, y, w, h)
    return (x, y, w, h)

def crop_image_safaa(face):
    x = face[1 - 1].x
    y = face[3 - 1].y - (face[9 - 1].y - face[3 - 1].y)
    h = (face[9 - 1].y - face[3 - 1].y) * 2
    w = (face[9 - 1].x - x) * 2
    return (x, y, w, h)


def DoRecognation(rects,Frame):

    for rect in rects:
        (x, y, w, h)=FaceProcess.cropFace(rect)
        cropImage=Frame[y:y+h,x:x+w]
        if(Recogation(cropImage)):
            return (x,y,w,h)

    return (None,None,None,None)


def Recogation(img):
    picture_of_me = face_recognition.load_image_file("..\Gui\yourPhoto.jpg")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]


    #unknown_picture = face_recognition.load_image_file("3.png")
    try:
        unknown_face_encoding = face_recognition.face_encodings(img)[0]

        # Now we can see the two face encodings are of the same person with `compare_faces`!

        results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

        if results[0] == True:


            return True
        else:

            return False
    except:

        return False