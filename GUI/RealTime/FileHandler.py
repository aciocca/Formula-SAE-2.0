import csv, time, os
# from GUI.RealTime import DataFrame
from GUI.RealTime.FormatData import FormatData as fd
from multiprocessing import Process, Pipe

# Sottoprocesso che legge i dati dalla pipe in arrivo dal SerialHandler;
# Pulisce i dati e li formatta in dizionari attraverso il FormatData
# I dati vengono salvati su gli appositi files per i dati a 100, 10, 4 Hz
# TODO: implementare passaggio di dati tra FileHandler e classe della GUI #

def subProcessFunction(obj):
    obj.openFile()

    while True:
        print("--- clock File Handler ---")
        pipeInput = obj.sh_fh_pipe.recv()
        print("Process: ", pipeInput)
        df = obj.getDataFrame()
        fd.setData(df, pipeInput, obj)
        engineFrame=df.getEngineFrame()
        GPSFrame=df.getGPSFrame()
        wheelSensorsFrame=df.getWheelSensorsFrame()
        gyroscopeFrame=df.getGyroscopeFrame()
        obj.fh_gui_pipe.send((engineFrame, GPSFrame, wheelSensorsFrame, gyroscopeFrame))
    

class FileHandler:

    __doc__='''Documentation for FormatData.py functions:

    __init__(self, dataFrame):
        creates a fileHandler object to save data in a CSV file called "dd_mm_yyyy  hh_mm__ss.csv"
        the fileHandler object has a dataFrame variable where the dataFrame is saved
        it opens the three files in order to have them ready to be written

    write100Hz():
        writes new 100Hz data inside the .csv file.
        In order to save data carefully it closes the file every 500 writings (5 seconds)

    write10Hz():
        writes new 10Hz data inside the .csv file.
        In order to save data carefully it closes the file every 50 writings (5 seconds)

    write4Hz():
        writes new 4Hz data inside the .csv file.
        In order to save data carefully it closes the file every 20 writings (5 seconds)

    writeReadError():
        used in formatData.setData() to fill the .csv files' fields with 'ReadError'. 
        Since we do not know which block is transmitting, a line full of 'ReadError' will be added to every file (100Hz, 10Hz, 4Hz)     
    '''

