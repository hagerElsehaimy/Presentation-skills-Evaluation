from tkinter import *
import cv2
from PIL import Image, ImageTk
from IContact.IContact import IContact
from IContact.ForwardCamera import ForwardCamera
from threading import Thread
from menu import menu
#from IContact.binaryFile import file
import matplotlib
matplotlib.use('Agg')
import threading
from tkinter import messagebox
from Speech.Evaluate import Evaluate
import time


class Video():


    def EnableEvaluteButton(self):
        self.evaluate.configure(state="active")

    def record(self):

        if self.startRecordFlag == False:


            self.startRecordFlag=True



            self.Record.configure(bg="#e1ae21", fg="#fff")
            self.Record.configure(state="disabled")

            #self.thread._stop()

            self.lock.acquire()
            self.forward['text'] = "END"
            self.lock.release()

            self.notice['text'] = "Start Record"

            self.iContact=IContact(self.selectOption,self.cap,self.notice)
            self.thread2 = Thread(target=self.iContact.func, args=())
            self.thread2.start()

            # Speech Evaluate
            self.speech = Evaluate(self.voiceDuration, self.data)
            self.thread3 = Thread(target=self.speech.evaluateSpeechRealTime, args=(END,self.evaluate, ))
            self.thread3.start()

            """self.startTime = time.time()
            self.thread4 = Thread(target=self.EnableEvaluteButton, args=())
            self.thread4.start()"""

            #threading.Timer(5.0, self.EnableEvaluteButton).start()
        else:
            self.Record.configure(state="disabled")



    def evaluate(self):

        if  self.iContact!=None and self.speech != None:
           #try:
                speechEvaluate = self.speech.evaluateRecord()
                iContactEvaluate=self.iContact.Evaluate()

                cv2.destroyAllWindows()
                self.root.destroy()

                #cleanup_stop_thread()

                import evaluate
                self.speechEvaluate, self.scoreSpeech = speechEvaluate
                self.iContactEvaluate, self.scoreIContact = iContactEvaluate
                
                from Files.datastore import datastore
                datastore.icontant = self.iContactEvaluate
                datastore.score = (self.scoreSpeech + self.scoreIContact) / 2
                speechEvaluateData = str(self.speechEvaluate).replace('\n' , '-')
                output_file = open("../Files/esraa.txt", "ab")
                output_file.write(
                    str(self.name).encode() + "$".encode() + str(self.title).encode() + "$".encode() + str(
                        (self.scoreSpeech + self.scoreIContact) / 2).encode() + "$".encode() + str(self.iContactEvaluate).encode() + "$".encode() + str(speechEvaluateData).encode() + "\n".encode())
                output_file.close()
                output_file = open("../Files/esraa.txt", "r")

                evaluate.evaluate(iContactEvaluate,speechEvaluate,self.name)
                #evaluate.evaluate(iContactEvaluate, speechEvaluate)

           #except:
            #    messagebox.showinfo("Error Message", "Hey You didn't record anything to evaluate")
                """
                # Speech Evaluate
                self.speech = Evaluate(self.voiceDuration, self.data)
                self.thread3 = Thread(target=self.speech.evaluateSpeechRealTime, args=(END,))
                self.thread3.start()
                self.Record.configure(state="disable")
                """
                """
                self.Record.configure(bg="#e0ebeb", fg="#132533")
                self.Record.configure(state="active")"""

                ### Here Wanna to Stop Record and reagain it
        else:
            messagebox.showinfo("Help Message","Please,You must start record First")




    def EnableEvaluteButton(self):
        while True:
            diff= time.time()- self.startTime
            if diff>=5:
                self.evaluate.configure(state="active")
                break


    def __init__(self,selectOption,duration,title,name):

        self.root=Tk()
        self.startRecordFlag=False
        self.title=title
        self.name=name
        self.speech = None
        self.root.geometry("960x640+30+30")
        self.root.title("Evaluate Presentation Skills")
        self.root.iconbitmap(r'photo\5start-img.ico')
        self.voiceDuration = duration

        #super(Video, self).__init__(self.root,self.name)

        self.iContact = None
        self.selectOption=selectOption
        self.lock = threading.Lock()


        #mymenu=Menuclass.Menu(root)

        self.cap = cv2.VideoCapture(0)

        self.root.configure(background='#132533')
        self.bagroundVideo = Label(self.root,width=500, height=350,bg="#132533",borderwidth=3,relief="groove")
        self.bagroundVideo.place(relx=0.30, rely=0.39,anchor=CENTER)
        self.notice=Label(text="you must look forward to camera", bg="#132533", fg="#fff", font=('Buxton Sketch', 24))
        self.notice.place(relx=0.25, rely=0.05, anchor=CENTER)
        self.forward = Label(text="Forward", bg="#132533", fg="#fff", font=('Buxton Sketch', 24))
        self.forward.place(relx=0.30, rely=0.10, anchor=CENTER)
        imagepause = Image.open("photo\play-button.png")
        photo = ImageTk.PhotoImage(imagepause)
        self.Record = Button(text=' Record ', bg="#e0ebeb", fg="#132533", command=self.record,
                             font=('Buxton Sketch', 18), image=photo, compound="left")
        self.Record.place(relx=0.40, rely=0.82, anchor=CENTER, width=170, height=50)
        #self.Record.configure(text="loza")
        self.Record.configure(state="disabled")
        """imagepause = Image.open("photo\pause(1).png")
        photo2= ImageTk.PhotoImage(imagepause)
        pause=Button(text=' Pause', bg="#e0ebeb", fg="#132533", font=('Buxton Sketch', 18),image=photo2,compound="left")
        pause.place(relx=0.50, rely=0.82, anchor=CENTER,width=110, height=44)"""
        imagepause = Image.open("photo\stop.png")
        photo3= ImageTk.PhotoImage(imagepause)
        self.evaluate=Button(text=' Evaluate me ', bg="#273D52" , fg="#fff", font=('Buxton Sketch', 18)
                        ,image=photo3,compound="left",command=self.evaluate)
        self.evaluate.place(relx=0.65, rely=0.82, anchor=CENTER,width=200, height=50)
        self.evaluate.configure(state="disabled")
        evaluate=Label(text="Voice's report", bg="#132533" , fg="#fff", font=('Buxton Sketch', 24))
        evaluate.place(relx=0.76, rely=0.06, anchor=CENTER)

        images = Image.open("photo\star2.png")
        images = images.resize((50, 50), Image.ANTIALIAS)
        photo4 = ImageTk.PhotoImage(images)
        line = Label(self.root,bg="#132533",fg="#fff",image=photo4)
        line.place(relx=0.64, rely=0.06,anchor=CENTER)
        line2= Label(self.root,bg="#132533",fg="#fff",image=photo4)
        line2.place(relx=0.88, rely=0.06,anchor=CENTER)
        self.data = Text(bg="#e0ebeb", fg="#132533", font=('Buxton Sketch', 16), borderwidth=3, relief="solid")
        self.data.place(relx=0.76, rely=0.40, anchor=CENTER, width=350, height=350)
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)

        forwardCamera = ForwardCamera(self.forward,self.cap,self.Record)
        self.threadForward = Thread(target=forwardCamera.func, args=())
        self.threadForward.start()

        #self.Vedioappear()

        self.thread = Thread(target=self.Vedioappear, args=())
        self.thread.start()

        self.root.mainloop()

    def ask_quit(self):

        messagebox.showinfo("Error Message", "Sorry,Can't Exit This Window")
        """
        if messagebox.askokcancel("Exit", "You want to quit now?"):
            if self.startRecordFlag == False:
                
                print ("Forward")
                self.lock.acquire()
                self.forward['text'] = "END"
                self.lock.release()
                
                state = str(self.Record['state'])
                if state != 'disabled' :
                    print ("true")
                    self.cap.release()
                    self.thread._stop()
                    self.threadForward._stop()
                    cv2.destroyAllWindows()
                    self.root.destroy()
            else:
                self.iContact.Evaluate()
                cv2.destroyAllWindows()
                self.root.destroy()
        """






    def Vedioappear(self):
        _, frame =self.cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.bagroundVideo.imgtk = imgtk
        self.bagroundVideo.configure(image=imgtk)

        if self.root!=None:
            self.bagroundVideo.after(10,self.Vedioappear)


if __name__ == '__main__':
    Video("small",5,"loza","loza")
    pass


