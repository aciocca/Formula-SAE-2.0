# Classe di snodo del controller che permette di ricevere dati dal
# model e inserirli in delle code (queue)
# volatili gestite da questa stessa classe
# (riempimento, richiesta dati e disponibilit�)
import queue
import serial
from Model.IModel import IModel
from time import sleep

class IController:
    __instance = None
    __serialInstance = None
    __modelInstance = None
    __stopBit = 1 
    __wordLength = 8
    __wordParity = 'N'
    __timeout = 600/115200
    __bytesToRead = 1
    __portName=""
    __baudRate=115200          #default baudrate 115200
    
    def __init__(self):
        # media dati 100Hz ogni 10 dati
        # media dati 10Hz ogni 10 dati
        # media dati 4Hz ogni elemento (nessuna media)
        self.__BUF_SIZE100 = 10
        self.__BUF_SIZE10 = 10
        self.__BUF_SIZE4 = 1
        self.initializeGlobalVariables()
        #DEBUG: CONNECTION STRING TO MODIFY
        # Virtually private constructor.
        if IController.__instance is not None:
            print("This class is a singleton!")
        else:
            IController.__instance = self

    
    @staticmethod
    def getInstance():
        # Static access method.
        print("ContInstance called")
        if IController.__instance is None:
            IController()
        return IController.__instance
    
    @staticmethod
    def scanCOMs():
        portList = []
        for i in range(255):
            try:
                portToCheck = 'COM' + str(i)
                s = serial.Serial(portToCheck)
                s.close()
                portList.append(portToCheck)
            except serial.SerialException:
                pass
        return portList

    @staticmethod
    def openPort(portName, baudRate, **kwargs):
        IController.__portName=portName
        IController.__baudRate=baudRate
        if "stopBit" in kwargs.keys():
            IController.__stopBit = kwargs["stopBit"]

        if "length" in kwargs.keys():
            IController.__wordLength=kwargs["length"]
            
        if "parity" in kwargs.keys():
            IController.__wordParity=kwargs["parity"]

        if "timeout" in kwargs.keys():
            IController.__timeout=kwargs["timeout"]
        
        if "bytesToRead" in kwargs.keys():
            IController.__bytesToRead=kwargs["bytesToRead"]
        
        IController.__serialInstance = serial.Serial(port=IController.__portName, baudrate=IController.__baudRate, bytesize=IController.__wordLength, parity=IController.__wordParity, stopbits=IController.__stopBit, timeout=IController.__timeout)
        IController.__serialInstance.close()
        IController.__serialInstance.open()
        sleep(2)        # to stabilize the connection
        IController.__modelInstance.getInstance().startThread(IController.__serialInstance)
    
    def setModelInterface(self, interface):
        IController.__modelInstance=interface
    
    def closePort(self):   
        self.__serialInstance.close()        

    def getSerialInstance(self):
        return IController.__serialInstance
       
    def getSpecs(self):         #returns connection's specs or 0 if there isn't a serial connection
        if IController.__serialInstance != None:    
            specs = {"stopBit": IController.__stopBit, "wordLength": IController.__wordLength, "wordParity": IController.__wordParity, "timeout": IController.__timeout, "bytesToRead": IController.__bytesToRead}
            return specs
        else:
            return False

    def initializeGlobalVariables(self):
        self.q100 = queue.Queue(self.__BUF_SIZE100)
        self.q10 = queue.Queue(self.__BUF_SIZE10)
        self.q4 = queue.Queue(self.__BUF_SIZE4)

    #Methods for Model Purposes

    # 100Hz methods
    def add100HzData(self, item):
        if self.q100.full():
            self.q100.get()
        self.q100.put(item)

    def q100HzFull(self):
        return self.q100.full()

    # 10Hz methods
    def add10HzData(self, item):
        if self.q10.full():
            self.q10.get()
        self.q10.put(item)

    def q10HzFull(self):
        return self.q10.full()

    # 4Hz methods

    def add4HzData(self, item):
        if self.q4.full():
            self.q4.get()
        self.q4.put(item)

    def q4HzFull(self):
        return self.q4.full()

    # debug methods: stampano i contenuti delle code

    def list100Hz(self):
        return list(self.q100.queue)

    def list10Hz(self):
        return list(self.q10.queue)

    def list4Hz(self):
        return list(self.q4.queue)
    
    # Methods for View purposes
        
    def consume(self):
        print('Getting ' + str(IController.getInstance().get100HzData()) +
              ' from 100Hz buffered queue\n')
        print('Getting ' + str(IController.getInstance().get10HzData()) +
              ' from 10Hz buffered queue\n')
        print('Getting ' + str(IController.getInstance().get4HzData()) +
              ' from 4Hz buffered queue\n')
        
    def list(self):
        print("Elements in q100:\n")
        for elem in self.list100Hz():
            print("\t"+str(elem))
        print("\nElements in q10:\n")
        for elem in self.list10Hz():
            print("\t"+str(elem))
        print("\nElements in q4:\n")
        for elem in self.list4Hz():
            print("\t"+str(elem))
        print("End printing lists\n")

    def get100HzData(self):
        # da fare la media dei primi 10 valori della queue
        data = 0
        items = 0
        if not self.q100.empty():
            # il "listing" e' un'operazione atomica quindi
            # NON DOVREBBE bloccare il thread
            for elem in list(self.q100.queue):
                data = data + elem
                items = items + 1
            quant = data/items
        else:
            quant = -1
        return quant
        
    def get10HzData(self):
        # da fare la media dei primi 10 valori della queue
        data = 0
        items = 0
        if not self.q10.empty():
            # il "listing" e' un'operazione atomica quindi NON DOVREBBE
            # bloccare il thread
            for elem in list(self.q10.queue):
                data = data + elem
                items = items + 1
            quant = data/items
        else:
            quant = -1
        return quant

    def get4HzData(self):
        # Non servono medie, do il dato esattamente come e'
        if self.q4.empty():
            item = None
        else:
            item = self.q4.get()
        return item