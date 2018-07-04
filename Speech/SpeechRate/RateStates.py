from Speech.SpeechStates import SpeechStates

class RateStates(SpeechStates) :

    def __init__(self):

        self.__totalCountOfRates = {
            "N": [0, 0],
            "S": [0, 0],
            "G": [0, 0],
            "F": [0, 0]
        }

        self.resetRealTimeRates()


    def ChangeRateStates(self , rateState , NumofWords):
        # First , Increment Rate State Count
        self.__incrementRateCount(rateState)

        # Second , Increment Number of words
        self.__incrementRateWords(rateState , NumofWords)

        #print(self.__countRatesInRealTime, "  Count Rates In Real Time")
        #print(self.__totalCountOfRates, "   Total Rates Count ")

    # Increment Rate Count in Both Dictionaries
    def __incrementRateCount(self , rateState):
        self.__countRatesInRealTime[rateState][0] += 1
        self.__totalCountOfRates[rateState][0] += 1

    # Increment Rate Words in Both Dictionaries
    def __incrementRateWords(self , rateState , words):
        self.__countRatesInRealTime[rateState][1] += words
        self.__totalCountOfRates[rateState][1] += words

    # Get Maximum Rate in Real Time return "" if max Rate is Duplicate
    def getMaxRateInRealTime(self):
        return self.getMaxState(self.__countRatesInRealTime)

    # get Average of Words for duplicate Keys to know max rate
    def getMaxWordsInRealTime(self):
        return self.getAverageState(self.__countRatesInRealTime)

    # Reset Real Time Rates Values to 0 for new Interval
    def resetRealTimeRates(self):
        self.__countRatesInRealTime = {
            "N": [0, 0],
            "S": [0, 0],
            "G": [0, 0],
            "F": [0, 0]
        }

    # Get Total Maximum Rate
    def getFinalMaxRate(self):
        return self.getMaxState(self.__totalCountOfRates)

    # Get Average of Words for duplicate Keys to know max rate
    def getFinalMaxWords(self):
        return self.getAverageState(self.__totalCountOfRates)


if __name__ == '__main__':
    r = RateStates()
    while True:
        r.ChangeRateStates("N" , 5)