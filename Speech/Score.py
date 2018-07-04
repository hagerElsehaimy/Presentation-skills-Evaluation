
class Score:

    # Number of errors
    __errorCounter = 0

    # Number of Times Video record
    __FiveSecondCounter = 0

    # Number of correct
    __CorrectCounter = 0

    """
    # Errors Weights for each rule
    __ScoresGuidelines = {
        "SG": 1 ,
        "SQ": 2 ,
        "SH": 2 ,
        "GG": 0 ,
        "GQ": 1 ,
        "GH": 1 ,
        "FG": 1 ,
        "FQ": 2 ,
        "FH": 2 ,
        "FR": 1 ,
        "FF": 1 ,
        "NQ": 2 # Change This
    }
    """
    # Correctness Weights for each rule
    __ScoresGuidelines = {
        "SG": 0.69,  # 0.5 ---> 2.75 / 4
        "SQ": 0.38, # +0.25 ----> 1.5  / 4
        "SH": 0.38, # +0.25 ----> 1.5  / 4
        "GG": 1, # 4  /  4
        "GQ": 0.94, # 0.75 -----> 3.75 / 4
        "GH": 0.94, # 0.75 -----> 3.75 / 4
        "FG": 0.81, # 0.5 -----> 3.25 / 4
        "FQ": 0.56, # 0.5 ----> 2.25 / 4
        "FH": 0.56, # 0.5 ----> 2.25 / 4
        "FR": -0.13, # 0.05 ---- > 0.5 / 4
        "N": 0
    }

    # Count The Error Tries user do
    def IncrementErrorCounter(self , keyGuide):
        if len(keyGuide) == 2:
            self.__errorCounter += self.__ScoresGuidelines[keyGuide]
        else:
            keys = keyGuide.split()
            self.__errorCounter += self.__ScoresGuidelines[keys[0]] + self.__ScoresGuidelines[keys[1]]

    # Count The Correct Tries user do
    def IncrementCorrectCounter(self , keyGuide):
        self.__FiveSecondCounter += 1
        if "N" in keyGuide :
            self.__CorrectCounter += self.__ScoresGuidelines["N"]
        elif len(keyGuide) == 2 :
            self.__CorrectCounter += self.__ScoresGuidelines[keyGuide]
        else :
            keys = keyGuide.split()
            self.__CorrectCounter += self.__ScoresGuidelines[keys[0]] + self.__ScoresGuidelines[keys[1]]
        #print(self.__FiveSecondCounter ,"-------------------------" , self.__CorrectCounter ,keyGuide)

    """"
    def __SummationofAllScores(self):
        ScoresSumm = 0
        for value in self.__ScoresGuidelines.values():
            ScoresSumm += value
        return ScoresSumm

    # get Evaluation Score in Percentage
    def getEvaluationScore(self , keyGuide):
        if self.__errorCounter == 0 :
            self.IncrementErrorCounter(keyGuide)
        errorScore = (self.__errorCounter / self.__SummationofAllScores()) * 100
        trueScore = round(100 - errorScore)
        print(trueScore)
        return trueScore
    """

    # Get Correct Evaluation Score in Percentage
    def getEvaluationScore(self):
        correctScore = round((self.__CorrectCounter / self.__FiveSecondCounter) * 100, 2)
        errorScore = round(100 - correctScore)
        #print(correctScore , "Mine Evaluate" , errorScore)
        return correctScore
'''
if __name__ == '__main__':
    print(Score().getEvaluationScore())
'''