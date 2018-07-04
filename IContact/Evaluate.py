from IContact.TableRule import tableRule
import operator


"""
class evaluate():

    def __init__(self,dictionary,moveHead,tim,location):
        self.time=tim
        self.body=moveHead
        self.move=dictionary
        self.direction = {'F': 0, 'R': 0, 'L': 0, 'U': 0, 'D': 0}
        self.location=location

    def calc(self):
        self.direction['F']=self.move['F']
        self.direction['R']=self.move['R']+self.move['Rp']
        self.direction['L'] = self.move['L'] + self.move['Lp']
        self.direction['U'] = self.move['U']
        self.direction['D'] = self.move['D']


    def MaxMin(self):
        sum=0
        dic={}
        for key, value in self.direction.items():
            sum+=value

        maxKey = ""
        minKey = ""
        up = False
        down = False

        if sum!=0:
            for key, value in self.direction.items():
                dic[key]=(value/sum)*100
            min=9999
            for key, value in dic.items():
                if value>50 :
                    maxKey=key

                if value<25 and value<min and key!='U' and key!='D' and value!=0:
                    min=value
                    minKey=key

                if key=='D' and value>25 and value<50:
                    down=True

                if key=='U' and value>25 and value<50:
                    up=True

        return maxKey,minKey,up,down

    def evaluate_body(self):
        hour,minite,sec=self.time.split(":")
        hourtom=int(float(hour)*60*60


                    )
        minittom=int(float(minite)*60)
        total=hourtom+minittom+int(float(sec))
        total=int(total/50)
        #print (total,"  ",self.body)
        if total/2<self.body and total*2>self.body :
            return True
        elif total*2<self.body:
            return "more"
        elif total/2>self.body:
            return "less"

    def score(self,Nerror):
        score=Nerror*100/len(tableRule)
        score=100-score
        #print (score)
        #print (len(tableRule))
        return score

    def result(self):
        n = 0
        listMessage = []
        mistake = False

        for key, value in self.move.items():
            if value == 0 and key != 'LError' and key != 'RError':
                mistake = True
        if self.location == "small":
            numOfMove = True
        else:
            numOfMove = self.evaluate_body()

        if not mistake and numOfMove == True:
            listMessage.append(tableRule["goodAllDirection"])

        if self.move['L'] == 0:
            listMessage.append(tableRule["L0"])
            n += 1
        if self.move['Lp'] == 0 and self.location != "small":
            if self.move['L'] == 0:
                n += 1
                pass
            else:
                n += 1
                listMessage.append(tableRule["L-Lp0"])
        if self.move['R'] == 0:
            n += 1
            listMessage.append(tableRule["R0"])
        if self.move['Rp'] == 0 and self.location != "small":
            if self.move['R'] == 0:
                n += 1
            else:
                n += 1
                listMessage.append(tableRule["R-Rp0"])

        if self.move["U"] == 0 and self.location == "hall":
            n += 1
            listMessage.append(tableRule["U0"])

        if self.move["D"] == 0 and self.location == "Threater":
            n += 1
            listMessage.append(tableRule["D0"])
        if self.move["F"] == 0:
            n += 1
            listMessage.append(tableRule["F0"])

        self.calc()

        max, min, up, down = self.MaxMin()
        if max != min:
            if max != '':
                listMessage.append(tableRule[max + "m"])
            if min != '':
                listMessage.append(tableRule[min + "f"])

        if self.move['RError'] != 0:
            listMessage.append(tableRule["RError"])

        if self.move['LError'] != 0:
            listMessage.append(tableRule["LError"])

        if up and self.location != "hall":
            listMessage.append(tableRule["U1"])
            n += 1

        if down and self.location != "Threater":
            n += 1
            listMessage.append(tableRule["D1"])

        if numOfMove == "more":
            n += 1
            listMessage.append(tableRule["M"])
        elif numOfMove == "less" and self.location != "small":
            n += 1
            listMessage.append(tableRule["ML"])
        score=self.score(n)
        return listMessage,score
"""
class evaluate():

    def __init__(self,dictionary,moveHead,tim,location,outofcamera):
        self.time=tim
        self.body=moveHead
        self.move=dictionary
        self.direction = {'F': 0, 'R': 0, 'L': 0, 'U': 0, 'D': 0}
        self.location=location
        self.listMessage = []
        self.numberOfError = 0
        self.mistake = False
        self.outofcamera=outofcamera

    def calc(self):
        self.direction['F']=self.move['F']
        self.direction['R']=self.move['R']+self.move['Rp']
        self.direction['L'] = self.move['L'] + self.move['Lp']
        self.direction['U'] = self.move['U']
        self.direction['D'] = self.move['D']


    def MaxMin(self):
        sum=0
        dic={}
        for key, value in self.direction.items():
            sum+=value

        maxKey = ""
        minKey = ""
        up = False
        down = False

        if sum!=0:
            for key, value in self.direction.items():
                dic[key]=(value/sum)*100
            min=9999
            for key, value in dic.items():
                if value>50 :
                    maxKey=key

                if value<25 and value<min and key!='U' and key!='D' and value!=0:
                    min=value
                    minKey=key

                if key=='D' and value>25 and value<50:
                    down=True

                if key=='U' and value>25 and value<50:
                    up=True

        return maxKey,minKey,up,down

    def evaluate_body(self):
        hour,minite,sec=self.time.split(":")
        hourtom=int(float(hour)*60*60)
        minittom=int(float(minite)*60)
        total=hourtom+minittom+int(float(sec))
        total=int(total/50)

        if total*2<self.body:
            return "more"
        elif total/2>self.body:
            return "less"
        else:
            return True

    def FinalScore(self,AllDirect,forward,totalRight,totalleft,up,down,MINMAX,move,out):
        Score=0
        # minus out from screan
        if self.location!='':
                if self.outofcamera==0:
                    Score+=5
                if forward:
                    Score += 10
                    if MINMAX != "F":
                        Score += 10

                if out == 1:
                    Score += 2.5

                if out == 0:
                    Score += 5


        if self.location=="small" or self.location=="big":
            if (AllDirect)==False:
                Score=10
                return Score
            if up != True:
                Score += 10

            if down != True:
                Score += 10


        if (self.location=="big")or self.location=="Threater":
            if move == True:
                Score += 10

            if self.move['R'] != 0:
                Score += 5
                if MINMAX != "R":
                    Score += 10
            if self.move['Rp'] != 0:
                Score+=5


            if totalleft != 0:
                Score += 5
                if MINMAX != "L":
                    Score += 10
            if self.move['Lp'] != 0:
                Score+=5


        elif (self.location == "small"):

                if totalRight!=0:
                    Score+=10
                    if MINMAX!="R":
                        Score+=10

                if totalleft != 0:
                    Score += 10
                    if MINMAX != "L":
                        Score += 10

                if move !="more":
                    Score += 10


        elif self.location=="Threater":
            if (AllDirect) == False and down != True:
                Score = 10
                return Score
            if up != True:
                Score += 10

            if down == True:
                Score += 10

            if AllDirect==True and down==True:
                self.listMessage.append(tableRule["goodAllDirection"])
        elif self.location=="hall":
            if (AllDirect) == False and up!=True:
                Score=10
                return Score
            if up == True:
                Score += 10

            if down != True:
                Score += 10

            if AllDirect==True and up==True:
                self.listMessage.append(tableRule["goodAllDirection"])

        return Score



    def EvaluateRight(self):
        totalRight=0
        if self.move['R'] == 0 and self.move['Rp']==0:
            self.listMessage.append(tableRule["R0"])
        else:
            totalRight+=1
        if self.move['Rp'] == 0 and self.location != "small":
            if self.move['R'] != 0:
                self.listMessage.append(tableRule["R-Rp0"])
        if self.move['Rp'] != 0:
            totalRight+=1


        return totalRight

    def EvaluateLeft(self):
        totalLeft=0
        if self.move['L'] == 0 and self.move["Lp"]==0:
            self.listMessage.append(tableRule["L0"])
        else:
            totalLeft+=1
        if self.move['Lp'] == 0 and self.location != "small":
            if self.move['L'] != 0:
                self.listMessage.append(tableRule["L-Lp0"])
        if self.move['Lp'] != 0:
            totalLeft+=1
        return totalLeft
    def EvaluateUp(self,up):
        if up != True and self.location == "hall":
            self.listMessage.append(tableRule["U0"])
        elif self.location != "hall" and up:
            self.listMessage.append(tableRule["U1"])

    def EvaluateDown(self,down):
        if down != True and self.location == "Threater":
            self.listMessage.append(tableRule["D0"])
        elif self.location != "Threater" and down:
            self.listMessage.append(tableRule["D1"])

    def EvaluateForward(self):
        if self.move["F"] == 0:
            self.listMessage.append(tableRule["F0"])
            return False
        else:
            return True
    def CheckMinAndMaxToEvaluate(self):
        self.calc()
        max, min, up, down = self.MaxMin()
        if max != min:
            if max != '':
                if self.move[max]!=0:
                    self.listMessage.append(tableRule[max + "m"])
            if min != '':
                if self.move[min]!=0:
                        self.listMessage.append(tableRule[min + "f"])
        return min,up,down
    def EvaluateMove(self):
        numOfMove = self.evaluate_body()
        if numOfMove == "more":
            self.listMessage.append(tableRule["M"])
        elif numOfMove == "less" and self.location != "small":
            self.listMessage.append(tableRule["ML"])

        return numOfMove

    def OutFromScrean(self):
        out=0
        if self.move['RError'] != 0:
            out+=1
            self.listMessage.append(tableRule["RError"])

        if self.move['LError'] != 0:
            out+1
            self.listMessage.append(tableRule["LError"])
        return out
    def AllDirection(self):
        if self.move['L']!=0 and self.move["R"]!=0 and self.move["F"]!=0:
            if self.location=="small" or self.location=="big":
                self.listMessage.append(tableRule["goodAllDirection"])
            return True
        elif self.move['L']==0 and self.move["R"]==0 and self.move["F"]==0:
            return False
        return "Ok"

    def result(self):
        if self.outofcamera!=0:
            self.listMessage.append("Regardless to getting out of camera boundaries your other mistakes are: ")
        AllDirect=self.AllDirection()
        forward=self.EvaluateForward()
        totalleft=self.EvaluateLeft()
        totalRight=self.EvaluateRight()
        min, up, down = self.CheckMinAndMaxToEvaluate()
        self.EvaluateUp(up)
        self.EvaluateDown(down)
        move=self.EvaluateMove()

        out=self.OutFromScrean()
        score=self.FinalScore(AllDirect,forward,totalRight,totalleft,up,down,min,move,out)

        return self.listMessage, score



