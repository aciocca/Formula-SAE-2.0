import json
class settings:
    def __init__(self, portname, **kwargs):
        self.__portName = portname
        try:
            self.__baudRate = kwargs["baudrate"]
        except KeyError:
            self.__baudRate = 115200
        
        try:
            self.__stopBit = kwargs["stopbit"]
        except KeyError:
            self.__stopBit = None
        
        try:
            self.__wordParity = kwargs["parity"]
        except KeyError:
            self.__wordParity = None

        try:
            self.__wordLength = kwargs["packetlength"]
        except KeyError:
            self.__wordLength = None

        try:
            self.__timeout = kwargs["updatetimeout"]
        except KeyError:
            self.__timeout = None

        try:
            self.__bytesToRead = kwargs["bytestoread"]
        except KeyError:
            self.__bytesToRead = None
    

    def setportname(self, portname):
        self.__portName = portname
    def getportname(self):
        return self.__portName

    def setbaudrate(self, baudrate):
        self.__baudRate = baudrate
    def getbaudrate(self):
        return self.__baudRate
    
    def setstopbit(self, stopbit):
        self.__stopBit = int(stopbit)

    def getstopbit(self):
        return self.__stopBit

    def setparity(self, parity):
        self.__wordParity = parity
    def getparity(self):
        return self.__wordParity
    
    def setpacketlength(self, packetlength):
        self.__wordLength = packetlength
    def getpacketlength(self):
        return self.__wordLength

    def setupdatetimeout(self, updatetimeout):
        self.__timeout = updatetimeout
    def getupdatetimeout(self):
        return self.__timeout
    
    def setbytestoread(self, bytestoread):
        self.__bytesToRead = bytestoread
    def getbytestoread(self):
        return self.__bytesToRead
        
    def currentSettings(self):
        settingsDict ={"portname": self.__portName, "baudrate": self.__baudRate, 
                        "stopbit": self.__stopBit, "parity": self.__wordParity,
                        "packetlength": self.__wordLength, "updatetimeout": self.__timeout,
                        "bytestoread": self.__bytesToRead}
        secondDict = dict((a, b) for (a, b) in settingsDict.items() if b is not None)
        print("currentSettings", secondDict)
        return secondDict

    def saveSettings(self):
        try:
            savefile = open(mode = "w", file = "settings.xml")
        except:
            print("File not found, creating a new one")
        json.dump(self.currentSettings(), savefile)
        savefile.close()
    
    def loadSettings(self):
        try:
            loadfile = open(mode = "r", file = "settings.xml")
            settingsList = json.load(loadfile)
        except:
            print("File not found")
            settingsList = {}
        
        # Carica da file un dict con i settings salvati,
        # in caso di mancanza di alcune key dal dizionario
        # (file corrotto?), prova ad usare dei valori "sani"
        # di fallback

        
        try:
            self.__portName = settingsList["portname"]
        except KeyError:
            self.__portName = "COM12"

        try:
            self.__baudRate = settingsList["baudrate"]
        except KeyError:
            self.__baudRate = 115200
        
        try:
            self.__stopBit = settingsList["stopbit"]
        except KeyError:
            self.__stopBit = 1
        
        try:
            self.__wordParity = settingsList["parity"]
        except KeyError:
            self.__wordParity = "N"

        try:
            self.__wordLength = settingsList["packetlength"]
        except KeyError:
            self.__wordLength = 8

        try:
            self.__timeout = settingsList["updatetimeout"]
        except KeyError:
            self.__timeout = 600/self.__baudRate
        
        try:
            self.__bytesToRead = settingsList["bytestoread"]
        except KeyError:
            self.__bytesToRead = 1

        return settingsList

    def resetDefaults(self):
        self.__baudRate = 115200
        self.__stopBit = 1
        self.__wordlength = 8
        self.__wordparity = "N"
        self.__timeout = 600/self.__baudRate
        self.__bytesToRead = 1
