from tkinter import *
from menu import menu
from tkinter import messagebox


class SelectOptionVoice(menu):


   def letGoButton(self):

      SpeechDuration = self.durationInMinutes.get() * 60 + self.durationInSeconds.get()

      if SpeechDuration !="" and self.title.get()!="" and self.location!="":
          name = re.compile(r'^[a-zA-Z][a-zA-Z ]*$')
          if name.match(self.title.get()):
              self.root.destroy()
              from Files.datastore import datastore
              import Video
              datastore.name = self.enter
              datastore.title = self.title.get()
              Video.Video(self.location, SpeechDuration, self.title.get(), self.name)
          else:
              messagebox.showinfo("Error Message", "Please,You must Write Only English Letters")
      else:
         messagebox.showinfo("Error Message", "Please,You must Enter Video Title")




   def donothing(self):
      pass


   def on_leave(self,event):
       self.helpLabel.configure(text="",bg="#132533")

   def on_enter_duration(self, event):
       self.SpeechDuration = self.durationInMinutes.get() * 60 + self.durationInSeconds.get()
       self.ChangeDuration()

   def on_scale_minutes(self , val):
        minute = int(val)
        self.SpeechDuration = minute * 60 + self.durationInSeconds.get()
        self.ChangeDuration()

   def on_scale_seconds(self , val):
        second = int(val)
        self.SpeechDuration = (self.durationInMinutes.get() * 60) + second
        self.ChangeDuration()

   def ChangeDuration(self):
        if self.SpeechDuration == 0:
            self.helpLabel.configure(text="There is No Partial Speech Evaluation During Record")
        else:
            self.helpLabel.configure(
                text="A Partial Speech Evaluation will appear every " + str(self.SpeechDuration) + " Seconds")

   def __init__(self,location,enter):


      self.enter=enter
      self.location=location

      self.root = Tk()
      super(SelectOptionVoice, self).__init__(self.root,self.enter)

      speechTitle = StringVar()
      label = Label(textvariable=speechTitle, fg="#E2AF1E", bg="#132533", font=('Buxton Sketch', 18)).place(relx=0.17, rely=0.12,
                                                                                                    anchor=CENTER,
                                                                                                    width=300,
                                                                                                    height=36)
      speechTitle.set("To get Partial Speech Evaluation")
      HelpText = StringVar()
      label = Label(  textvariable=HelpText ,fg="#FFF",bg="#132533",font=('Buxton Sketch',18), justify = LEFT).place(relx=0.38, rely=0.22, anchor=CENTER,width=600 ,height=36)

      HelpText.set("Please, Select the Duration you prefer (in Minutes and Seconds) :")

      self.MinutesText = StringVar()
      self.MinutesText.set("Minutes Duration :")
      labelMinutesDuration = Label(textvariable=self.MinutesText, font=('Buxton Sketch', 18), fg="#E2AF1E",
                                   bg="#132533").place(relx=0.3, rely=0.33, anchor=CENTER, width=220, height=36)
      self.durationInMinutes = IntVar()
      self.MinutesDuration = Scale(self.root,
                                   tickinterval=2,
                                   width=20,
                                   length=300,
                                   activebackground="DodgerBlue",
                                   troughcolor="#E2AF1E",
                                   fg="coral",
                                   bg="#132533",
                                   highlightbackground="#132533",
                                   cursor="hand2",
                                   orient=HORIZONTAL,
                                   from_=0, to=10,
                                   variable=self.durationInMinutes,
                                    command = self.on_scale_minutes)
      self.MinutesDuration.place(relx=0.6, rely=0.33, anchor=CENTER)

      self.SecondsText = StringVar()
      self.SecondsText.set("Seconds Duration :")
      labelSecondsDuration = Label( textvariable=self.SecondsText ,font=('Buxton Sketch',18) ,fg="#E2AF1E",bg="#132533").place(relx=0.3, rely=0.45, anchor=CENTER,width=220 ,height=36)
      self.durationInSeconds = IntVar()
      self.SecondsDuration = Scale(self.root,
                            tickinterval=10,
                            width = 20,
                            length=300,
                            activebackground="DodgerBlue",
                            troughcolor="#E2AF1E",
                            fg="coral",
                            bg="#132533",
                            highlightbackground="#132533",
                            resolution = 5,
                            cursor="hand2",
                            orient=HORIZONTAL,
                            from_=0, to=60,
                            variable=self.durationInSeconds,
                            command=self.on_scale_seconds)
      self.SecondsDuration.place(relx=0.6, rely=0.45, anchor=CENTER)

      self.SecondsDuration.bind("<Enter>", self.on_enter_duration)
      self.SecondsDuration.bind("<Leave>", self.on_leave)
      self.MinutesDuration.bind("<Enter>", self.on_enter_duration)
      self.MinutesDuration.bind("<Leave>", self.on_leave)
      var = StringVar()
      label = Label(  textvariable=var, fg="#E2AF1E",bg="#132533",font=('Buxton Sketch',18)).place(relx=0.11, rely=0.6, anchor=CENTER,width=220 ,height=36)

      var.set("Video 's Title  :")
      self.title = StringVar()
      enter=Entry(textvariable=self.title).place(relx=0.45, rely=0.6, anchor=CENTER,width=300 ,height=30)

      note = StringVar()
      noteLabel = Label(textvariable=note, fg="#FFF", bg="#132533", font=('Buxton Sketch', 18) , justify = LEFT)
      note.set("** Note **\n Before recording Make Sure that you are in a quiet place away from any noise for Better Evaluation. ")
      noteLabel.place(relx=0.50, rely=0.75, anchor=CENTER, width=1000, height=60)

      self.helpLabel = Label(text="", fg="#FFF", bg="#132533", font=('Buxton Sketch', 18))
      self.helpLabel.place(relx=0.35, rely=0.9, anchor=CENTER, width=600, height=36)

      Go = Button( text ="Let's GO ...",bg="#273D52",fg="#FFF",font=('Buxton Sketch',22),command = self.letGoButton).place(relx=0.8, rely=0.9, anchor=CENTER,width=250 ,height=40)
      self.root.mainloop()



if __name__=='__main__':
    SelectOptionVoice("small","name")