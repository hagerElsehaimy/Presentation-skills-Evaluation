class AllState:

    dictonary={"R":0,"L":0,"U":0,"D":0,"F":0,"RError":0,"LError":0,"Rp":0,"Lp":0}

    """"
    dict like {1:[now state,[a valid State]]}
    """""

    @staticmethod
    def saveChange(dict):



        count=0
        keys=dict.keys() # all keys of dict
        keys=list(keys) #  because return tuple
        direction=[]



        for key in  keys:


            values = dict[key] # values of  key





            flagError=False

            for dir in values[0]:
                flag=False
                if dir=='R' or dir=='Rp' or dir == 'L' or dir=='Lp':
                    for x in values[1]:
                        if x==dir:
                            flag=True

                    if flag==False:

                        if dir=='R' or dir=='Rp':
                            AllState.dictonary["RError"] += 1

                        elif dir == 'L' or dir=='Lp':
                            AllState.dictonary["LError"] += 1

                        flagError=True



            if flagError==True:
                continue

            if "R" in values[0]:
                AllState.dictonary["R"]+=1

            if "L" in values[0]:
                AllState.dictonary["L"]+=1

            if "U" in values[0]:
                AllState.dictonary["U"]+=1
            if "D" in values[0]:
                AllState.dictonary["D"]+=1
            if "F" in values[0]:
                AllState.dictonary["F"]+=1

            if "Lp" in values[0]:
                AllState.dictonary["Lp"]+=1
            if "Rp" in values[0]:
                AllState.dictonary["Rp"]+=1

            count+=1

            values.clear()
        return  AllState.dictonary

    def Max(self,temp):
        count={}
        Data={}
        for key,value in temp():
            if value[0] in count:
                count[value[0]]+=1
            else:
                count[value[0]] = 0
                Data[value[0]]=[key,value[1]]
        return count

        max=-1
        direct=""

        for key,value in count.items:
            if value>max:
                direct=key
                max=value

        return Data[direct][0],Data[direct][1]




if __name__=="__main__":


    dict={1:[["F"],["L","U","F"]],2:[["L"],["R","U"]],3:[["F","D"],["L","D","F"]]}
    dics=AllState.saveChange(dict)


