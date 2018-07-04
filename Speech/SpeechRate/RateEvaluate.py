from Speech.SpeechRate import Praat
from Speech.SpeechRate import RateStates

class SpeechRate:

    def __init__(self):

        self.__rateStates = RateStates.RateStates()


    def runSpeechRate(self, snd):
        praatScript = Praat.Praat()

        # words analysis every 5 seconds
        words = praatScript.calcSyllbale(snd)
        #print(words , "Num of Spoken Words")

        # Get Rate Evaluate
        rateEvaluate = self.__evaluateRate((words / (5/60)))

        # increment num of Rate occurs in Dict
        self.__rateStates.ChangeRateStates(rateEvaluate , words)

        return rateEvaluate

    def getRateEvaluationForIntervals(self):
            # Get Max Real Time Rate
            maxRate = self.__rateStates.getMaxRateInRealTime()

            # if there are duplicate keys
            if maxRate == "":
                maxRate = self.__evaluateRate(self.__rateStates.getMaxWordsInRealTime() / (5/60))

            if "N" in maxRate:
                maxRate = "NR N"
            # Reset Real Time Count
            self.__rateStates.resetRealTimeRates()
            return maxRate

    def getFinalRateEvaluation(self):
        # When s/he Quit from This
        # Get Final Max Rate
        maxRate = self.__rateStates.getFinalMaxRate()

        # if there are duplicate keys
        if maxRate == "":
            maxRate = self.__evaluateRate(self.__rateStates.getFinalMaxWords() / (5 / 60))

        if "N" in maxRate:
            maxRate = "NF N"
        return maxRate

    def __evaluateRate(self , words):
        #print(words)
        if words < 25: ## 20
            return("N")
        if words < 70:
            return ("S")
        elif words >= 70 and words < 100:  # maybe <105 or <120 it need more test
            return ("G")
        elif words >= 100:
            return ("F")

