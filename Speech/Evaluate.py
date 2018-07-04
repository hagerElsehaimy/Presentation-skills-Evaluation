from Speech.SpeechProcessing.FilterAudio import *
from Speech.SpeechRate.RateEvaluate import *
from Speech.SpeechVolume.VolumeEvaluate import *
from Speech.EvaluationGuidlines import *
from Speech.Score import *
import parselmouth
import threading

class Evaluate:

    # Count of Seconds until Minute
    __secondCount = 0
    # Number of Minutes Total of Video
    __videoLength = 0
    # Voice Duration that user's choosen
    __evaluationDuration = 1

    def __init__(self,  duration = 1 , data = " "):
        # Record Evaluation Duration
        self.__evaluationDuration = duration / 5
        # SpeechRate Object
        self.__rate = SpeechRate()
        # Volume Object
        self.__volume = Volume()
        #Score Object
        self.__score = Score()
        # Voice Msg
        self.__voiceMsg = data

    # Evaluate All the Entire Record
    def evaluateRecord(self):

        # When s/he Quit from Record
        self.__exitLoop = True
        #self.__lock.release()

        # Final Evaluation Result
        EvaluateResult = ""

        #print("=================================")
        #print("Minutes ", self.__videoLength)
        #print("Final Evaluation : ")

        # Final Evaluate Rate && Volume
        EvaluateResult += self.__rate.getFinalRateEvaluation()
        EvaluateResult += self.__volume.getFinalVolumeEvaluation(self.__videoLength)
        #print(EvaluateResult)

        # return Msg  &&  Speech Evaluate
        return EvaluationGuidlines().getMessage(EvaluateResult) , self.__score.getEvaluationScore()

    # Evaluate Record in Real Time
    def evaluateSpeechRealTime(self , END , evaluateBtn):
        #print("start run")
        self.__lock = threading.Lock()
        self.__exitLoop = False

        #print("Recording..........")
        while True:
            # Acquire a lock
            self.__lock.acquire()

            # First, Record Audio
            # Second, Filter Audio
            AudioFilter = Filter()
            WavFilter = AudioFilter.getAudioFiltered()

            if self.__exitLoop:
                #print("Release Voice")
                break

            # Third, Analyze Wave File with parselmouth library
            snd = parselmouth.Sound(WavFilter)

            # Fourth, Run Speech Rate & Volume
            RateEvaluate = self.__rate.runSpeechRate(snd)
            VolumeEvaluate = self.__volume.runVolume(snd)

            # Increase or Decrease Score of every five Seconds
            self.__score.IncrementCorrectCounter(RateEvaluate + VolumeEvaluate)

            # Enable Evaluate Button
            if self.__videoLength == 0:
                evaluateBtn.configure(state="active")

            # Calculate Video Length
            self.__CalcVideoLength()
            #print(self.__videoLength, "Video length")

            # Count Seconds
            self.__secondCount += 1
            #print(self.__secondCount*5 , "Second")

            # Check If Seconds Count Equal Record  Evaluation Duration
            if(self.__secondCount == self.__evaluationDuration):

                EvaluateResult = ""
                # Get Speech rate & Volume Evaluate
                EvaluateResult += self.__rate.getRateEvaluationForIntervals()
                EvaluateResult += self.__volume.getVolumeEvaluationForIntervals(self.__secondCount)

                # Get Message from Evaluation Guidelines
                self.__voiceMsg.insert(END , EvaluationGuidlines().getMessage(EvaluateResult))
                self.__voiceMsg.insert(END , "ــــ"*28)
                #print(EvaluationGuidlines().getMessage(EvaluateResult))

                # reset counting seconds
                self.__secondCount = 0
                #print("Recording..........")

            self.__lock.release()

    # Increse Video Length every 5 seconds
    def __CalcVideoLength(self):
        increaseAmount = 5 / 60
        self.__videoLength += increaseAmount


"""
if __name__ == '__main__':
    #q = queue.Queue()
    Evaluate(0).evaluateSpeechRealTime()
    ev = Evaluate(2)
    while True:
    try:
        start_new_thread(ev.evaluateRealTime, ())
        time.sleep(10000000)
    except:
        print("Error: unable to start thread")
    """