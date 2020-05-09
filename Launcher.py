# TODO
# Info utili: http://stupidpythonideas.blogspot.com/2013/12/tkinter-validation.html
# Buone pratiche: https://www.begueradj.com/tkinter-best-practices/
# Creare un programma per arduino per il test del seriale
#
# TODO Launcher:
# Spezzare il launcher in più classi
# Togliere dimensioni hardcoded dai pannelli delle opzioni avanzate
#
# TODO RealTimeMode:
# Aggiungere var con media velocità ruote anteriori
# Aggiungere tab con la possibilità di selezionare un sensore e ottenere tutte le info su di esso
# Aggiungere possibilità di passare a post gara dalla modalità real time
#??? Possibilità di regolare la velocità di aggiornamento
#
# TODO Settings:
# Eliminare ridondanza sulla gestione dei valori di default in caso di mancata specifica
import GUI.Launcher.settings as settings
import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog
from tkinter import ttk
from os.path import basename
import GUI.RealTime.SerialHandler as sh
import subprocess
import GUI.RealTime.Utils.helperTools as ht
import GUI.globalstuff as globalstuff

class Application(tk.Frame):
    #########
    # SETUP #
    #########
    def __init__(self, master = None):
        self.master = master
        tk.Frame.__init__(self, master)
        self.grid()
        self.configureGUI()
        self.createWidgets()

    def onclose(self):
        self.master.destroy()
        
    def configureGUI(self):
        self.master.title("Formula SAE UniPG 2020")
        self.master.geometry("800x600")
        self.master.protocol("WM_DELETE_WINDOW", self.onclose)
        self.master.resizable(False, False)
        # Idealmente useremmo l'attributo unifom = "groupname" per i pannelli di dx e sx
        # ma avendo un separator in mezzo non facente parte del gruppo
        # i calcoli delle dimensioni ritornano sbagliati, dando una UI non bilanciata
        # Senza separator viene perfettamente bilanciato
        ht.configureMultipleColumns(self.master, 3)
        self.master.rowconfigure(0, weight = 1)
    

    ###########################
    # Aggiornamento attributi #
    ###########################

    def updateSettings(self):
        self.mysettings = settings.settings("temp")
        self.updatePort()
        if(self.advoptBool.get() == 1):
            self.updateBaudrate()
            self.updateBytes()
            self.updateLength()
            self.updateParity()
            self.updateStopbit()
            self.updateTimeout()
        self.mysettings.saveSettings()

    def updatePort(self): 
        self.mysettings.setportname(self.portCombobox.get())

    def updateBaudrate(self):
        if(self.baudrateEntry.get() is not ""):
            self.mysettings.setbaudrate(int(self.baudrateEntry.get()))

    def updateStopbit(self):
        if(self.sbEntry.get() is not ""):
           self.mysettings.setstopbit(int(self.sbEntry.get()))

    def updateParity(self):
        if(self.parityEntry.get() is not ""):
            self.mysettings.setparity(self.parityEntry.get())

    def updateLength(self):
        if(self.lengthEntry.get() is not ""):
            self.mysettings.setpacketlength(int(self.lengthEntry.get()))

    def updateTimeout(self):
        if(self.timeoutEntry.get() is not ""):
            self.mysettings.setupdatetimeout(int(self.timeoutEntry.get()))
    
    def updateBytes(self):
        if(self.bytesEntry.get() is not ""):
            self.mysettings.setbytestoread(int(self.bytesEntry.get()))

    ####################
    # Logica della GUI #
    ####################
    
    def updateSerialButton(self, event):
        self.serialButton.config(state = "normal")

    def updatePgButton(self, *args):
        self.pgButton.config(state = "normal")

    def refreshPorts(self):
        portList = sh.SerialHandler.scanCOMs()
        self.portCombobox.config(values = portList)
        return portList


    # I due metodi sono diversi perchè uno [updateSerialButton()] sfrutta l'esistenza del <<VirtualEvent>> legato al
    # combobox, l'altro [updatePgButton()] invece si appoggia al .trace() di una StringVar(), che gli passa altri
    # argomenti di cui però non abbiamo bisogno
    def openSerialMode(self):
        self.updateSettings()
        subprocess.Popen("python RealTimeMode.py")
        self.master.destroy()

    def checkAdvancedOptions(self):
        if (self.advoptBool.get() == 1):
            for e in self.serialOpFrame.winfo_children():
                e.config(state = "normal")
        else:
            #self.mysettings.resetDefaults()
            for e in self.serialOpFrame.winfo_children():
                e.config(state = "disabled")
                self.advoptLabel.config(state = "normal")
                self.advoptCheck.config(state = "normal")

    def pgcheckAdvancedOptions(self):
        if (self.pgadvoptBool.get() == 1):
            for e in self.pgOpFrame.winfo_children():
                e.config(state = "normal")
        else:
            for e in self.pgOpFrame.winfo_children():
                e.config(state = "disabled")
                self.pgadvoptLabel.config(state = "normal")
                self.pgadvoptCheck.config(state = "normal")

    def browseFile(self):
        self.path = filedialog.askopenfilename(initialdir = "/",title = "Select .csv file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        self.filename = tk.StringVar()
        self.filename.trace("w", callback = self.updatePgButton)
        self.filename.set(basename(self.path))
        self.pathLabel.config(text = self.filename.get())
        return self.path

    ###############
    # GUI Widgets #
    ###############

    def createLeftFrame(self):
        # Mi serve per avere info sulle dimensioni correnti della finestra
        # forza l'applicazione a calcolare ora le dimensioni della finestra
        # e dei widget fino ad ora messi sulla grid
        root.update_idletasks()
        self.leftFrame = tk.Frame(self.master, width = (root.winfo_width() / 2))
        self.leftFrame.grid(column = 0, row = 0, sticky = "nsew")
        self.leftFrame.grid_propagate(0)
        ht.configureMultipleColumns(self.leftFrame, 3, uniform = "a")
        ht.configureMultipleRows(self.leftFrame, 3)

    def createSerialOptionsFrame(self):
        self.serialOpFrame = tk.Frame(self.leftFrame, height = 150)
        self.serialOpFrame.grid_propagate(0) 
        self.serialOpFrame.grid(column = 0, row = 3, columnspan =3, sticky = "nsew")
        ht.configureMultipleColumns(self.serialOpFrame, 4, uniform="c")
        ht.configureMultipleRows(self.serialOpFrame, 3)

    def createmainSeparator(self):
        sep = ttk.Separator(self.master, orient = tk.VERTICAL)
        sep.grid(column = 1, row = 0, sticky = "nsew")

    def createRightFrame(self):
        # Mi serve per avere info sulle dimensioni correnti della finestra
        # forza l'applicazione a calcolare ora le dimensioni della finestra
        # e dei widget fino ad ora messi sulla grid
        root.update_idletasks()
        self.rightFrame = tk.Frame(self.master, width = (root.winfo_width() / 2))
        # La colonna 1 è riservata al separatore
        self.rightFrame.grid(column = 2, row = 0, sticky = "nsew")
        self.rightFrame.grid_propagate(0)
        ht.configureMultipleColumns(self.rightFrame, 3)
        ht.configureMultipleRows(self.rightFrame, 3)
            
    def createPostRaceModeOptionsFrame(self):
        self.pgOpFrame = tk.Frame(self.rightFrame, height = 150)
        self.pgOpFrame.grid_propagate(0) 
        self.pgOpFrame.grid(column = 0, row = 3, columnspan =3, sticky = "nsew")
        ht.configureMultipleColumns(self.pgOpFrame, 3)
        ht.configureMultipleRows(self.pgOpFrame, 2)
    
    def createSerialMode(self):
        modeFont = Font(size = 36)
        serialLab = tk.Label(self.leftFrame, anchor = tk.S, text = "Serial", font = modeFont)
        serialLab.grid(row = 0, column = 0, columnspan = 3)

        serialPicture = tk.PhotoImage(file = "res/serial.gif")
        self.serialButton = tk.Button(self.leftFrame, image = serialPicture, state = "disabled", command = self.openSerialMode)
        if (globalstuff.mode == "test"):
            self.serialButton.config(state = "normal")
        self.serialButton.image = serialPicture
        self.serialButton.grid(row = 1, column = 1)
        
        portLabel = tk.Label(self.leftFrame, text = "Choose Port")
        portLabel.grid(row = 2, column = 0)

        refreshImage = tk.PhotoImage(file = "res/refresh_icon.gif")
        refreshButton = tk.Button(self.leftFrame, image = refreshImage, command = self.refreshPorts)
        refreshButton.image = refreshImage
        refreshButton.grid(row = 2, column = 1, sticky = tk.E)
        
        self.portCombobox = ttk.Combobox(self.leftFrame)
        self.portCombobox.grid(row = 2, column = 2, padx = 10)
        self.portCombobox.bind("<<ComboboxSelected>>", self.updateSerialButton)

        if (len(self.refreshPorts()) > 0):
            self.portCombobox.current(0)
            self.serialButton.config(state = "normal")

    def createSerialOptions(self):
        self.advoptBool = tk.IntVar()
        self.advoptLabel = tk.Label(self.serialOpFrame, text = "Advanced options?")
        self.advoptLabel.grid(row = 0, column = 0, sticky = tk.N, columnspan = 2)
        self.advoptCheck = tk.Checkbutton(self.serialOpFrame, command = self.checkAdvancedOptions, variable= self.advoptBool)
        self.advoptCheck.grid(row = 0, column = 3, sticky = tk.N)
       
        baudrateLabel = tk.Label(self.serialOpFrame, text = "Baud Rate", state = "disabled")
        baudrateLabel.grid(row = 1, column = 0)
        self.baudrateEntry = tk.Entry(self.serialOpFrame, state = "disabled")
        self.baudrateEntry.grid(row = 1, column = 1, padx = 10)

        sbLabel = tk.Label(self.serialOpFrame, text = "Stop Bit", state = "disabled")
        sbLabel.grid(row = 2, column = 0)
        self.sbEntry = tk.Entry(self.serialOpFrame, state = "disabled")
        self.sbEntry.grid(row = 2, column = 1, padx = 10)

        parityLabel = tk.Label(self.serialOpFrame, text = "Parity", state = "disabled")
        parityLabel.grid(row = 3, column = 0)
        self.parityEntry = tk.Entry(self.serialOpFrame, state = "disabled")
        self.parityEntry.grid(row = 3, column = 1, padx = 10, pady = 5)

        lengthLabel = tk.Label(self.serialOpFrame, text = "Length", state = "disabled")
        lengthLabel.grid(row = 1, column = 2)
        self.lengthEntry = tk.Entry(self.serialOpFrame, state = "disabled")
        self.lengthEntry.grid(row = 1, column = 3, padx = 10)

        timeoutLabel = tk.Label(self.serialOpFrame, text = "Timeout", state = "disabled")
        timeoutLabel.grid(row = 2, column = 2)
        self.timeoutEntry = tk.Entry(self.serialOpFrame, state = "disabled")
        self.timeoutEntry.grid(row = 2, column = 3, padx = 10)

        bytesLabel = tk.Label(self.serialOpFrame, text = "Bytes to Read", state = "disabled")
        bytesLabel.grid(row = 3, column = 2)
        self.bytesEntry = tk.Entry(self.serialOpFrame, state = "disabled")
        self.bytesEntry.grid(row = 3, column = 3, padx = 10, pady = 5)

    def createPostRaceMode(self):
        modeFont = Font(size = 36)
        pgLab = tk.Label(self.rightFrame, anchor = tk.S, text = "Post Gara", font = modeFont)
        pgLab.grid(row = 0, column = 0, columnspan = 3)
        pgPicture = tk.PhotoImage(file = "res/postgara.gif")
        self.pgButton = tk.Button(self.rightFrame, image = pgPicture, state = "disabled")
        self.pgButton.image = pgPicture
        self.pgButton.grid(row = 1, column = 1)

        selfilLabel = tk.Label(self.rightFrame, text = "Select a .csv")
        selfilLabel.grid(column = 0, row = 2)
        selfilLabel.bind("")
        self.pathLabel = tk.Label(self.rightFrame, wraplength = 200)
        self.pathLabel.grid(column = 1, row = 2)
        selfilButton = tk.Button(self.rightFrame, text = "Browse", command = self.browseFile)
        selfilButton.grid(column = 2, row = 2)

    def createPostRaceModeOptions(self):    
        self.pgadvoptBool = tk.IntVar()
        self.pgadvoptLabel = tk.Label(self.pgOpFrame, text = "Advanced options?")
        self.pgadvoptLabel.grid(row = 0, column = 0, pady = 5, sticky = tk.N)
        self.pgadvoptCheck = tk.Checkbutton(self.pgOpFrame, command = self.pgcheckAdvancedOptions, variable= self.pgadvoptBool)
        self.pgadvoptCheck.grid(row = 0, column = 1, pady = 5, sticky = tk.N)
               
        pgseparatorLabel = tk.Label(self.pgOpFrame, text = "Separator", state = "disabled")
        pgseparatorLabel.grid(row = 1, column = 0, sticky = tk.N)
        pgseparatorEntry = tk.Entry(self.pgOpFrame, state = "disabled")
        pgseparatorEntry.grid(row = 1, column = 1, sticky = tk.N)


    def createWidgets(self):
        self.createLeftFrame()
        self.createmainSeparator()
        self.createRightFrame()      

        self.createSerialMode()
        self.createSerialOptionsFrame()
        self.createSerialOptions()

        self.createPostRaceMode()
        self.createPostRaceModeOptionsFrame()
        self.createPostRaceModeOptions()
        
root = ""
app = ""
def main():
    global root
    global app
    root = tk.Tk()
    root.iconbitmap("res/icon.ico")
    app = Application()
    root.mainloop()

if __name__ == "__main__":
    main()
