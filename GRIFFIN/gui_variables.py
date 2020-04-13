import tkinter as tk
status =""
def initializeStatus(master):
    global status
    status = tk.StringVar(master)
    status.set("Offline")

def go_online(master):
    global status
    # info = serialinterface.get_connection_info()
    if status is None:
        status = tk.StringVar(master)
        #status.append(info)
    status.set("Online!")

def go_offline(master):
    global status
    if status is None:
        status = tk.StringVar(master)
    status.set("Offline")