from  tkinter import *

def addition():
    a=atul.get()
    atul.set(a+"+")
def equal():
    atul.set("equal")
def change():
    try:
        sum=eval(atul.get())
        atul.set(sum)
    except Exception as e:
        atul.set("ERROR")

def number():
    print("hlo")

frame1= Tk()


frame1.geometry("900x600")
atul=StringVar()

frame2=Frame(frame1)
frame2.pack(side=TOP,fill=X)
label1=Entry(frame2,textvariable=atul,font=("arial",40,"bold")).pack()
atul.set("")


frame3=Frame(frame1, borderwidth=8, relief=SUNKEN,pady=10)
frame3.pack(fill=X,pady=40)
button1=Button(frame3,text="addittion",borderwidth=3,relief=SUNKEN,padx=10,pady=5,command=lambda : atul.set(atul.get()+"+")).pack(side=LEFT,padx=10)
button2=Button(frame3,text="Subtraction",borderwidth=3,padx=5,pady=5,relief=SUNKEN,command=lambda : atul.set(atul.get()+"-")).pack(padx=20,side=LEFT)
button3=Button(frame3,text="Multiplication",borderwidth=3,padx=5,pady=5,relief=SUNKEN,command=lambda : atul.set(atul.get()+"*")).pack(padx=20,side=LEFT)
button4=Button(frame3,text="division",borderwidth=3,padx=5,pady=5,relief=SUNKEN,command=lambda : atul.set(atul.get()+"/")).pack(padx=20,side=LEFT)
button5=Button(frame3,text="Answer",borderwidth=3,padx=5,pady=5,relief=SUNKEN,command=change).pack(padx=20,side=BOTTOM)


frame3=Frame(frame1)
frame3.pack(fill=X,pady=4)
butt1=Button(frame3,text="7",borderwidth=1,relief=SUNKEN,padx=10,pady=5,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"7"))
butt1.pack(side=LEFT,padx=10)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))


butt1=Button(frame3,text="8",borderwidth=1,padx=15,pady=5,relief=SUNKEN,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"8"))
butt1.pack(padx=20,side=LEFT)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))

butt1=Button(frame3,text="9",borderwidth=1,padx=15,pady=5,relief=SUNKEN,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"9"))
butt1.pack(padx=20,side=LEFT)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))

#*********************************************    second
frame3=Frame(frame1)
frame3.pack(fill=X,pady=4)
butt1=Button(frame3,text="4",borderwidth=1,relief=SUNKEN,padx=10,pady=5,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"4"))
butt1.pack(side=LEFT,padx=10)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))


butt1=Button(frame3,text="5",borderwidth=1,padx=15,pady=5,relief=SUNKEN,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"5"))
butt1.pack(padx=20,side=LEFT)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))

butt1=Button(frame3,text="6",borderwidth=1,padx=15,pady=5,relief=SUNKEN,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"6"))
butt1.pack(padx=20,side=LEFT)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))





#***************************************    third

frame3=Frame(frame1)
frame3.pack(fill=X,pady=4)
butt1=Button(frame3,text="1",borderwidth=1,relief=SUNKEN,padx=10,pady=5,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"1"))
butt1.pack(side=LEFT,padx=10)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))


butt1=Button(frame3,text="2",borderwidth=1,padx=15,pady=5,relief=SUNKEN,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"2"))
butt1.pack(padx=20,side=LEFT)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))

butt1=Button(frame3,text="3",borderwidth=1,padx=15,pady=5,relief=SUNKEN,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"3"))
butt1.pack(padx=20,side=LEFT)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))


#***************************************** fourth
frame3=Frame(frame1)
frame3.pack(fill=X,pady=4)
butt1=Button(frame3,text=".",borderwidth=1,relief=SUNKEN,padx=10,pady=5,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"."))
butt1.pack(side=LEFT,padx=10)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))


butt1=Button(frame3,text="0",borderwidth=1,padx=15,pady=5,relief=SUNKEN,font=("arial",25,"bold"),
             command=lambda : atul.set(atul.get()+"0"))
butt1.pack(padx=20,side=LEFT)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))

butt1=Button(frame3,text="C",borderwidth=1,padx=15,pady=5,relief=SUNKEN,font=("arial",25,"bold"),
             command=lambda : atul.set(""))
butt1.pack(padx=20,side=LEFT)
butt1.bind("<Enter>", lambda event, h=butt1: h.configure(bg="red"))
butt1.bind("<Leave>", lambda event, h=butt1: h.configure(bg="white"))



frame1.mainloop()



