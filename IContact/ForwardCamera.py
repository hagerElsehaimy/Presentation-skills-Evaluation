from imutils.video import VideoStream
from imutils import face_utils
import datetime
import argparse
import imutils
import time
import dlib
import cv2
from IContact.index import Index
import math
from IContact.FaceProcess import FaceProcess
from IContact.processing import AllState
from IContact.Detect import Detect
import threading
from IContact.LoadPredictorFile import LoadPredictorFile


class ForwardCamera():


    def func(self):



        stateOfRecord = ""

        # initialize dlib's face detector (HOG-based) and then create
        # the facial landmark predictor
        # static object

        detector, predictor = LoadPredictorFile.getFile()



        # initialize the video stream and allow the cammera sensor to warmup

        # Open the first webcame device
        #self.vs = cv2.VideoCapture(0)
        # loop over the frames from the video stream




        # Start the window thread for the two windows we are using
        cv2.startWindowThread()

        # Create the tracker we will use
        tracker = dlib.correlation_tracker()

        # The variable we use to keep track of the fact whether we are
        # currently using the dlib tracker
        trackingFace = 0

        # to calculate number of frame
        frameCount = 0

        # coordinate of faical land mark for pervise face
        ListOfIndexOld = []

        # coordinate of faical land mark for current face
        ListOfIndexNew = []
        rectang = []

        self.move = 0

        while True:

            self.lock.acquire()



            # grab the frame from the threaded video stream, resize it to
            # have a maximum width of 400 pixels, and convert it to
            # grayscale
            rc, baseImage = self.capture.read()

            # Result image is the image we will show the user, which is a
            # combination of the original image from the webcam and the
            # overlayed rectangle for the largest face
            frame = baseImage.copy()

            frameCount += 1

            frame = imutils.resize(frame, width=400)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if not trackingFace:

                # detect faces in the grayscale frame
                rects = detector(gray, 1)

                # check if detect faces or not
                if len(rects) >= 1:

                    if len(rects) == 1:
                        # use function crop face to return coordinate to face (x,y,w,h)
                        (x, y, w, h) = FaceProcess.cropFace(rects[0])

                        # Initialize the tracker
                        tracker.start_track(frame,
                                            dlib.rectangle(x,
                                                           y,
                                                           x + w,
                                                           y + h))

                        # Set the indicator variable such that we know the
                        # tracker is tracking a region in the image
                        trackingFace = 1

            # Check if the tracker is actively tracking a region in the image
            if trackingFace:

                # Update the tracker and request information about the
                # quality of the tracking update
                trackingQuality = tracker.update(frame)

                # If the tracking quality is good enough, determine the
                # updated position of the tracked region and draw the
                # rectangle
                #

                tracked_position = tracker.get_position()

                if tracked_position.is_empty() == False and trackingQuality >= 8.75:

                    tracked_position = tracker.get_position()

                    t_x = int(tracked_position.left())
                    t_y = int(tracked_position.top())
                    t_w = int(tracked_position.width())
                    t_h = int(tracked_position.height())

                    rect = dlib.rectangle(t_x, t_y, t_x + t_w, t_y + t_h)

                    # determine the facial landmarks for the face region, then
                    # convert the facial landmark (x, y)-coordinates to a NumPy
                    # array

                    shape = predictor(gray, rect)
                    shape = face_utils.shape_to_np(shape)

                    Count = 0

                    ListOfIndexNew = []

                    for (x, y) in shape:
                        Count += 1

                        indexObj = Index(x, y)
                        ListOfIndexNew.append(indexObj)

                    if len(ListOfIndexNew) != 0:

                        direction = Detect.detectDirection(ListOfIndexNew)

                        stateOfRecordLast = stateOfRecord

                        if (direction[0] != "F" or (direction[0] == "F" and len(direction) != 1)):

                            stateOfRecord = "dir:" + ''.join(direction)
                            state = str(self.recordButton['state'])
                            if state == 'disabled':
                                self.recordButton.configure(state="active")



                        else:

                            stateOfRecord = "dir:-F"

                            FaceProcess.saveFace(frame, ListOfIndexNew)


                        if self.stateOfRecordTextGui['text'] == "END":

                            self.lock.release()
                            break


                        if stateOfRecord != stateOfRecordLast and stateOfRecordLast!="END":
                            self.stateOfRecordTextGui['text'] = stateOfRecord



                            # just copy all element to old
                            ListOfIndexOld = []
                            for x in ListOfIndexNew:
                                ListOfIndexOld.append(x)

                else:
                    # If the quality of the tracking update is not
                    # sufficient (e.g. the tracked region moved out of the
                    # screen) we stop the tracking of the face and in the
                    # next loop we will find the largest face in the image
                    # again
                    trackingFace = 0
                    # Since we want to show something larger on the screen than the
                    # original 320x240, we resize the image again
                    #

            self.lock.release()

            #key = cv2.waitKey(1) & 0xFF

        #self.capture.release()
        cv2.destroyAllWindows()

    def __init__(self,stateOfRecordTextGui,cap,recordButton):

        self.stateOfRecordTextGui = stateOfRecordTextGui

        self.lock = threading.Lock()
        self.capture=cap
        self.recordButton=recordButton


if '__main__'==__name__:
    ForwardCamera("t")