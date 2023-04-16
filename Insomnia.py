# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:55:18 2022

@author: Louise.Ward
"""
import time
import pyautogui
from threading import Thread 
import threading as th
import tkinter as tk

window_bg = "white"
window_fg = "black"
button_bg = "SystemButtonFace"
button_fg = "black"
LARGE_FONT= ("Verdana", 12)
NORM_FONT= ("Verdana", 10)
SMALL_FONT= ("Verdana", 8)

window = tk.Tk()
window.iconbitmap("C:/Users/Louise.Ward/Documents/3_Personal Developemnt/Python/mrBlinky.ico")

stop = 0

def StayAwake():
    global stop
    stop = 0
    thread2 = Thread(target=insomnia, args = (12,))
    thread2.start()
    call()

def SleepTime():
    global stop
    stop = 1
    thread2.join()

def tkWindow(arg):
    global counter
    window.title("Insomnia")
    
    frame = tk.Frame(
        master = window, 
        bg = window_bg
        )
    
    frame_b = tk.Frame(
        master = window, 
        bg = window_bg
        )
    
    greeting = tk.Label(
        master = frame, 
        text = "Welcome to Insomnia", 
        font = LARGE_FONT,
        bg = window_bg, 
        fg = window_fg
        )
    
    counter = tk.Label(
        master = frame,
        text = "unknown",
        bg = window_bg,
        fg = window_fg
        )
    
    button_awake_start = tk.Button(
        master = window,
        text="Stay Awake",
        bg = button_bg,
        fg = button_fg,
        width = 20,
        command = StayAwake
        )
    
    button_awake_stop = tk.Button(
        master = window,
        text = "Stop Keeping Awake",
        bg = button_bg,
        fg = button_fg,
        width = 20,
        command= SleepTime
        )
    
    frame.pack(
        side = tk.TOP,
        fill = tk.BOTH, 
        expand = True, 
        ipadx = 50,
        ipady = 1
        )
    
    greeting.pack()
    counter.pack()
    
    frame_b.pack(
        side = tk.BOTTOM,
        fill = tk.BOTH,
        expand = True,
        ipadx = 50,
        ipady=20)
    
    button_awake_start.pack(in_ = frame_b, side = tk.LEFT, anchor = 'e', expand = True)
    button_awake_stop.pack(in_ = frame_b, side = tk.LEFT, anchor = 'w', expand = True)
    call()

def call():
    global j
    global stop
    if stop == 0:
        counter.config(text=str(j))
        window.after(1000, call)
    else:
        counter.config(text=str(0))

def insomnia(arg):
    global j
    global counter
    j = 0
    pyautogui.FAILSAFE = False
    while True:
        if stop == 1:
            j = 0
            break

        time.sleep(1)

        for i in range(0, 3):
            pyautogui.press('shift')
        #print("boop levels: ", j)
        j = j + 1
    j = 0

if __name__ == "__main__":
    thread = Thread(target=tkWindow, args = (12,))
    thread.start()
    thread2 = Thread(target=insomnia, args = (12,))
    thread2.start()

window.mainloop()