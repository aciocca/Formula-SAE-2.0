import tkinter as tk 
import tkinter.ttk as ttk
import GUI.RealTime.Utils.helperTools as ht
from PIL import Image, ImageTk
import threading
rotation = 0
def createTextTab(notebook, master):
    virtualcockpitFrame = tk.Canvas(notebook, name = "virtualCockpit", background = "#fff")
    virtualcockpitFrame.pack(fill = "both", expand = True)
    ht.configureMultipleColumns(virtualcockpitFrame, 1)
    ht.configureMultipleRows(virtualcockpitFrame, 1)
    notebook.add(virtualcockpitFrame, text = "Text Mode", compound = tk.LEFT)
    return virtualcockpitFrame

def scaleImage(image, targetwidth, targetheight):
    width = image.size[0]
    height = image.size[1]
    newsize = [0,0]
    if (width>height):
        #Altezza piu` piccola della larghezza
        ratio = height / width # deve sempre essere <1
        newsize[0] = targetwidth
        newsize[1] = int(targetwidth * ratio) 
        return newsize
    elif(width < height):
        ratio = width / height
        newsize[0] = int(targetheight * ratio)
        newsize[1] = targetheight
        return newsize
    else:
        newsize[0] = targetheight
        newsize[1] = targetheight
        return newsize

def populateVCTab(virtualcockpitFrame, master, textvarframe):
    master.update_idletasks()
    framewidth = textvarframe.winfo_width()
    frameheight = textvarframe.winfo_height()
    drawHUD(virtualcockpitFrame, framewidth, frameheight)
    drawLancetta(virtualcockpitFrame, framewidth, frameheight)
    
def drawHUD(virtualcockpitFrame, framewidth, frameheight):
    virtualcockpitBackgroud = Image.open("res/background.png")
    newsize = scaleImage(virtualcockpitBackgroud, framewidth, frameheight)
    resized = virtualcockpitBackgroud.resize(newsize, Image.ANTIALIAS)
    virtualcockpitBackgroudTK = ImageTk.PhotoImage(resized)
    
    lab2 = tk.Label(virtualcockpitFrame, image = virtualcockpitBackgroudTK)
    lab2.image = virtualcockpitBackgroudTK    
    virtualcockpitFrame.create_image(framewidth/2,frameheight/2, image = virtualcockpitBackgroudTK)
    
def drawLancetta(virtualcockpitFrame, framewidth, frameheight):
    lancetta = Image.open("res/short_pointer2.png")
    lancettasize = scaleImage(lancetta, framewidth, frameheight)
    resizedlancetta = lancetta.resize(lancettasize, Image.ANTIALIAS)
    picture = ImageTk.PhotoImage(resizedlancetta)
    lab2 = tk.Label(virtualcockpitFrame, image = picture)
    lab2.image = picture
    
    dynamic = virtualcockpitFrame.create_image(framewidth/4,frameheight/2, image = picture)
    dyno = threading.Timer(0.001, rotateLancetta(virtualcockpitFrame, dynamic, resizedlancetta, framewidth, frameheight))
    dyno.daemon = True
    #dyno.start()
    

def rotateLancetta(virtualcockpitFrame, dynamic, resizedlancetta, framewidth, frameheight):
    virtualcockpitFrame.create_rectangle(framewidth/4, frameheight/2, framewidth/4 - 100,frameheight/2 - 10 , fill = "black", tags = "lancetta")
