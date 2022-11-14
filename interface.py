from functions import *
from varuables import *
import tkinter as tk
from tkinter import *

root.title('Auto Clicker')
root.resizable(width=False, height=False)

canva.pack()
frame.place(relwidth=0.9, relheight=1, relx=0.05, rely=0.05)
title.pack()


StartButton = Button(frame, width=w, height=0, bg='darkorange', text='Start', foreground='yellow', 
font='Arial, 25', command=Start)
StopButton = Button(frame, width=w, height=0, bg='darkorange', text='Stop(Clamp X)', foreground='yellow', 
font='Arial, 25', command=Stop)

StartButton.place(relwidth=1, relx=0, rely=0.64)
StopButton.place(relwidth=1, relx=0, rely=0.79)

second.pack()
Button(frame, text="SET TIME",width=w,bg='darkorange', foreground='yellow',font='Arial 15',command=Delay).pack()


LeftClickButton.pack(pady=10)
LeftClickButton.select()

RightClickButton.pack()


root.mainloop()