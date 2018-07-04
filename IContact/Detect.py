import math

class Detect():

    moveDic = {'L': 0, 'R': 0}

    @staticmethod
    def detectPosition(t_x):
        if (t_x < 100):
            return ['L','F','Lp','U','D']
        elif (t_x > 500):
            return ['R','F','Rp','U','D']
        else:
            return ['L','F','R','Rp','Lp','U','D']

    @staticmethod
    def compare(rectang,new):
        if (new[1-1].x) <rectang[0]:
            Nrectang=  Detect.locate_of_face_esraa(new)
            return "Right",Nrectang
        if  new[17-1].x>rectang[3]:
            Nrectang = Detect.locate_of_face_esraa(new)
            return "Left", Nrectang
        if new[20 - 1].y < rectang[1]:
            Nrectang = Detect.locate_of_face_esraa(new)
            return "up head", Nrectang
        if (new[9 - 1].y > rectang[2]):
            Nrectang = Detect.locate_of_face_esraa(new)
            return "down head", Nrectang
        return " ",rectang

    @staticmethod
    def detectDirection(new):


        direct=""

        #check up vs down
        xUp = new[31 - 1].x - new[30 - 1].x
        yUp = new[31 - 1].y - new[30 - 1].y

        up=math.sqrt(xUp ** 2 + yUp ** 2)

        xdown = new[34 - 1].x - new[31 - 1].x
        ydown = new[34 - 1].y - new[31 - 1].y

        down = math.sqrt(xdown ** 2 + ydown ** 2)


        if up>down:
            direct="D"


        elif down>up:
            diff=down-up
            if diff>up:
                direct = "U"


        #check left & right & forward

        xL = new[17-1].x - new[46-1].x
        yL = new[17-1].y - new[46-1].y

        xR = new[37-1].x - new[1-1].x
        yR= new[37-1].y - new[1-1].y

        left =math.sqrt(xL**2+yL**2)
        right = math.sqrt(xR**2 + yR**2)

        if left>right :
            if right<left/4:
                if direct!="":
                    return ["Rp",direct]
                else:
                    return ["Rp"]


            if right>left/4 and right<left/2:
                if direct!="":
                    return ["R",direct]
                else:
                    return ["R"]

        if right > left:
            if left<right/4:
                if direct!="":
                    return ["Lp",direct]
                else:
                    return ["Lp"]

            if left>right/4 and left<right/2:
                if direct!="":
                    return ["L",direct]
                else:
                    return ["L"]

        if left==right or right>left or left>right:
            if direct != "":
                return ["F", direct]
            else:
                return ["F"]
        else:
            if direct != "":
                return ["N", direct]
            else:
                return ["N"]





    def locate_of_face_esraa(face):
            x = face[1 - 1].x
            y = face[20- 1].y
            xw = face[17 - 1].x - face[1 - 1].x
            yh = face[17 - 1].y - face[1 - 1].y
            xR =face[20 - 1].x - face[9 - 1].x
            yR = face[20 - 1].y - face[9 - 1].y
            w = int(math.sqrt(xw ** 2 + yh ** 2))
            h = int(math.sqrt(xR ** 2 + yR ** 2))+10
            rx=x - int(0.5 * w)
            ry=y - int(0.5 * h)
            rw=x + w + int(0.5 * w)
            rh= y + h
            return [rx,ry,rh,rw]

    def timer(start, end):
        hours, rem = divmod(end - start, 3600)
        minutes, seconds = divmod(rem, 60)
        return ("{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))