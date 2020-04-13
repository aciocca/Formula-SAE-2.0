import tkinter as tk
import tkinter.ttk as ttk 
class TextviewTab():
    def __init__(self, notebook):
        textmodeframe = tk.Frame(notebook, name = "textmodeframe")
        textmodeframe.grid(row = 0, column = 0, sticky = "nsew")
        textmodeframe.columnconfigure(0, weight = 1)
        textmodeframe.columnconfigure(1, weight = 2)
        textmodeframe.columnconfigure(2, weight = 1)
        textmodeframe.columnconfigure(3, weight = 1)
        textmodeframe.columnconfigure(4, weight = 1)
        textmodeframe.columnconfigure(5, weight = 2)
        textmodeframe.columnconfigure(6, weight = 1)
        textmodeframe.rowconfigure(0, weight = 1)
        textmodeframe.rowconfigure(1, weight = 2)
        textmodeframe.rowconfigure(2, weight = 1)
        textmodeframe.rowconfigure(3, weight = 2)
        textmodeframe.rowconfigure(4, weight = 1)
        textmodeframe.rowconfigure(5, weight = 1)
        textmodeframe.rowconfigure(6, weight = 1)
        notebook.add(textmodeframe, text = "Text Mode")
