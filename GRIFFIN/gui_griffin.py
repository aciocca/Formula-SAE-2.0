import tkinter as tk
import tkinter.ttk as ttk
import gui_logic as gl
import gui_connectiontab as cntab
import gui_textviewtab as txtab 


class GRIFFINGUI(tk.Frame):

    def toggle_fullscreen(self, event=None):
        # Permette di passare da windowed a fullscreen e viceversa (1)
        is_fullscreen = self.winfo_toplevel().wm_attributes("-fullscreen")
        is_fullscreen = not is_fullscreen
        self.winfo_toplevel().wm_attributes("-fullscreen", is_fullscreen)
    
    def onclose(self):
        # Eseguito quando viene chiusa la finestra, le funzioni di cleanup vengono messe qui
        # Per l'uso di destroy vedi (2)
        self.logic_handler.go_offline()
        self.winfo_toplevel().destroy()
        
    def configure_window_defaults(self):
        top_level_window = self.winfo_toplevel()
        # Contiene tutti i parametri di default della finestra
        top_level_window.bind("<F11>", self.toggle_fullscreen)
        top_level_window.minsize(800, 600)
        top_level_window.title("GRIFFIN 2020 Edition")
        top_level_window.aspect(4,3,4,3)
        top_level_window.protocol("WM_DELETE_WINDOW", self.onclose)
        top_level_window.iconbitmap("res/griffin_base.ico")
    
    def create_menubar(self):
        # Si occupa delle barre dei menu (5) per ulteriori info
        menubar = tk.Menu(self.winfo_toplevel(), name = "menubar")
        # Necessario per evitare che il garbage collector cancelli la barra dei menu prima di essere visualizzata (3; 4)
        self.winfo_toplevel()["menu"] = menubar
        filemenu = tk.Menu(menubar, name = "filemenu")
        settingsmenu = tk.Menu(menubar, name = "settingsmenu")
        helpmenu = tk.Menu(menubar, name = "helpmenu")
        menubar.add_cascade(label = "File", menu = filemenu)
        menubar.add_cascade(label = "Settings", menu = settingsmenu)
        menubar.add_cascade(label = "Help", menu = helpmenu)

    def populate_menubar(self):
        # Si occupa di riempire i sottomenu della barra dei menu
        settings = self.winfo_toplevel().nametowidget(".menubar.settingsmenu")
        settings.add_checkbutton(label = "Fullscreen (F11)", command = self.toggle_fullscreen)
        
    def create_notebook(self):
        tabsholder = ttk.Notebook(self.winfo_toplevel(), name = "tabsholder")
        tabsholder.pack(expand = 1, fill = "both") #.grid() mi da la possibilità di espanderlo a tutto schermo

    def populate_notebook(self):
        griffin_notebook = self.winfo_toplevel().nametowidget("tabsholder")
        # crea la tabella con una funzione presente in un altro modulo e la attacca al mio notebook
        # abbiamo un modulo per tab
        # text data tab
        # virtual cockpit tab
        cntab.ConnectionTab(griffin_notebook, self.logic_handler).build_connectiontab()
        txtab.TextViewTab(griffin_notebook, self.logic_handler).build_textviewtab()

    def create_statusbar(self):
        # Gestisce la statusbar in fondo alla finestra, sempre visibile, qualsiasi sia il tab aperto sopra
        statusbar = tk.Label(self.winfo_toplevel(), name = "statusbar", bd = 1, relief = tk.SUNKEN, anchor = tk.W, textvariable = self.logic_handler.status)
        statusbar.pack(side = tk.BOTTOM, fill = tk.X)

    def assemble_widgets(self):
        # Vedi 8 per sintassi
        GRIFFINGUI.create_menubar(self)
        GRIFFINGUI.populate_menubar(self)
        GRIFFINGUI.create_notebook(self)
        GRIFFINGUI.populate_notebook(self)
        GRIFFINGUI.create_statusbar(self)

    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.configure_window_defaults()
        self.winfo_toplevel().rowconfigure(0)
        self.winfo_toplevel().columnconfigure(0)
        self.winfo_toplevel().grid()
        # Crea un oggetto ConnectionStatus dal modulo gui_logic che conterrà le informazioni sulla connessione, viene utilizzato dalla statusbar
        self.logic_handler = gl.GUI_LOGIC_HANDLER(self.winfo_toplevel())
        self.assemble_widgets()
        

    
    
def run_gui():
    root = tk.Tk()
    GRIFFINGUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
    