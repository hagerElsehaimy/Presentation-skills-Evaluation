# import the necessary packages
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
from IContact.recongation import *
from IContact.Detect import Detect
import threading
from IContact.LoadPredictorFile import LoadPredictorFile
from IContact.Evaluate import evaluate


class IContact:



    def Evaluate(self):

        #self.lock.acquire()
        self.exitLoop = True
        #self.lock.release()

        tim = Detect.timer(self.start_time, time.time())


        Obj = evaluate(AllState.dictonary, self.move, tim,self.selectOption,self.outcamera)
        res ,score= Obj.result()




        return res,score




    def func(self):
        self.outcamera=0

        self.lock = threading.Lock()

        self.exitLoop = False

        #AllState.dictonary={"R":0,"L":0,"U":0,"D":0,"F":0,"RError":0,"LError":0,"Rp":0,"Lp":0}

        stateOfRecord = ""

        self.start_time = time.time()

        self.NotFoundCounter=0


        # initialize dlib's face detector (HOG-based) and then create
        # the facial landmark predictor
        # static object

        detector, predictor = LoadPredictorFile.getFile()


        # initialize the video stream and allow the cammera sensor to warmup

        # Open the first webcame device
        #self.capture = cv2.VideoCapture(0)
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
        dicSave = {}
        self.move = 0
        start = False

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



            if self.NotFoundCounter>10:
                if not (self.noticeLabel['text'] == "you out Camera") :
                    self.noticeLabel['text']="you out Camera"
                self.NotFoundCounter=0




            if self.NotFoundCounter==-1:
                if self.noticeLabel['text'] == "you out Camera"  :
                    self.noticeLabel['text']="Start Record"
                    self.outcamera+=1



            if frameCount > 10:

                if frameCount % 10 == 0:

                    d = AllState()
                    d.saveChange(dicSave)
                    dicSave = {}


            frame = imutils.resize(frame, width=400)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            if not trackingFace:

                # detect faces in the grayscale frame
                rects = detector(gray, 1)

                if len(rects)==0:
                    self.NotFoundCounter+=1


                # check if detect faces or not
                if len(rects) >= 1:

                    self.NotFoundCounter=-1



                    if len(rects) == 1:
                        # use function crop face to return coordinate to face (x,y,w,h)
                        (x, y, w, h) = FaceProcess.cropFace(rects[0])

                    else:
                        # if i detect many face at first determine which face
                        # i need to track it throw recongation  after that
                        # track it
                        (x, y, w, h) = DoRecognation(rects, frame)

                        # if not recongnaize any face
                        # all face return false
                        if x == None:
                            continue



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
                        position = Detect.detectPosition(ListOfIndexNew[0].x)

                        dicSave[frameCount] = [direction, position]
                        frameCount += 1





                        if len(ListOfIndexNew) != 0 and len(ListOfIndexOld) == 0:
                            rectang = Detect.locate_of_face_esraa(ListOfIndexNew)


                        if len(ListOfIndexNew) != 0 and len(ListOfIndexOld) != 0:
                            if len(rectang) != 0:
                                p, rectang = Detect.compare(rectang, ListOfIndexNew)
                                if p == "Left" or p == "Right":
                                    self.move += 1



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


            key = cv2.waitKey(1) & 0xFF


            #to exit loop and start evaluate
            if self.exitLoop:
                break
            self.lock.release()

        self.capture.release()
        cv2.destroyAllWindows()

    def __init__(self,selectOption,cap,notice):

        self.selectOption=selectOption
        self.capture=cap
        self.noticeLabel=notice







#IContact()