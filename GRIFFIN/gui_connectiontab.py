import tkinter as tk
import tkinter.ttk as ttk 
from tkinter.font import Font
# Questo serve a far funzionare tutte quelle funzioni che hanno argomenti ma devono essere legate ad un command di un widget
from functools import partial
class ConnectionTab:
    def __init__(self, notebook, logic_manager):
        self.logic_manager = logic_manager
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

    def start_connection_helper(self):
        # Classe di appoggio per il bottone di inizio collegamento, volevo fare tutto su gui_logic ma avere una funzione di appoggio qui
        # semplifica notevolmente le cose
        connection_parameters = {"portname": self.portCombobox.get(), "baudrate": self.baudrateEntry.get(), "bytestoread": self.bytesEntry.get(),
                                 "length": self.lengthEntry.get(), "parity": self.parityEntry.get(), "stopbit": self.sbEntry.get(), "timeout": self.timeoutEntry.get()}
        self.logic_manager.start_serial_connection(connection_parameters, self.connectbutton, self.disconnectbutton)

    def populate_connection_panel(self):
        titlefont = Font(size = 36)
        connectlabel = tk.Label(self.connectionframe, text = "Connect", font = titlefont)
        connectlabel.grid(column = 1, row = 1)
        disconnectlabel = tk.Label(self.connectionframe, text = "Disconnect", font = titlefont)
        disconnectlabel.grid(column = 5, row = 1)
        connectpicture = tk.PhotoImage(file = "res/serial.gif")
        self.connectbutton = tk.Button(self.connectionframe, image = connectpicture, state = "disabled", command = self.start_connection_helper)
        # Workaround per il garbage collector (3)
        self.connectbutton.image = connectpicture
        self.connectbutton.grid(column = 1, row = 3)
        verticalseparator = ttk.Separator(self.connectionframe, orient = tk.VERTICAL)
        verticalseparator.grid(column = 3, row = 0, sticky = "ns", rowspan = 6)
        disconnectpicture = tk.PhotoImage(file = "res/serial.gif")
        self.disconnectbutton = tk.Button(self.connectionframe, image = disconnectpicture, state = "disabled")
        # Su due linee perchè così posso passare se stesso come argomento
        self.disconnectbutton.config(command = partial(self.logic_manager.stop_serial_connection, self.connectbutton, self.disconnectbutton))
        # Workaround per il garbage collector (3)
        self.disconnectbutton.image = disconnectpicture
        self.disconnectbutton.grid(column = 5, row = 3)
        horizontalseparator = ttk.Separator(self.connectionframe, orient = tk.HORIZONTAL)
        horizontalseparator.grid(column = 0, row = 7, sticky = "ew", columnspan = 7)
        
        portselectframe = tk.Frame(self.connectionframe)
        portselectframe.grid(column = 1, row = 5)
        self.portCombobox = ttk.Combobox(portselectframe)
        self.portCombobox.grid(column = 0, row = 0, padx = 10)
        self.portCombobox.bind("<<ComboboxSelected>>", partial(self.logic_manager.port_selected, self.connectbutton))
        refreshImage = tk.PhotoImage(file = "res/refresh_icon.gif")
        refreshButton = tk.Button(portselectframe, image = refreshImage, command = partial(self.logic_manager.check_ports, self.portCombobox))
        refreshButton.image = refreshImage
        refreshButton.grid(column = 1, row = 0)

    def populate_advanced_options_frame(self):
        advanced_options_frame = tk.Frame(self.connectionframe, name = "advanced_options_frame")
        advanced_options_frame.grid(column = 0, row = 8, columnspan = 7)
        advanced_options_frame.columnconfigure(0, weight = 1, uniform = "names")
        advanced_options_frame.columnconfigure(1, weight = 1, uniform = "values")
        advanced_options_frame.columnconfigure(2, weight = 1, uniform = "names")
        advanced_options_frame.columnconfigure(3, weight = 1, uniform = "values")
        advanced_options_frame.columnconfigure(4, weight = 1, uniform = "names")
        advanced_options_frame.columnconfigure(5, weight = 1, uniform = "values")
        advanced_options_frame.rowconfigure(0, weight = 0, uniform = "checkbox")
        advanced_options_frame.rowconfigure(1, weight = 1, uniform = "options")
        advanced_options_frame.rowconfigure(2, weight = 1, uniform = "options")

        self.advoptBool = tk.BooleanVar()
        advoptLabel = tk.Label(advanced_options_frame, text = "Advanced options?", name = "advoptLabel")
        advoptLabel.grid(row = 0, column = 0, sticky = tk.W, columnspan = 2)
        advoptCheck = tk.Checkbutton(advanced_options_frame, variable= self.advoptBool, name = "advoptCheck")
        # Su due linee perchè così posso passare lo stesso oggetto come argomento della funzione che chiamo
        advoptCheck.config(command = partial(self.logic_manager.toggle_advanced_options, advoptCheck, self.advoptBool, checkbox_label = advoptLabel))
        advoptCheck.grid(row = 0, column = 1, sticky = tk.N)
       
        baudrateLabel = tk.Label(advanced_options_frame, text = "Baud Rate", state = "disabled")
        baudrateLabel.grid(row = 1, column = 0)
        self.baudrateEntry = tk.Entry(advanced_options_frame, state = "disabled")
        self.baudrateEntry.grid(row = 1, column = 1, padx = 10)

        sbLabel = tk.Label(advanced_options_frame, text = "Stop Bit", state = "disabled")
        sbLabel.grid(row = 2, column = 0)
        self.sbEntry = tk.Entry(advanced_options_frame, state = "disabled")
        self.sbEntry.grid(row = 2, column = 1, padx = 10)

        parityLabel = tk.Label(advanced_options_frame, text = "Parity", state = "disabled")
        parityLabel.grid(row = 1, column = 2)
        self.parityEntry = tk.Entry(advanced_options_frame, state = "disabled")
        self.parityEntry.grid(row = 1, column = 3, padx = 10, pady = 5)

        lengthLabel = tk.Label(advanced_options_frame, text = "Length", state = "disabled")
        lengthLabel.grid(row = 2, column = 2)
        self.lengthEntry = tk.Entry(advanced_options_frame, state = "disabled")
        self.lengthEntry.grid(row = 2, column = 3, padx = 10)

        timeoutLabel = tk.Label(advanced_options_frame, text = "Timeout", state = "disabled")
        timeoutLabel.grid(row = 1, column = 4)
        self.timeoutEntry = tk.Entry(advanced_options_frame, state = "disabled")
        self.timeoutEntry.grid(row = 1, column = 5, padx = 10)

        bytesLabel = tk.Label(advanced_options_frame, text = "Bytes to Read", state = "disabled")
        bytesLabel.grid(row = 2, column = 4)
        self.bytesEntry = tk.Entry(advanced_options_frame, state = "disabled")
        self.bytesEntry.grid(row = 2, column = 5, padx = 10, pady = 5)

    def build_connectiontab(self):
        self.populate_connection_panel()
        self.populate_advanced_options_frame()
