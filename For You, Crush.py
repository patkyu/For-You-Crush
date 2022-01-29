from tkinter import *
from tkinter import messagebox

r =Tk()
r.title('Message In a GUI')
r.geometry("200x200")
def msg():
    messagebox.showwarning("Happy Valentine's Day, Crush","Stop! You're under arrest for capturing my heart!")


but= Button(r,text="Secret Message",command=msg)
but.place(x=50,y=50)
r.mainloop()      