#Creates a FileHandler object to save data in a CSV file called "dd_mm_yyyy_hh_mm_ss.csv"

    def __init__(self, dataFrame, sh_fh_pipe, fh_gui_pipe):
        self.__dataFrame = dataFrame
        dir_ = "resources/"
        name = time.strftime("%a_%d_%b_%Y") + "_" + time.strftime("%H_%M_%S_")
        self.__name100Hz = dir_ + name + "100Hz.csv"
        self.__name10Hz = dir_ + name + "10Hz.csv"
        self.__name4Hz = dir_ + name + "4Hz.csv"
       
        # Getting dictionaries from a dataFrame object
        self.__engineFrame = self.__dataFrame.getEngineFrame()
        self.__wheelFrame = self.__dataFrame.getWheelSensorsFrame()
        self.__gyroscopeFrame = self.__dataFrame.getGyroscopeFrame()
        self.__GPSFrame = self.__dataFrame.getGPSFrame()
        
        # Dictionaries used to write data inside the .csv file (sorted by frequency)
        self.__FrameValues100Hz = {'rpm': 0, 'tps': 0.0, 'accel_x': 0.0, 'accel_y': 0.0, 'accel_z': 0.0, 'gyro_x': 0.0, 'gyro_y': 0.0, 'gyro_z': 0.0, 'pot_fsx': 0.0, 'pot_fdx': 0.0, 'pot_FAccuracy': 0.0, 'pot_rsx': 0.0, 'pot_rdx': 0.0, 'pot_RAccuracy': 0.0,'steeringEncoder': 0.0, 'vel_fsx': 0.0, 'vel_fdx': 0.0, 'vel_rsx': 0.0, 'vel_rdx': 0.0, 'gear': 0}       
        self.__FrameValues10Hz = {'t_h20': 0, 't_air': 0, 't_oil': 0, 'vbb': 0.0, 'lambda1_avg': 0.0, 'lambda1_raw': 0.0, 'k_lambda1': 0.0, 'inj_low': 0.0, 'inj_high': 0.0}  
        self.__FrameValues4Hz = {'hour': 0, 'minutes': 0, 'seconds': 0, 'micro_seconds': 0.0, 'n_sats': 0, 'fixQuality': 0, 'e_w': "", 'n_s': "", 'hdop': 0.0, 'latitude': 0.0, 'longitude': 0.0, 'velGPS': 0.0}
                
        # LINES WRITTEN (USED TO KNOW THE FILE HAS TO BE CLOSED AND REOPENED)
        self.__lineNumber100Hz = 0
        self.__lineNumber10Hz = 0
        self.__lineNumber4Hz = 0

        # PIPES
        self.sh_fh_pipe = sh_fh_pipe
        self.fh_gui_pipe = fh_gui_pipe

        # CREATE DIR IF NOT EXIST (RELATIVE_PATH)
        if not os.path.exists(dir_):
            os.makedirs(dir_)

    def openFile(self):
        #CREATION OF THE dd_mm_yyyy_hh_mm_ss_100Hz.csv FILE        
        self.__file100Hz = open(self.__name100Hz, 'w', newline='')
        self.__writerFile100Hz = csv.writer(self.__file100Hz, delimiter=',', dialect='excel')
        self.__writerFile100Hz.writerow(list(self.__FrameValues100Hz.keys()))
        
        #CREATION OF THE dd_mm_yyyy_hh_mm_ss_10Hz.csv FILE
        self.__file10Hz = open(self.__name10Hz, 'w', newline='')
        self.__writerFile10Hz = csv.writer(self.__file10Hz, delimiter=',', dialect='excel')
        self.__writerFile10Hz.writerow(list(self.__FrameValues10Hz.keys()))
        
        #CREATION OF THE dd_mm_yyyy_hh_mm_ss_4Hz.csv FILE
        self.__file4Hz = open(self.__name4Hz, 'w', newline='')
        self.__writerFile4Hz = csv.writer(self.__file4Hz, delimiter=',', dialect='excel')
        self.__writerFile4Hz.writerow(list(self.__FrameValues4Hz.keys()))

    def run(self):
        print("Funzione Run")
        self.p = Process(target=subProcessFunction, args=(self,))
        self.p.start()

    def join(self):
        self.p.join()

    def getDataFrame(self):
        return self.__dataFrame

