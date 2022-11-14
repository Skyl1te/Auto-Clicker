from tkinter import *

root = Tk()
h = 450
w = 250*2
root.geometry(f"{w}x{h}")

RightClick = IntVar()  
LeftClick = IntVar()  


canva = Canvas(root, width=w, height=h, bg='orange')
frame = Frame(root, bg='orange')
title = Label(frame, text='Auto CLicker', bg='orange', font='Arial, 40', foreground='yellow')

second = Entry(frame, width=w, font='Arial, 20')
second.insert(END, 'Enter delay in second(clear this text)')


LeftClickButton = Checkbutton(frame, text = "Left click", 
                      variable = LeftClick,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = w)

RightClickButton = Checkbutton(frame, text = "Right click",
                      variable = RightClick,
                      onvalue = 1,
                      offvalue = 0,
                      height = 2,
                      width = w)