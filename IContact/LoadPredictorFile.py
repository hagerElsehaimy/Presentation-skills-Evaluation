import dlib

class LoadPredictorFile():

    detector = dlib.get_frontal_face_detector()
    predictor = None




    @staticmethod
    def getFile():
        if LoadPredictorFile.predictor==None:
            LoadPredictorFile.predictor=dlib.shape_predictor("..\IContact\shape_predictor_68_face_landmarks.dat")
        return LoadPredictorFile.detector,LoadPredictorFile.predictor



