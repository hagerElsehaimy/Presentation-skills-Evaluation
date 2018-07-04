from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox



class menu:



   def letGoButton(self):
      pass

   def history(self):
      import history
      self.root.destroy()

      history.history(self.name)

   def donothing(self):
      pass

   def logout(self):
      self.root.destroy()
      import welcome_page
      welcome_page.welcome_frame()

   def About(self):
      self.root.destroy()
      import about
      about.about(self.name)

   def new(self):
      self.root.destroy()
      import selectOption
      selectOption.selectOption(self.name)

   def ask_quit(self):
      if messagebox.askokcancel("Exit", "You want to quit now?"):
         self.root.destroy()

   def exit(self):
      #print('User chosen: {}'.format(choice))
      if messagebox.askokcancel("Exit","Are you Sure , you want to Exit?"):
         self.root.destroy()

   def __init__(self,root,name):
      self.name=name
      self.root=root
      self.root.geometry("960x640+30+30")
      self.root.title("Evaluate Presentation Skills")
      self.root.iconbitmap(r'photo\5start-img.ico')

      menubar = Menu(root)
      filemenu = Menu(menubar, tearoff=0)

      filemenu = Menu(menubar, tearoff=0)
      filemenu.add_command(label="New", command=self.new)
      filemenu.add_command(label="History", command=self.history)



      filemenu.add_separator()

      filemenu.add_command(label="Logout", command=self.logout)

      #filemenu.add_command(label="Close", command=self.exit)
      menubar.add_cascade(label="User", menu=filemenu)

      helpmenu = Menu(menubar, tearoff=0)
      helpmenu.add_command(label="Help Index", command=self.donothing)
      helpmenu.add_command(label="Presentation Skills", command=self.donothing)
      helpmenu.add_separator()
      helpmenu.add_command(label="About ...  ", command=self.About)

      menubar.add_cascade(label="Help", menu=helpmenu)

      menubar.add_cascade(label="Exit",command=self.exit)
      root.config(menu=menubar)

      background = Label(root, bg="#132533")
      background.place(relx=0.1, rely=0.1, anchor=CENTER, width=2500, height=2000)
      self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)
      #root.mainloop()


#menu()