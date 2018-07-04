from tkinter import *
import cv2
from PIL import Image, ImageTk
from menu import menu
import time


class evaluate(menu):

    def WriteTotalscore(self):
        EvalauationScore = round((self.scoreSpeech + self.scoreIContact) / 2 , 2)
        EvalauationScore="%.2f" % EvalauationScore
        #print(self.scoreSpeech , self.scoreIContact , EvalauationScore)
        self.score['text']=str(EvalauationScore)+"%"



    def eyeContact(self):
        self.printResult.configure(state="normal")
        self.eye.configure(bg="#e0ebeb", fg="#132533")
        self.voice.configure(bg="#273D52", fg="#fff")
        self.printResult.delete(1.0, END)
        for line in self.iContactEvaluate:
            if line[0]!='R':
                line = " - " + line
            self.printResult.insert(END, line)
            self.printResult.insert(END, "\n")



        self.printResult.configure(state="disabled")

    def speechEvaluation(self):
        self.printResult.configure(state="normal")
        self.voice.configure(bg="#e0ebeb", fg="#132533")
        # self.body.configure(bg="#273D52" , fg="#fff")
        self.eye.configure(bg="#273D52", fg="#fff")
        self.printResult.delete(1.0, END)
        self.printResult.insert(END, self.speechEvaluate)
        self.printResult.configure(state="disabled")

    def defaultDisplayEvalautioIsEyeContact(self):
        self.eyeContact()

    def __init__(self,iContactEvaluate, speechEvaluate,name):

        self.root=Tk()
        self.name = name
        super(evaluate, self).__init__(self.root,self.name)
        self.speechEvaluate , self.scoreSpeech = speechEvaluate
        self.iContactEvaluate,self.scoreIContact=iContactEvaluate
        width=960
        height=640
        self.root.geometry("960x640+30+30")
        self.root.title("Evaluate presentation skills")
        self.root.configure(background='#132533')
        Evaluate = Label(self.root,bg="#132533",fg="#fff",text="Your Evaluate",font=('Buxton Sketch', 40))
        Evaluate.place(relx=0.50, rely=0.10,anchor=CENTER)
        images = Image.open("photo\star.png")
        images = images.resize((160, 50), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(images)
        line = Label(self.root,bg="#132533",fg="#fff",image=photo)
        line.place(relx=0.50, rely=0.17,anchor=CENTER)
        self.score=Label( bg="#132533" , fg="#e1ae21",text="100%", font=('Roboto', 20))
        self.score.place(relx=0.72, rely=0.30, anchor=CENTER,width=300, height=50)
        value=Label( bg="#132533" , fg="#fff",text="Evaluate your presentation skills :", font=('Roboto', 20))
        value.place(relx=0.45, rely=0.30, anchor=CENTER)
        self.eye = Button(text=' I-contact ', bg="#e0ebeb", fg="#132533", font=('Buxton Sketch', 18),command=self.eyeContact)
        self.eye.place(relx=0.37, rely=0.85, anchor=CENTER,width=130, height=50)
        """self.body=Button(text=' Body Language', bg="#e0ebeb", fg="#132533", font=('Buxton Sketch', 18))
        self.body.place(relx=0.50, rely=0.85, anchor=CENTER,width=200, height=50)"""
        self.voice=Button(text=' Speech ', bg="#273D52" , fg="#fff", font=('Buxton Sketch', 18) , command=self.speechEvaluation)
        self.voice.place(relx=0.60, rely=0.85, anchor=CENTER,width=141, height=50)
        self.printResult=Text( bg="#e0ebeb" , fg="#132533", font=('Buxton Sketch', 18), borderwidth=5 ,relief="sunken")
        #self.printResult.configure(state="disabled")
        scrollbar = Scrollbar(self.printResult,command=self.printResult.yview ,width=10)

        scrollbar.pack( side = RIGHT, fill = Y )
        self.printResult['yscrollcommand'] = scrollbar.set
        self.WriteTotalscore()
        #self.printResult.insert(END,"hello")
        self.printResult.place(relx=0.50, rely=0.55, anchor=CENTER,width=500, height=250 )
        self.defaultDisplayEvalautioIsEyeContact()
        #self.printResult.configure(bg="Lightgray", fg="#000")
        try:
            self.root.mainloop()
        except:
            print("error")


if __name__=='__main__':
    li=["safaa husin shafe'y ali ali saed i love loza esraa mohammed Amal tarek","loza","safaa","loza","safaa","loza","safaa","loza","safaa","loza","safaa","loza","safaa","loza","safaa","loza","safaa","loza","safaa","loza"]
    evaluate((li,90.0001111111111111110000000000000005),("safaa",12),"name")