#Appends data to the file created before
    def write100Hz(self):
        #getting the updated dictionaries from the dataFrame object
        self.__engineFrame = self.__dataFrame.getEngineFrame()
        self.__wheelFrame = self.__dataFrame.getWheelSensorsFrame()
        self.__gyroscopeFrame = self.__dataFrame.getGyroscopeFrame()

        #Updating the "writing" dictionary with new values (a loop isn't used because three different frames are needed)
        self.__FrameValues100Hz["rpm"] = self.__engineFrame["rpm"]
        self.__FrameValues100Hz["tps"] = self.__engineFrame["tps"]
        self.__FrameValues100Hz['gear'] = self.__engineFrame['gear']
        self.__FrameValues100Hz['accel_x'] = self.__gyroscopeFrame['accel_x']
        self.__FrameValues100Hz['accel_y'] = self.__gyroscopeFrame['accel_y']
        self.__FrameValues100Hz['accel_z'] = self.__gyroscopeFrame['accel_z']
        self.__FrameValues100Hz['gyro_x'] = self.__gyroscopeFrame['gyro_x']
        self.__FrameValues100Hz['gyro_y'] = self.__gyroscopeFrame['gyro_y']
        self.__FrameValues100Hz['gyro_z'] = self.__gyroscopeFrame['gyro_z']
        self.__FrameValues100Hz['pot_fsx'] = self.__wheelFrame['pot_fsx']
        self.__FrameValues100Hz['pot_fdx'] = self.__wheelFrame['pot_fdx']
        self.__FrameValues100Hz['potFAccuracy'] = self.__wheelFrame['potFAccuracy']
        self.__FrameValues100Hz['pot_rsx'] = self.__wheelFrame['pot_rsx']
        self.__FrameValues100Hz['pot_rdx'] = self.__wheelFrame['pot_rdx']
        self.__FrameValues100Hz['potRAccuracy'] = self.__wheelFrame['potRAccuracy']
        self.__FrameValues100Hz['steeringEncoder'] = self.__wheelFrame['steeringEncoder']
        self.__FrameValues100Hz['vel_fsx'] = self.__wheelFrame['vel_fsx']
        self.__FrameValues100Hz['vel_fdx'] = self.__wheelFrame['vel_fdx']
        self.__FrameValues100Hz['vel_rsx'] = self.__wheelFrame['vel_rsx']
        self.__FrameValues100Hz['vel_rdx'] = self.__wheelFrame['vel_rdx']
        self.__FrameValues100Hz['gear'] = self.__engineFrame['gear']



        #Writing the whole line in dd_mm_yyyy_hh_mm_ss_100Hz.csv file
        self.__writerFile100Hz.writerow(list(self.__FrameValues100Hz.values()))

        # CLOSES THE FILE EVERY 500 WRITINGS
        self.__lineNumber100Hz = (self.__lineNumber100Hz + 1) % 500
        if (self.__lineNumber100Hz==0):
            self.__file100Hz.close()
            self.__file100Hz = open(self.__name100Hz, 'a', newline='')
            self.__writerFile100Hz = csv.writer(self.__file100Hz, delimiter=',', dialect='excel')

    def write10Hz(self):
        #getting the updated dictionariy from the dataFrame object (only engineFrame is needed)
        self.__engineFrame = self.__dataFrame.getEngineFrame()
        
        #Updating the "writing" dictionary
        for key in self.__FrameValues10Hz.keys():
            self.__FrameValues10Hz[key] = self.__engineFrame[key]

        #Writing the whole line in dd_mm_yyyy_hh_mm_ss_10Hz.csv
        self.__writerFile10Hz.writerow(list(self.__FrameValues10Hz.values()))
        
        # CLOSES THE FILE EVERY 50 WRITINGS
        self.__lineNumber10Hz = (self.__lineNumber10Hz + 1) % 50
        if (self.__lineNumber10Hz==0):
            self.__file10Hz.close()
            self.__file10Hz = open(self.__name10Hz, 'a', newline='')
            self.__writerFile10Hz = csv.writer(self.__file10Hz, delimiter=',', dialect='excel')
    
    def write4Hz(self):
        #getting the updated dictionariy from the dataFrame object (only GPSFrame is needed)
        self.__GPSFrame = self.__dataFrame.getGPSFrame()
        
        #Updating the "writing" dictionary
        for key in self.__FrameValues4Hz.keys():
            self.__FrameValues4Hz[key] = self.__GPSFrame[key]

        #Writing the whole line in dd_mm_yyyy_hh_mm_ss_4Hz.csv
        self.__writerFile4Hz.writerow(list(self.__FrameValues4Hz.values()))

        # CLOSES THE FILE EVERY 20 WRITINGS
        self.__lineNumber4Hz = (self.__lineNumber4Hz + 1) % 20
        if (self.__lineNumber4Hz==0):
            self.__file4Hz.close()
            self.__file4Hz = open(self.__name4Hz, 'a', newline='')
            self.__writerFile4Hz = csv.writer(self.__file4Hz, delimiter=',', dialect='excel')
    
    #if the headerIndex has been received writes "ReadError" in the whole line of the file. If not received, "ReadError" will be written in the last line of each file
    def writeReadError(self, *args):
        if len(args) > 0:
            if args[0] == 0x3F:
                self.__writerFile100Hz.writerow(['ReadError'] * len(self.__FrameValues100Hz.keys()))
            elif args[0] == 0x0A:
                self.__writerFile10Hz.writerow(['ReadError'] * len(self.__FrameValues10Hz.keys()))
            elif args[0] == 0x04:
                self.__writerFile4Hz.writerow(['ReadError'] * len(self.__FrameValues4Hz.keys()))

        else:   
            self.__writerFile100Hz.writerow(['ReadError'] * len(self.__FrameValues100Hz.keys()))
            self.__writerFile10Hz.writerow(['ReadError'] * len(self.__FrameValues10Hz.keys()))
            self.__writerFile4Hz.writerow(['ReadError'] * len(self.__FrameValues4Hz.keys()))