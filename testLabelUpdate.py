import tkinter as tk
import GUI.RealTime.SerialHandler as SerialHandler

class Application(tk.Frame):
    def __init__(self, master=None):
        self.serialConnection = serialManager()
        self.master = master
        tk.Frame.__init__(self, master)
        self.master.rowconfigure(0)
        self.master.columnconfigure(0)
        self.master.grid()
        self.createLabel()
        self.varUpdater()
        
    def createLabel(self):
        self.tkCurrent = tk.StringVar()
        self.tkindex = tk.IntVar()
        self.tkindex.set(0)
        textLabel = tk.Label(self.master, text = "Current Bit: ")
        varLabel = tk.Label(self.master, textvar = self.tkCurrent)
        indexLabel = tk.Label(self.master, textvar = self.tkindex)
        textLabel.pack()
        varLabel.pack()
        indexLabel.pack()
        
    def varUpdater(self):
        self.tkindex.set(self.tkindex.get() + 1)
        self.tkCurrent.set(self.serialConnection.readData())
        self.master.after(100, self.varUpdater)

def main():
    root = tk.Tk()
    Application()
    root.mainloop()

def serialManager():
    serialConnection = SerialHandler.SerialHandler("COM12", 115200)
    serialConnection.openPort()
    return serialConnection

if __name__ == "__main__":
    main()