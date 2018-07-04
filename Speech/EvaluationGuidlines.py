
class EvaluationGuidlines:

    __Guidelines = {
        "SG" : "You are talking slowly with a suitable volume.\nJust talk faster a little bit.\n",
        "SQ" : "You are talking slowly with a quiet volume.\nPlease, Talk faster and raise your voice.\n",
        "SH" : "You are talking slowly with harmful volume.\nPlease, Talk faster and do not raise it too much.\n",
        "GG" : "Excellent!\n",
        "GQ" : "Very Good! Just raise your voice a little bit.\n",
        "GH" : "Very Good! Just don't shout.\n",
        "FG" : "Good! Just Be slower a little bit.\n",
        "FQ" : "Please, Be slower and raise your voice a little bit.\n",
        "FH" : "You're talking too fast with a too loud voice.\nPlease, Make it slower and don't shout.\n",
        "FR" : "Your Volume's Fixed. Please, Change Your Volume\n",
        "FF" : "Your Volume's Fixed all of The Time\n",
        "NR" : "Hey, wake up! your listeners feel asleep ^_^\n",
        "NF" : "There're a lot of Silence in Record\n"
    }

    # Get the Message from Guidelines Dictionary
    def getMessage(self , keyGuide):
        if "N" in keyGuide:
            return self.__Guidelines[keyGuide.split()[0]]
        elif len(keyGuide) == 2 :
            return self.__Guidelines[keyGuide]
        else :
            keys = keyGuide.split()
            return self.__Guidelines[keys[0]] + self.__Guidelines[keys[1]]

'''
if __name__ == '__main__':
    print(EvaluationGuidlines().getMessage("SQ" + " FR"))
'''