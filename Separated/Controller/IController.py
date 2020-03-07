# Classe di snodo del controller che permette di ricevere dati dal
# model e inserirli in delle code (queue)
# volatili gestite da questa stessa classe
# (riempimento, richiesta dati e disponibilit�)
import queue
from Model import IModel
from time import sleep

class IController:
    __instance = None
    __serialInstance = None

    @staticmethod
    def getInstance():
        # Static access method.
        if IController.__instance is None:
            IController()
        return IController.__instance

        IModel.open
    
    @staticmethod
    def scanCOMs(cls):
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
    def openPort(cls, portName, baudRate, **kwargs):
        
        if "stopBit" in kwargs.keys():
            stopBit = kwargs["stopBit"]
        else:
            stopBit=1

        if "length" in kwargs.keys():
            wordLength=kwargs["length"]
        else:
            wordLength=8
            
        if "parity" in kwargs.keys():
            wordParity=kwargs["parity"]
        else:
            wordParity='N'

        if "timeout" in kwargs.keys():
            timeout=kwargs["timeout"]
        else:
            timeout=600/self.__baudRate
        
        if "bytesToRead" in kwargs.keys():
            bytesToRead=kwargs["bytesToRead"]
        else:
            bytesToRead=1
        
        IController.__serialInstance = serial.Serial(port=portName, baudrate=baudRate, bytesize=wordLength, parity=wordParity, stopbits=stopBit, timeout=timeout)
        IController.__serialInstance.close()
        IController.__serialInstance.open()
        sleep(2)        # to stabilize the connection
        IModel.getInstance().startThread(IController.__serialInstance)
    
    @staticmethod
    def closePort(cls):   
        IController.__serialInstance.close()        

    @staticmethod
    def getSerialInstance(cls):
        return IController.__serialInstance
        

    def initializeGlobalVariables(self):
        self.q100 = queue.Queue(self.__BUF_SIZE100)
        self.q10 = queue.Queue(self.__BUF_SIZE10)
        self.q4 = queue.Queue(self.__BUF_SIZE4)

    def __init__(self):
        # media dati 100Hz ogni 10 dati
        # media dati 10Hz ogni 10 dati
        # media dati 4Hz ogni elemento (nessuna media)
        self.__BUF_SIZE100 = 10
        self.__BUF_SIZE10 = 10
        self.__BUF_SIZE4 = 1
        self.initializeGlobalVariables()
        # Virtually private constructor.
        if IController.__instance is not None:
            print("This class is a singleton!")
        else:
            IController.__instance = self

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
        self.myInstance.getInstance()
        print('Getting ' + str(self.myInstance.get100HzData()) +
              ' from 100Hz buffered queue\n')
        print('Getting ' + str(self.myInstance.get10HzData()) +
              ' from 10Hz buffered queue\n')
        print('Getting ' + str(self.myInstance.get4HzData()) +
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