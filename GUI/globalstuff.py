# Classe che tiene tutte le variabili globali al quale possono accedere le varie tab del programma

import random
import tkinter as tk
import threading
import time
from GUI.RealTime import DataFrame as DataFrame
from GUI.RealTime import FileHandler as fh
from GUI.RealTime import FormatData as FormatData
# Inizializzazione di variabili globali
# Realtime
df = None
csvFile = None
mode = "arduino"
timerDelay=1 # Delay in ms, 17 = 60fps, 167 = 6fps
# Engine
rpm = ""
tps = ""
t_h20 = ""
t_air = ""
t_oil = ""
vbb = ""
lambda1_avg = ""
lambda1_raw = ""
k_lambda1 = ""
inj_low = ""
inj_high = ""
gear = ""
# GPS
n_s = ""
e_w= ""
fixQuality = ""
n_sats = ""
hdop = ""
latitude = ""
longitude = ""
velGPS = ""
# Wheel
vel_fsx = "" 
vel_fdx = "" 
vel_rsx = ""
vel_rdx = ""
pot_fsx = ""
pot_fdx = ""
pot_rdx = ""
pot_rsx = ""
steeringEncoder = ""
# Gyroscope
gyro_x = ""
gyro_y = ""
gyro_z = ""
accel_x = ""
accel_y = ""
accel_z = ""
potRAccuracy = ""
potFAccuracy = ""

"""
def loggingFile():
    global df
    global csvFile
    df = DataFrame.DataFrame()
    csvFile = fh.FileHandler(df)
"""

def initializeValues(master):
    # Engine
    global rpm
    global tps
    global t_h20
    global t_air
    global t_oil
    global vbb
    global lambda1_avg
    global lambda1_raw
    global k_lambda1
    global inj_low
    global inj_high
    global gear
    # GPS
    global n_s
    global e_w
    global fixQuality
    global n_sats
    global hdop
    global latitude
    global longitude
    global velGPS
    # WheelFrame
    global vel_fsx
    global vel_fdx
    global vel_rsx
    global vel_rdx
    global pot_fdx
    global pot_fsx
    global pot_rdx
    global pot_rsx
    global potFAccuracy
    global potRAccuracy
    global steeringEncoder
    # Gyroscope
    global gyro_x
    global gyro_y
    global gyro_z
    global accel_x
    global accel_y
    global accel_z
    # Engine
    rpm = tk.StringVar(master)
    tps = tk.StringVar(master)
    t_h20 = tk.StringVar(master)
    t_air = tk.StringVar(master)
    t_oil = tk.StringVar(master)
    vbb = tk.StringVar(master)
    lambda1_avg = tk.StringVar(master)
    lambda1_raw = tk.StringVar(master)
    k_lambda1 = tk.StringVar(master)
    inj_low = tk.StringVar(master)
    inj_high = tk.StringVar(master)
    gear = tk.StringVar(master)
    # GPS
    n_s = tk.StringVar(master)
    e_w = tk.StringVar(master)
    fixQuality = tk.StringVar(master)
    n_sats = tk.StringVar(master)
    hdop = tk.StringVar(master)
    latitude = tk.StringVar(master)
    longitude = tk.StringVar(master)
    velGPS = tk.StringVar(master)
    # Wheel
    vel_fsx = tk.StringVar(master) 
    vel_fdx = tk.StringVar(master) 
    vel_rsx = tk.StringVar(master)
    vel_rdx = tk.StringVar(master)
    pot_fsx = tk.StringVar(master)
    pot_fdx = tk.StringVar(master)
    pot_rdx = tk.StringVar(master)
    pot_rsx = tk.StringVar(master)
    potFAccuracy = tk.StringVar(master)
    potRAccuracy = tk.StringVar(master)
    steeringEncoder = tk.StringVar(master)
    # Gyroscope
    gyro_x = tk.StringVar(master)
    gyro_y = tk.StringVar(master)
    gyro_z = tk.StringVar(master)
    accel_x = tk.StringVar(master)
    accel_y = tk.StringVar(master)
    accel_z = tk.StringVar(master)    