from Speech.SpeechVolume import VolumeStates
import numpy as np

class Volume:

    def __init__(self):
        # Current Intensity
        self.__currentTone = 0

        # Counter to Check if Tone is Fixed or not
        self.__fixedToneCounter = 0

        # Volume States
        self.__volumeStates = VolumeStates.VolumeStates()

        # Total Video Counting Fixed Tones
        self.__totalFixedCounter = 0


    def runVolume(self , snd):
        result = ""
        # Get Intensity
        intensity = snd.to_intensity()

        # Check if The tone as previous tone or not
        prevTone = self.__currentTone
        self.__currentTone = int(round(np.mean(intensity.values)))

        # Check if Tone 's Fixed or Changed
        sub = self.__currentTone - prevTone
        #print(sub , " Fixed Tone" , self.__currentTone)
        if sub == 0:
            self.__fixedToneCounter += 1
            self.__totalFixedCounter += 1
            result = (" FR")

        # Get Volume Evaluate for RealTime
        volumeEvaluate = self.__evaluateVolume(self.__currentTone)

        # increment num of Volume occurs in Dict
        self.__volumeStates.ChangeVolumeStates(volumeEvaluate, self.__currentTone)
        result = volumeEvaluate + result
        return result

    def getVolumeEvaluationForIntervals(self, duration):
        result = ""
        # Get Max Real Time Volume
        maxTone = self.__volumeStates.getMaxVolumeInRealTime()

        # if there are duplicate keys
        if maxTone == "":
            maxTone = self.__evaluateVolume(self.__volumeStates.getMaxTonesInRealTime())

        if self.__fixedToneCounter >= (duration / 2):
            result = (" FR")

        result = maxTone + result

        # Reset Real Time Count
        self.__volumeStates.resetRealTimeVolumeState()
        # reset Variables for another Interval
        self.__fixedToneCounter = 0
        return result


    def getFinalVolumeEvaluation(self, videoLength):
        # When s/he Quit from This
        result = ""
        # Get Final Max Volume Evaluate
        maxTone = self.__volumeStates.getFinalMaxVolume()

        # if there are duplicate keys
        if maxTone == "":
            maxTone = self.__evaluateVolume(self.__volumeStates.getFinalMaxTones())

        #print(self.__totalFixedCounter , self.__fixedToneCounter , videoLength)
        # Evaluate Volume
        if self.__totalFixedCounter >= (round(videoLength * 12)/2):
            result = (" FF")

        result = maxTone + result
        return result

    def __evaluateVolume(self, averageIntensity):
        if averageIntensity >= 50 and averageIntensity < 80:
            return ("G")
        if averageIntensity < 50:
            return ("Q")
        if averageIntensity >= 80:
            return ("H")
