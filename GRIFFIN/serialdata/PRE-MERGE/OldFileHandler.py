

import csv, time
from GUI.RealTime import DataFrame

class FileHandler:

#Creates a FileHandler object to save data in CSV file called "dd_mm_yyyy  hh_mm__ss.csv"

    def __init__(self, dataFrame):
        self.__dataFrame = dataFrame
        nome = time.strftime("%a_%d_%b_%Y") + " " + time.strftime("%H_%M_%S_")
        self.__name100Hz = nome + "100Hz.csv"
        self.__name10Hz = nome + "10Hz.csv"
        self.__name4Hz = nome + "4Hz.csv"
        self.__fieldnames100Hz  = ['rpm', 'tps', 'accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'pot_fsx',  'pot_fdx', 'pot_FAccuracy', 'pot_rsx',  'pot_rdx', 'pot_RAccuracy','steeringEncoder']
        self.__fieldnames10Hz  = ['t_h20', 't_air', 't_oil', 'vbb', 'lambda1_avg', 'lambda1_raw', 'k_lambda1', 'inj_low', 'inj_high']
        self.__fieldnames4Hz = [''] #DA FARE
        with open(self.__name100Hz, 'w', newline='') as file100Hz:
            writer = csv.writer(file100Hz, delimiter=';', dialect='excel')
            writer.writerow(self.__fieldnames100Hz)
        with open(self.__name10Hz, 'w', newline='') as file10Hz:
            writer = csv.writer(file10Hz, delimiter=';', dialect='excel')
            writer.writerow(self.__fieldnames10Hz)
        with open(self.__name4Hz, 'w', newline='') as file4Hz:
            writer = csv.writer(file4Hz, delimiter=';', dialect='excel')
            writer.writerow(self.__fieldnames4Hz)

#Appends data to the file created before
    def write100Hz(self):
        engineFrame100Hz = self.__dataFrame.getEngineFrame()
        wheelFrame100Hz = self.__dataFrame.getWheelSensorsFrame()
        gyroscopeFrame100Hz = self.__dataFrame.getGyroscopeFrame()
        FrameValues100Hz = [engineFrame100Hz["rpm"], engineFrame100Hz["tps"]]
        FrameValues100Hz.append(gyroscopeFrame100Hz['accel_x'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['accel_y'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['accel_z'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['gyro_x'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['gyro_y'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['gyro_z'])
        FrameValues100Hz.append(wheelFrame100Hz['pot_fsx'])
        FrameValues100Hz.append(wheelFrame100Hz['pot_fdx'])
        FrameValues100Hz.append(wheelFrame100Hz['potFAccuracy'])
        FrameValues100Hz.append(wheelFrame100Hz['pot_rsx'])
        FrameValues100Hz.append(wheelFrame100Hz['pot_rdx'])
        FrameValues100Hz.append(wheelFrame100Hz['potRAccuracy'])
        FrameValues100Hz.append(wheelFrame100Hz['steeringEncoder'])
        # gpsFrameValues = list(self.__dataFrame.getGPSFrame().values())
        # wheelSensorsFrameValues = list(self.__dataFrame.getWheelSensorsFrame().values()) + 
        # gyroscopeFrameValues = list(self.__dataFrame.getGyroscopeFrame().values())
        with open (self.__name100Hz, 'a', newline='') as csvfile100Hz:
            writer = csv.writer(csvfile100Hz, delimiter=';', dialect='excel')
            writer.writerow(FrameValues100Hz)
    
    def write10Hz(self):
        engineFrame10Hz = self.__dataFrame.getEngineFrame()
        FrameValues10Hz = [engineFrame10Hz["t_h20"], engineFrame10Hz["t_air"], engineFrame10Hz["t_oil"], engineFrame10Hz["vbb"], engineFrame10Hz["lambda1_avg"], engineFrame10Hz["lambda1_raw"], engineFrame10Hz["k_lambda1"], engineFrame10Hz["inj_low"], engineFrame10Hz["inj_high"]]
        with open (self.__name10Hz, 'a', newline='') as csvfile10Hz:
            writer = csv.writer(csvfile10Hz, delimiter=';', dialect='excel')
            writer.writerow(FrameValues10Hz)
