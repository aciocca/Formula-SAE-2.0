import tkinter as tk
from tkinter.font import Font
from serialdata import Controller
from time import sleep

class GUI_LOGIC_HANDLER():
    def __init__(self, master):
        self.master = master
        self.controller_object = Controller.Controller()
        self.status = tk.StringVar(master)
        self.status.set("Offline")
        self.update = True
        GUI_LOGIC_HANDLER.initialize_dictionaries(self, self.master)
        GUI_LOGIC_HANDLER.font_variables(self)
        
    def font_variables(self):
        self.bold = Font(weight = "bold", size = 12)
    
    def initialize_dictionaries(self, master):
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
        ports_list = self.controller_object.check_avaible_ports()
        port_combobox.config(values = ports_list)

    def start_serial_connection(self, serial_dict, connect_button, disconnect_button):
        # Viene chiamato da gui_connectiontab
        print(serial_dict)
        self.controller_object.start_serial_connection(serial_dict)
        self.fh_gui_pipe = self.controller_object.getGUIPipe()
        connect_button.config(state = "disabled")
        # TODO gestione connessione fallita
        GUI_LOGIC_HANDLER.go_online(self)
        disconnect_button.config(state = "normal")
        GUI_LOGIC_HANDLER.update_loop(self)



    def stop_serial_connection(self, connect_button, disconnect_button):
        print("disconnected")
        connect_button.config(state = "normal")
        GUI_LOGIC_HANDLER.go_offline(self)
        disconnect_button.config(state = "disabled")
    
    def update_loop(self):
    
        dict_100hz, dict_10hz, dict_4hz = self.fh_gui_pipe.recv()
        
        # 100Hz
        self.rpm.set(dict_100hz["rpm"])
        self.tps.set(dict_100hz["tps"])
        self.gear.set(dict_100hz["gear"])
        self.accel_x.set(dict_100hz["accel_x"])
        self.accel_y.set(dict_100hz["accel_y"])
        self.accel_z.set(dict_100hz["accel_z"])
        self.gyro_x.set(dict_100hz["gyro_x"])
        self.gyro_y.set(dict_100hz["gyro_y"])
        self.gyro_z.set(dict_100hz["gyro_z"])
        self.vel_fsx.set(dict_100hz["vel_fsx"])
        self.vel_fdx.set(dict_100hz["vel_fdx"])
        self.vel_rsx.set(dict_100hz["vel_rsx"])
        self.vel_rdx.set(dict_100hz["vel_rdx"])
        self.pot_fdx.set(dict_100hz["pot_fdx"])
        self.pot_fsx.set(dict_100hz["pot_fsx"])
        self.pot_rsx.set(dict_100hz["pot_rsx"])
        self.pot_rdx.set(dict_100hz["pot_rdx"])
        self.potFAccuracy.set(dict_100hz["potFAccuracy"])
        self.potRAccuracy.set(dict_100hz["potRAccuracy"])
        self.steeringEncoder.set(dict_100hz["steeringEncoder"])
        
        # 10Hz
        self.t_h20.set(dict_10hz["t_h20"])
        self.t_air.set(dict_10hz["t_air"])
        self.t_oil.set(dict_10hz["t_oil"])
        self.vbb.set(dict_10hz["vbb"])
        self.lambda1_avg.set(dict_10hz["lambda1_avg"])
        self.lambda1_raw.set(dict_10hz["lambda1_raw"])
        self.k_lambda1.set(dict_10hz["k_lambda1"])
        self.inj_low.set(dict_10hz["inj_low"])
        self.inj_high.set(dict_10hz["inj_high"])

        # 4Hz
        self.n_s.set(dict_4hz["n_s"])
        self.e_w.set(dict_4hz["e_w"])
        self.fixQuality.set(dict_4hz["fixQuality"])
        self.n_sats.set(dict_4hz["n_sats"])
        self.hdop.set(dict_4hz["hdop"])
        self.latitude.set(dict_4hz["latitude"])
        self.longitude.set(dict_4hz["longitude"])
        self.velGPS.set(dict_4hz["velGPS"])
        self.master.after(1, self.update_loop)
        
        

