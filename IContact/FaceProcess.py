import cv2

class FaceProcess():


    @staticmethod
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

    @staticmethod
    def crop_image_List(face):
        x = face[1 - 1].x
        y = face[3 - 1].y - (face[9 - 1].y - face[3 - 1].y)
        h = (face[9 - 1].y - face[3 - 1].y) * 2
        w = (face[9 - 1].x - x) * 2
        return (x, y, w, h)

    @staticmethod
    def saveFace(img,face):
        (x,y,w,h)=FaceProcess.crop_image_List(face)
        cv2.imwrite("yourPhoto"+".jpg", img[y:y+h,x:x+w])
