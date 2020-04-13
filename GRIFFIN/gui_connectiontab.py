import tkinter as tk
import tkinter.ttk as ttk 
from tkinter.font import Font
class ConnectionTab:
    def __init__(self, notebook):
        # Qui uso self per non dover richiamare una funzione del root ogni volta
        self.connectionframe = tk.Frame(notebook, name = "connectionframe")
        self.connectionframe.grid(row = 0, column = 0, sticky = "nsew")
        self.connectionframe.columnconfigure(0, weight = 0, uniform = "small")
        self.connectionframe.columnconfigure(1, weight = 1, uniform = "big")
        self.connectionframe.columnconfigure(2, weight = 0, uniform = "small")
        self.connectionframe.columnconfigure(3, weight = 0, uniform = "small")
        self.connectionframe.columnconfigure(4, weight = 0, uniform = "small")
        self.connectionframe.columnconfigure(5, weight = 1, uniform = "big")
        self.connectionframe.columnconfigure(6, weight = 0, uniform = "small")
        self.connectionframe.rowconfigure(0, weight = 0, uniform = "small") # Spazio
        self.connectionframe.rowconfigure(1, weight = 1, uniform = "big") # Titoli
        self.connectionframe.rowconfigure(2, weight = 0, uniform = "small") # Spazio
        self.connectionframe.rowconfigure(3, weight = 1, uniform = "big") # Icone
        self.connectionframe.rowconfigure(4, weight = 0, uniform = "small") # Spazio
        self.connectionframe.rowconfigure(5, weight = 1, uniform = "big") # Menu a tenina
        self.connectionframe.rowconfigure(6, weight = 0, uniform = "small") # Spazio
        self.connectionframe.rowconfigure(7, weight = 0, uniform = "small") # Separatore
        self.connectionframe.rowconfigure(8, weight = 1, uniform = "big") # Opzioni Avanzate
        notebook.add(self.connectionframe, text = "Connection")
    
    def populate_connection_panel(self):
        titlefont = Font(size = 36)
        connectlabel = tk.Label(self.connectionframe, text = "Connect", font = titlefont)
        connectlabel.grid(column = 1, row = 1)
        disconnectlabel = tk.Label(self.connectionframe, text = "Disconnect", font = titlefont)
        disconnectlabel.grid(column = 5, row = 1)
        connectpicture = tk.PhotoImage(file = "res/serial.gif")
        connectbutton = tk.Button(self.connectionframe, image = connectpicture, state = "active", command = None)
        # Workaround per il garbage collector (3)
        connectbutton.image = connectpicture
        #connectbutton = tk.Button(self.connectionframe, image = connectpicture, state = "enabled", command = START_CONNECTION())
        connectbutton.grid(column = 1, row = 3)
        verticalseparator = ttk.Separator(self.connectionframe, orient = tk.VERTICAL)
        verticalseparator.grid(column = 3, row = 0, sticky = "ns", rowspan = 6)
        disconnectpicture = tk.PhotoImage(file = "res/serial.gif")
        disconnectbutton = tk.Button(self.connectionframe, image = disconnectpicture, state = "active", command = None)
        # Workaround per il garbage collector (3)
        disconnectbutton.image = disconnectpicture
        #connectbutton = tk.Button(self.connectionframe, image = connectpicture, state = "enabled", command = START_CONNECTION())
        disconnectbutton.grid(column = 5, row = 3)
        horizontalseparator = ttk.Separator(self.connectionframe, orient = tk.HORIZONTAL)
        horizontalseparator.grid(column = 0, row = 7, sticky = "ew", columnspan = 7)
        
        portselectframe = tk.Frame(self.connectionframe)
        portselectframe.grid(column = 1, row = 5)
        portCombobox = ttk.Combobox(portselectframe)
        portCombobox.grid(column = 0, row = 0, padx = 10)
        #portCombobox.bind("<<ComboboxSelected>>", self.updateSerialButton)
        refreshImage = tk.PhotoImage(file = "res/refresh_icon.gif")
        refreshButton = tk.Button(portselectframe, image = refreshImage, command = None)
        refreshButton.image = refreshImage
        refreshButton.grid(column = 1, row = 0)

    def populate_advanced_options_frame(self):
        advanced_options_frame = tk.Frame(self.connectionframe)
        advanced_options_frame.grid(column = 0, row = 8, columnspan = 7)

    def build_connectiontab(self):
        self.populate_connection_panel()
        self.populate_advanced_options_frame()
