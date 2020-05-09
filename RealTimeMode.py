import GUI.globalstuff as globalstuff
import tkinter as tk 
import tkinter.ttk as ttk
from GUI import tableview as tx
from GUI.RealTime import SerialHandler as sh
import GUI.Launcher.settings as settings
import GUI.RealTime.DataFrame as DataFrame
import GUI.RealTime.FormatData as FormatData
import GUI.RealTime.FileHandler as FileHandler

from multiprocessing import Process, Pipe

fh_sh_pipe, sh_fh_pipe = Pipe()
gui_fh_pipe, fh_gui_pipe = Pipe()

class Application(tk.Frame):
    #########
    # SETUP #
    #########
    def __init__(self, master = None):
        # Creazione pipes di comunicazione
        
        
        # inizializzazione del DataFrame con le opportune pipes
        self.df = DataFrame.DataFrame()
        self.csvFile = FileHandler.FileHandler(self.df, fh_sh_pipe, fh_gui_pipe)

        self.mysettings = settings.settings("temp")
        self.mysettings.loadSettings()
        # Crea il master e lo assegna come attributo della classe
        self.fullscreenBoolean = False
        # Inizializzo i lavori del backend
        self.initializeSerial() #Mi crea un self.serialConnection
        # Inizio a disegnare la GUI

        # run multiprocessing        
        
        self.master = master
        tk.Frame.__init__(self, master)
        # Inizializza le var globali e le trasforma in StringVar
        globalstuff.initializeValues(master)
        self.updateThread()
        self.configureGUI() # Imposta i default della finestra
        self.master.rowconfigure(0)
        self.master.columnconfigure(0)
        self.master.grid()
        self.assembleWidgets()
    
    def onclose(self):
        self.master.destroy()
        self.serialConnection.closePort()
    
    def configureGUI(self):
        self.master.title("Formula SAE UniPG 2020 - Real Time Mode")
        self.master.bind("<F11>", self.toggleFullscreen)
        self.master.minsize(800, 600)
        self.master.resizable(True, True)
        top = self.master.winfo_toplevel()
        top.aspect(4,3,4,3)
        self.master.protocol("WM_DELETE_WINDOW", self.onclose)
        
    def initializeSerial(self):
        print("Connecting to the serial using: ", self.mysettings.currentSettings())
        self.serialConnection = sh.SerialHandler(name = self.mysettings.getportname(),
                                                 baudrate = self.mysettings.getbaudrate(),
                                                 sh_fh_pipe = sh_fh_pipe,
                                                 stopBit = self.mysettings.getstopbit(),
                                                 length = self.mysettings.getpacketlength(),
                                                 parity = self.mysettings.getparity(),
                                                 timeout = self.mysettings.getupdatetimeout(),
                                                 bytesToRead = self.mysettings.getbytestoread()
                                                )
        #self.serialConnection.openPort() DEPRECATED, la porta la apre in automatico il SerialHandler

    def updateThread(self):

        # read from pipe
        
        #data = self.serialConnection.readData(startChar = b'\x02', endChar=b'\x03') DEPRECATED, la lettura è effettuata via Pipe
        #FormatData.FormatData.setData(df, data, csvFile) DEPRECATED, la lettura è automatica nel FileHandler
        
        # engineFrame=df.getEngineFrame() DEPRECATED, la lettura è effettuata sotto dalla pipe in automatico
        # GPSFrame=df.getGPSFrame() DEPRECATED, la lettura è effettuata sotto dalla pipe in automatico
        # wheelSensorsFrame=df.getWheelSensorsFrame() DEPRECATED, la lettura è effettuata sotto dalla pipe in automatico
        # gyroscopeFrame=df.getGyroscopeFrame() DEPRECATED, la lettura è effettuata sotto dalla pipe in automatico

        engineFrame, GPSFrame, wheelSensorsFrame, gyroscopeFrame = gui_fh_pipe.recv()
        
        # EngineFrame
        globalstuff.rpm.set(engineFrame["rpm"])
        globalstuff.tps.set(engineFrame["tps"])
        globalstuff.t_h20.set(engineFrame["t_h20"])
        globalstuff.t_air.set(engineFrame["t_air"])
        globalstuff.t_oil.set(engineFrame["t_oil"])
        globalstuff.vbb.set(engineFrame["vbb"])
        globalstuff.lambda1_avg.set(engineFrame["lambda1_avg"])
        globalstuff.lambda1_raw.set(engineFrame["lambda1_raw"])
        globalstuff.k_lambda1.set(engineFrame["k_lambda1"])
        globalstuff.inj_low.set(engineFrame["inj_low"])
        globalstuff.inj_high.set(engineFrame["inj_high"])
        globalstuff.gear.set(engineFrame["gear"])
        # GPSFrame
        globalstuff.n_s.set(GPSFrame["n_s"])
        globalstuff.e_w.set(GPSFrame["e_w"])
        globalstuff.fixQuality.set(GPSFrame["fixQuality"])
        globalstuff.n_sats.set(GPSFrame["n_sats"])
        globalstuff.hdop.set(GPSFrame["hdop"])
        globalstuff.latitude.set(GPSFrame["latitude"])
        globalstuff.longitude.set(GPSFrame["longitude"])
        globalstuff.velGPS.set(GPSFrame["velGPS"])
        # wheelsensorsFrame
        globalstuff.vel_fsx.set(wheelSensorsFrame["vel_fsx"])
        globalstuff.vel_fdx.set(wheelSensorsFrame["vel_fdx"])
        globalstuff.vel_rsx.set(wheelSensorsFrame["vel_rsx"])
        globalstuff.vel_rdx.set(wheelSensorsFrame["vel_rdx"])
        globalstuff.pot_fsx.set(wheelSensorsFrame["pot_fsx"])
        globalstuff.pot_fdx.set(wheelSensorsFrame["pot_fdx"])
        globalstuff.pot_rdx.set(wheelSensorsFrame["pot_rdx"])
        globalstuff.pot_rsx.set(wheelSensorsFrame["pot_rsx"])
        globalstuff.potFAccuracy.set(wheelSensorsFrame["potFAccuracy"])
        globalstuff.potRAccuracy.set(wheelSensorsFrame["potRAccuracy"])
        globalstuff.steeringEncoder.set(wheelSensorsFrame["steeringEncoder"])
        # gyroscopeFrame
        globalstuff.gyro_x.set(gyroscopeFrame["gyro_x"])
        globalstuff.gyro_y.set(gyroscopeFrame["gyro_y"])
        globalstuff.gyro_z.set(gyroscopeFrame["gyro_z"])
        globalstuff.accel_x.set(gyroscopeFrame["accel_x"])
        globalstuff.accel_y.set(gyroscopeFrame["accel_y"])
        globalstuff.accel_z.set(gyroscopeFrame["accel_z"])
        self.master.after(globalstuff.timerDelay, self.updateThread)


   # Widget Creation

    def createNotebook(self):
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand = 1, fill = "both") #.grid() non mi dava la possibilità  di espandere a tutto schermo
        
    def createMenu(self):
        top = self.winfo_toplevel()
        self.menuBar = tk.Menu(top)
        top["menu"] = self.menuBar
        self.filesMenu = tk.Menu(self.menuBar)
        self.optionsMenu = tk.Menu(self.menuBar)
        self.menuTabs()
        self.helpMenu = tk.Menu(self.menuBar)
        self.menuBar.add_cascade(label = "File", menu = self.filesMenu)
        self.menuBar.add_cascade(label = "Options", menu = self.optionsMenu)
        self.menuBar.add_cascade(label = "Help", menu = self.helpMenu)
    
    def menuTabs(self):
        self.optionsMenu.add_checkbutton(label = "Fullscreen (F11)", command = self.toggleFullscreen)
        
    def toggleFullscreen(self, event=None):
        self.fullscreenBoolean = not self.fullscreenBoolean
        self.master.wm_attributes("-fullscreen", self.fullscreenBoolean)

    def assembleWidgets(self):
        # Assembla i widget delle varie tab, aggiungendo all'inizio i due propri di questo modulo
        self.createMenu()
        self.createNotebook()
        self.textvarFrame = tx.createTextTab(self.notebook)
        tx.populatetextvarFrame(self.textvarFrame)
        #self.virtualCockpitFrame = vc.createTextTab(self.notebook, self.master)
        #vc.populateVCTab(self.virtualCockpitFrame, self.master, self.textvarFrame)

def main():
    root2 = tk.Tk()
    root2.iconbitmap("res/icon.ico")
    Application()
    root2.mainloop()

if __name__ == "__main__":
    main()
    