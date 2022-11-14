import pyautogui, keyboard, time
from tkinter import *
from varuables import *

on_off = True
n = 0


def Stop():
    global on_off
    on_off = False
    


def Start():
    global on_off
    on_off = True

    if LeftClick.get() == 1 and RightClick.get() == 1:
        while on_off == True:
            pyautogui.click()
            pyautogui.rightClick()
            print('both ')
            time.sleep(seconds)
            if keyboard.is_pressed('x'):
                Stop() 

    elif LeftClick.get() == 1:
        while on_off == True:
            pyautogui.click()
            print('left ')
            time.sleep(seconds)
            if keyboard.is_pressed('x'):
                Stop()

    elif RightClick.get() == 1:
        while on_off == True:
            pyautogui.rightClick()
            print('right ')
            time.sleep(seconds)
            if keyboard.is_pressed('x'):
                Stop() 



def Delay():
    global seconds
    seconds = second.get()
    seconds = int(seconds)

