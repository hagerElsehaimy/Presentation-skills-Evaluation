from Speech.SpeechStates import SpeechStates


class VolumeStates(SpeechStates) :

    def __init__(self):

        self.__totalCountOfVolume = {
            "Q": [0, 0],
            "G": [0, 0],
            "H": [0, 0]
        }

        self.resetRealTimeVolumeState()


    def ChangeVolumeStates(self , volumeState , NumofTones):
        # First , Increment Volume State Count
        self.__incrementVolumeCount(volumeState)

        # Second , Increment Number of tones
        self.__incrementVolumeTones(volumeState , NumofTones)

        #print(self.__countVolumeInRealTime, "  Count Volume In Real Time")
        #print(self.__totalCountOfVolume, "   Total Volume Count ")

    # Increment Volume Count in Both Dictionaries
    def __incrementVolumeCount(self , volumeState):
        self.__countVolumeInRealTime[volumeState][0] += 1
        self.__totalCountOfVolume[volumeState][0] += 1

    # Increment Volume Tones in Both Dictionaries
    def __incrementVolumeTones(self , volumeState , tones):
        self.__countVolumeInRealTime[volumeState][1] += tones
        self.__totalCountOfVolume[volumeState][1] += tones

    # Get Maximum Volume in Real Time return "" if max Volume is Duplicate
    def getMaxVolumeInRealTime(self):
        return self.getMaxState(self.__countVolumeInRealTime)

    # get Average of Tones for duplicate Keys to know Real Time max volume
    def getMaxTonesInRealTime(self):
        return self.getAverageState(self.__countVolumeInRealTime)

    # Reset Real Time Volume Values to [ 0 , 0 ] for new Interval
    def resetRealTimeVolumeState(self):
        self.__countVolumeInRealTime = {
            "Q": [0, 0],
            "G": [0, 0],
            "H": [0, 0]
        }

    # Get Total Maximum Volume
    def getFinalMaxVolume(self):
        return self.getMaxState(self.__totalCountOfVolume)

    # Get Average of Tones for duplicate Keys to know Final max volume
    def getFinalMaxTones(self):
        return self.getAverageState(self.__totalCountOfVolume)
