from tkinter import *
from PIL import Image, ImageTk
from menu import menu
from tkinter import messagebox


class selectOption(menu):


   def next(self):

      if self.v.get()!="":

        self.root.destroy()
        from Files.datastore import datastore

        datastore.name = self.enter
        import SelectOptionVoice
        SelectOptionVoice.SelectOptionVoice(self.v.get(),self.name)

      else:
         messagebox.showinfo("Error Message", "Please,You must choice Location")




   def on_leave(self,event):
       self.helpLabel.configure(text="",bg="#132533")

   def on_enter_small(self, event):
       self.helpLabel.configure(text="Room : you should look only right and left.")

   def on_enter_big(self, event):
       self.helpLabel.configure(text="Class Room : you should look only right , left and cover them all.")

   def on_enter_threater(self, event):
       self.helpLabel.configure(text="Threater : you should interact with all directions.")


   def on_enter_hall(self, event):
       self.helpLabel.configure(text="Hall : you should look at all directions except downside.")




   def __init__(self,enter):
      #print(enter)
      self.enter=enter
      self.root = Tk()
      super(selectOption, self).__init__(self.root,self.enter)


      var = StringVar()
      label = Label(  textvariable=var ,fg="#E2AF1E",bg="#132533",font=('Buxton Sketch',18)).place(relx=0.13, rely=0.1, anchor=CENTER,width=220 ,height=36)

      var.set("Select Location ,")

      label = Label(textvariable=var, fg="#FFF", bg="#132533", font=('Buxton Sketch', 18)).place(relx=0.2, rely=0.2,
                                                                                                    anchor=CENTER,
                                                                                                    width=220,
                                                                                                    height=36)

      var.set("where you 'll evaluate ?")
      self.v = StringVar()
      #self.v.set("small")
      image1 = Image.open("photo//threater.jpg")
      image1 = image1.resize((200, 150), Image.ANTIALIAS)
      photo1 = ImageTk.PhotoImage(image1)
      self.threater=Radiobutton(self.root,image=photo1, variable=self.v, value="Threater",indicatoron = 0)
      self.threater.place(relx=0.38, rely=0.38, anchor=CENTER)
      self.threater.bind("<Enter>", self.on_enter_threater)
      self.threater.bind("<Leave>", self.on_leave)
      image2 = Image.open("photo\hall.jpg")
      image2 = image2.resize((200, 150), Image.ANTIALIAS)
      photo2 = ImageTk.PhotoImage(image2)
      self.hall=Radiobutton(self.root,image=photo2, variable=self.v, value="hall",indicatoron = 0)
      self.hall.place(relx=0.74, rely=0.38, anchor=CENTER)
      self.hall.bind("<Enter>", self.on_enter_hall)
      self.hall.bind("<Leave>", self.on_leave)
      image3 = Image.open("photo\small.jpg")
      image3 = image3.resize((200, 150), Image.ANTIALIAS)
      photo3 = ImageTk.PhotoImage(image3)
      self.small=Radiobutton( self.root,image=photo3, variable=self.v, value="small",indicatoron = 0)
      self.small.place(relx=0.38, rely=0.65, anchor=CENTER)
      self.small.bind("<Enter>", self.on_enter_small)
      self.small.bind("<Leave>", self.on_leave)
      image4 = Image.open("photo//big.jpeg")
      image4 = image4.resize((200, 150), Image.ANTIALIAS)
      photo4 = ImageTk.PhotoImage(image4)
      self.big=Radiobutton( self.root,image=photo4, variable=self.v, value="big",indicatoron = 0)
      self.big.place(relx=0.74, rely=0.65, anchor=CENTER)
      self.big.bind("<Enter>", self.on_enter_big)
      self.big.bind("<Leave>", self.on_leave)
      self.helpLabel = Label(text="", fg="#FFF", bg="#132533", font=('Buxton Sketch', 18))
      self.helpLabel.place(relx=0.35, rely=0.9, anchor=CENTER, width=600,height=36)

      B = Button( text ="Next",bg="#273D52",fg="#FFF",font=('Buxton Sketch',22),command = self.next).place(relx=0.8, rely=0.9, anchor=CENTER,width=250 ,height=40)
      self.root.mainloop()


if __name__=='__main__':
    selectOption("name")