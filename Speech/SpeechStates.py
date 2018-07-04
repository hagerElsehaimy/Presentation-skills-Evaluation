
class SpeechStates :

    # Get Max State from Dictionary
    def __getMax(self, dic):
        return max(dic.keys(), key=(lambda key: dic[key][0]))

    # Get Max State from Dictionary
    def getMaxState(self , dic):
        maxState = self.__getMax(dic)
        return self.__CheckMaxStateISDuplicate(maxState, dic)

    # Check if two or more Max Rate/Volume Dic has Same Equal Values
    def __CheckMaxStateISDuplicate(self, maxStateKey, dic):
        maxStatevalue = dic[maxStateKey]
        for key, value in dic.items():
            if value[0] == maxStatevalue[0] and key != maxStateKey:
                return ""
        return maxStateKey

    # Get List of Duplicate Keys in Dic
    def __getDuplicateMaxState(self, dic):
        duplicateKeys = []
        maxStateKey = self.__getMax(dic)
        duplicateKeys.append(maxStateKey)
        maxStatevalue = dic[maxStateKey]
        for key, value in dic.items():
            if value[0] == maxStatevalue[0] and key != maxStateKey:
                duplicateKeys.append(key)
        return duplicateKeys

    # Get Words\Tones Average --> Num of words\Tones / Num of occurs
    def __getAverage(self, duplicateKeys, dic):
        numWords = 0
        numOccurs = 0
        for key in duplicateKeys:
            numOccurs += dic[key][0]
            numWords += dic[key][1]
        return numWords / numOccurs

    # Get Duplicate Keys then get Average State for Specific Dictionary
    def getAverageState(self , dic):
        duplicateKeys = self.__getDuplicateMaxState(dic)
        averageTones = self.__getAverage(duplicateKeys, dic)
        return averageTones
