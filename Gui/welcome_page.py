import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import string
import re


class welcome_frame():

    def ask_quit(self):
        if messagebox.askokcancel("Exit", "You want to quit now?"):
            self.root.destroy()


    def startButton(self):

        if self.v.get()=="":
            messagebox.showinfo("Error Message", "Please,You must Write your name")
        else:
            name = re.compile(r'^[a-zA-Z][a-zA-Z ]*$')
            if name.match(self.v.get()):

                self.root.destroy()
                import selectOption
                selectOption.selectOption(self.v.get())
            else:
                messagebox.showinfo("Error Message", "Please,You must Write Only English Letters")

    def __init__(self):
        root = tk.Tk()
        self.width=960
        self.height=640
        self.root = root
        self.root.iconbitmap(r'photo\5start-img.ico')
        self.root.geometry("960x640+30+30")
        self.root.title("Evaluate Presentation Skills")
        image = Image.open("photo\home2.png")
        photo = ImageTk.PhotoImage(image)
        background=tk.Label(self.root,image=photo)
        background.pack()
        self.v = tk.StringVar()
        self.enter=tk.Entry(self.root,textvariable=self.v).place(relx=0.52, rely=0.60, anchor=tk.CENTER,width=220 ,height=36)
        bb=tk.Button(text='Start',command=self.startButton,bg="#e1ae21",fg="#000",font=('Buxton Sketch',22)).place(relx=0.50, rely=0.72, anchor=tk.CENTER,width=110 ,height=44)
        self.root.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.root.mainloop()


if __name__ == '__main__':
    frame=welcome_frame()
