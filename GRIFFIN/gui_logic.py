import tkinter as tk
class GUI_LOGIC_HANDLER():
    def __init__(self, master):
        self.status = tk.StringVar(master)
        self.status.set("Offline")
    
    def go_online(self):
        self.status.set("Online!")
    
    def go_offline(self):
        self.status.set("Offline")

    def toggle_advanced_options(self, checkbox, checkbox_variable, checkbox_label = None):
        # Per usare correttamente questa funzione, la checkbox label, il checkbox e la checkbox variable devono tutti essere all'interno dello stesso frame
        # La checkbox_label è opzionale
        # Il frame deve contenere solo le checkbox e le opzioni da attivare o disattivare
        checkbox_father = checkbox.master # (9) per ulteriori dettagli
        if checkbox_variable.get():
            for e in checkbox_father.winfo_children():
                e.config(state = "normal")
        else:
            for e in checkbox_father.winfo_children():
                e.config(state = "disabled")
                if checkbox_label is not None: checkbox_label.config(state = "normal")
                checkbox.config(state = "normal")

    def port_selected(self, connect_button, event):
        # Essendo bindato ad un evento di tkinter, gli sarà SEMPRE passato per ultimo un
        # oggetto del tipo tkinter.Event (11)
        connect_button.config(state = "normal")

    def check_ports(self, port_combobox):
        #portlist = control.checkavaibleports()
        portlist = ["test", "test2", "test3", "test4"]
        port_combobox.config(values = portlist)

    def start_serial_connection(self, connection_dictionary, connect_button, disconnect_button):
        print(connection_dictionary)
        #control_startserial(nome, baudrate, stopbit ecc ecc)
        connect_button.config(state = "disabled")
        # TODO gestione connessione fallita
        GUI_LOGIC_HANDLER.go_online(self)
        disconnect_button.config(state = "normal")

    def stop_serial_connection(self, connect_button, disconnect_button):
        print("disconnected")
        connect_button.config(state = "normal")
        GUI_LOGIC_HANDLER.go_offline(self)
        disconnect_button.config(state = "disabled")
