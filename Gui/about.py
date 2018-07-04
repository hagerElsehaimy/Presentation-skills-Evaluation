from tkinter import *
from menu import menu
from PIL import Image, ImageTk

class about(menu):

    def __init__(self,name):
        self.root = Tk()
        super(about, self).__init__(self.root,name)
        width = 960
        height = 640
        self.root.geometry("960x640+30+30")
        self.root.title("Evaluate presentation skills")
        self.root.configure(background='#132533')
        Evaluate = Label(self.root, bg="#132533", fg="#fff", text="Presentasi", font=('Buxton Sketch', 40))
        Evaluate.place(relx=0.50, rely=0.10, anchor=CENTER)
        images = Image.open("photo\star.png")
        images = images.resize((160, 50), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(images)
        line = Label(self.root, bg="#132533", fg="#fff", image=photo)
        line.place(relx=0.50, rely=0.17, anchor=CENTER)
        titlePro = Label(self.root, bg="#132533",fg="#e1ae21",text="DEVELOPED BY :",font=('Buxton Sketch', 20))
        titlePro.place(relx=0.20, rely=0.30, anchor=CENTER)
        progrmer=Text( bg="#132533" , fg="#e0ebeb", font=('Bahnschrift SemiBold', 18), borderwidth=0)
        progrmer.place(relx=0.30, rely=0.53, anchor=CENTER,width=300, height=250)
        progrmer.insert(END,"Esraa MOHAMED\nSafaa EL-SHAFE’Y\nHager MOHAMED\nAml TAREK\nAsmaa MOSTAFA\nAya GAMAL")
        titleinstr = Label(self.root, bg="#132533", fg="#e1ae21", text="SUPERVISOR :", font=('Buxton Sketch', 20))
        titleinstr.place(relx=0.64, rely=0.30, anchor=CENTER)
        progrmer = Text(bg="#132533", fg="#e0ebeb", font=('Bahnschrift SemiBold', 18), borderwidth=0)
        progrmer.place(relx=0.75, rely=0.53, anchor=CENTER, width=300, height=250)
        progrmer.insert(END, "Dr. Marwa M.A. Elfattah")
        self.root.mainloop()


if __name__=='__main__':
    about("esraa")
