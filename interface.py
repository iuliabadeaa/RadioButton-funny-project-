from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("First project")
root.geometry("200x200")
root.resizable(True,True)

def if_yes():
    root.destroy()

    window = Tk()
    window.title("First project")
    window.geometry("200x200")
    window.resizable(True,True)

    y=Label(window ,text='KNEW IT!') 
    y.place(x=50,y=70)
    y.config(font='bold,40')

    mainloop()


def if_no():
    root.destroy()
    img=Tk()

    frame = Frame(img)
    frame.pack()
    img = ImageTk.PhotoImage(Image.open("image.png"))
    label = Label(frame, image = img)
    label.pack()

    mainloop()


r=BooleanVar()


w=Label(root,text="U DUMB???🤓")
w.place(x=50,y=70)
w.configure(font='40')
yes_button=Radiobutton(root,text='yes', variable=r,value=1,command=if_yes).pack()
no_button=Radiobutton(root,text='no',variable=r,value=2,command=if_no).pack()


mainloop()