import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

isRunning = True
clicking = False
mouse = Controller()

def startClicker():
    global clicking
    clicking = True
    
def stopClicker():
    global clicking
    clicking = False
def autoClickerThreadHandler():
    while isRunning:
        if clicking == True:
            runAutoClicker()
    
def runAutoClicker():
    while clicking == True:
        mouse.click(Button.right)
        time.sleep(1)

autoClickerThread = threading.Thread(target=autoClickerThreadHandler)
autoClickerThread.start()
try:
    while isRunning:
        continue
except KeyboardInterrupt:
    isRunning = False
    stopClicker() 
        
autoClickerThread.join() # waits for autoClickThread to finish















    