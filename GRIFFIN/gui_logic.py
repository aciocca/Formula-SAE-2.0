import tkinter as tk
from tkinter.font import Font
class GUI_LOGIC_HANDLER():
    def __init__(self, master):
        self.status = tk.StringVar(master)
        self.status.set("Offline")
        GUI_LOGIC_HANDLER.initialize_dictionaries(self, master)
        GUI_LOGIC_HANDLER.font_variables(self)
        
    def font_variables(self):
        self.bold = Font(weight = "bold", size = 12)
    
    def initialize_dictionaries(self, master):
        # Funzione a parte per miglior ordine
        self.rpm = tk.StringVar(master)
        self.tps = tk.StringVar(master)
        self.t_h20 = tk.StringVar(master)
        self.t_air = tk.StringVar(master)
        self.t_oil = tk.StringVar(master)
        self.vbb = tk.StringVar(master)
        self.lambda1_avg = tk.StringVar(master)
        self.lambda1_raw = tk.StringVar(master)
        self.k_lambda1 = tk.StringVar(master)
        self.inj_low = tk.StringVar(master)
        self.inj_high = tk.StringVar(master)
        self.gear = tk.StringVar(master)
        # GPS
        self.n_s = tk.StringVar(master)
        self.e_w = tk.StringVar(master)
        self.fixQuality = tk.StringVar(master)
        self.n_sats = tk.StringVar(master)
        self.hdop = tk.StringVar(master)
        self.latitude = tk.StringVar(master)
        self.longitude = tk.StringVar(master)
        self.velGPS = tk.StringVar(master)
        # Wheel
        self.vel_fsx = tk.StringVar(master) 
        self.vel_fdx = tk.StringVar(master) 
        self.vel_rsx = tk.StringVar(master)
        self.vel_rdx = tk.StringVar(master)
        self.pot_fsx = tk.StringVar(master)
        self.pot_fdx = tk.StringVar(master)
        self.pot_rdx = tk.StringVar(master)
        self.pot_rsx = tk.StringVar(master)
        self.potFAccuracy = tk.StringVar(master)
        self.potRAccuracy = tk.StringVar(master)
        self.steeringEncoder = tk.StringVar(master)
        # Gyroscope
        self.gyro_x = tk.StringVar(master)
        self.gyro_y = tk.StringVar(master)
        self.gyro_z = tk.StringVar(master)
        self.accel_x = tk.StringVar(master)
        self.accel_y = tk.StringVar(master)
        self.accel_z = tk.StringVar(master)    
    
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

