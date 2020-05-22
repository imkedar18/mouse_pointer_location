import pyautogui, sys
from tkinter import *
from threading import Thread
def position_mouse():
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            button.config(text=str(positionStr))
            button.config(state=DISABLED)
    except KeyboardInterrupt:
        pass

def startThread():
  thread=Thread(target=position_mouse)
  thread.start()



window = Tk()
window.title(" ")
window.resizable(width=False,height=False)
window.geometry('200x50')
button=Button(window,text="Mouse Position",command=startThread, fg='black')
button.pack()
window.mainloop()