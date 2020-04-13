import tkinter as tk
class ConnectionStatus():
    def __init__(self, master):
        self.status = tk.StringVar(master)
        self.status.set("Offline")
    
    def go_online(self, master):
        self.status.set("Online!")
    
    def go_offline(self, master):
        self.status.set("Offline")