from tkinter  import *
from tkinter import font
from menu import menu
from PIL import Image, ImageTk

class history(menu):

    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),bd=5,width=650, height=400)

    def watch(self,id):

        list=self.mylist[id]
        list[3] = list[3].replace('"', '')
        list[3] = list[3].replace('[', '')
        list[3] = list[3].replace(']', '')
        list[3] = list[3].replace('\'', '')
        my=list[3].split(",")
        list[4] = list[4].replace("-" , '\n')
        self.root.destroy()
        import evaluate
        #print(list[4], "----" , self.name)
        evaluate.evaluate((my,float(list[2])),(list[4] , float(list[2])),  self.name)




    def createTable(self,idList,nameOfVideo,dateOfvideo):

        height = len(nameOfVideo)


        lst=[]






        for i in range(height):  # Rows

            lst.append(lambda j=i: self.watch(j))
            var = StringVar()

            name = Label(self.frame, textvariable=var, fg="#E2AF1E", font=('Buxton Sketch', 18)).grid(row=i, column=1)

            var.set(nameOfVideo[i])

            Label(self.frame, text="         ", fg="#E2AF1E", font=('Buxton Sketch', 18)).grid(
                row=i , column=2)

            var = StringVar()
            Label(self.frame, text="          ", fg="#E2AF1E", borderwidth=1,font=('Buxton Sketch', 18)).grid(
                row=i , column=3)
            Label(self.frame, text="          ", fg="#E2AF1E", font=('Buxton Sketch', 18)).grid(
                row=i , column=4)


            date = Label(self.frame, textvariable=var, fg="#E2AF1E", font=('Buxton Sketch', 18)).grid(row=i,column=5)

            var.set(dateOfvideo[i])

            Label(self.frame, text="          ", fg="#E2AF1E", font=('Buxton Sketch', 18)).grid(
                row=i, column=6)
            Label(self.frame, text="          ", fg="#E2AF1E", font=('Buxton Sketch', 18)).grid(
                row=i , column=7)
            Label(self.frame, text="          ", fg="#E2AF1E", font=('Buxton Sketch', 18)).grid(
                row=i , column=8)



        for col, Direction in enumerate(lst):

            watch = Button(self.frame, text="Watch", bg="#273D52", fg="#FFF", width=10, height=1,
                           font=('Buxton Sketch', 18),
                           command=Direction)
            watch.grid(row=col, column=9, sticky=W, pady=10)

    def __init__(self,name):
        self.name=name
        self.root=Tk()
        super(history, self).__init__(self.root,self.name)

        image = Image.open('photo\937ed160d941a13aeab31a9ffb4ef5ca.jpg')
        image = image.resize((100, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label=Label( image=photo,borderwidth=0, bg="#132533", state='normal').place(relx=0.8, rely=0.03)


        label=Label(image=photo ,borderwidth=0, bg="#132533", state='normal').place(relx=0.01, rely=0.03)


        var = StringVar()
        label = Label( textvariable=var, bg="#132533",fg="#FFF", font=('Georgia', 22)).place(
            relx=0.18, rely=0.15, anchor=CENTER, width=150, height=36)

        var.set("Name")

        var = StringVar()
        label = Label( textvariable=var, bg="#132533",fg="#FFF", font=('Georgia', 22)).place(
            relx=0.45, rely=0.15, anchor=CENTER,width=150, height=36)

        var.set("Score")


        idList=[]
        self.mylist=[]
        nameOfVideo = []
        dateOfVideo=[]

        output_file = open("../Files/esraa.txt", "r")
        for line in output_file.readlines():
            list=line.split("$")
            if self.name==list[0]:

                self.mylist.append(list)
                nameOfVideo.append(list[1])
                score="%.2f" % float(list[2])
                dateOfVideo.append(score)


        myframe = Frame( width=700, height=450, background="#FFF", bd=5)
        myframe.place(relx=0.1, rely=0.25)

        self.canvas = Canvas(myframe)
        self.frame = Frame(self.canvas)

        myscrollbar = Scrollbar(myframe, orient="vertical", command=self.canvas.yview)
        myscrollbar2=Scrollbar(myframe, orient="horizontal", command=self.canvas.xview)

        self.canvas.configure(yscrollcommand=myscrollbar.set)
        self.canvas.configure(yscrollcommand=myscrollbar2.set)

        myscrollbar.pack(side="right", fill="y")
        myscrollbar2.pack(side="bottom", fill="x")

        self.canvas.pack(side="left")

        self.canvas.create_window((0,10), window=self.frame, anchor='nw')

        self.frame.bind("<Configure>", self.myfunction)
        self.createTable(idList,nameOfVideo,dateOfVideo)
        self.root.mainloop()



if __name__ == '__main__':
    history("A")