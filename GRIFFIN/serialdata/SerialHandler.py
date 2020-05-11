import serial
from time import sleep
from multiprocessing import Process, Pipe

#Routine che apre la connessione alla seriale e attraverso una pipe li spedisce al format data#
def subProcessFunction(obj):
    obj.openPort()

    while True:
        pipeOutput = obj.readData(startChar = b'\x02', endChar=b'\x03')
        # add logs
        obj.sh_fh_pipe.send(pipeOutput)
        sleep(0.01)

    obj.closePort()

class SerialHandler:

    __doc__='''Documentation for SerialHandler.py functions:

-__init__(name, baudrate, **kwargs):
    -stopBit
    -length = dataFrame length in bit (5, 6, 7, 8)
    -parity = 'E', 'O', 'N'
    -timeout = max Timeout in reading
    -bytesToRead = Bytes to read from serial

-openPort():
    open the serial port and start communication

-closePort():
    close the communication and the serial port

-readData(**kwargs):
    read the data and return bytes with the read values, or b'ErrorReading' in case of failure
    -size = Bytes to read only once
    -startChar = byte that represent the start char for the sequence
        WARNING the start char will not be included in return bytes sequence

-getInfo():
    return the dictionary with the settings for the serial port

-clear(): 
    clear the input buffer
    
@classmethod
scanCOMs():
    return a list that contains the available ports (WORKS ONLY WITH WINDOWS O.S.)'''

    def __init__(self, name, baudrate, sh_fh_pipe,**kwargs):
        self.__portName=name
        self.__baudRate=baudrate

        if "stopBit" in kwargs.keys():
            self.__stopBit = kwargs["stopBit"]
        else:
            self.__stopBit=1

        if "length" in kwargs.keys():
            self.__wordLength=kwargs["length"]
        else:
            self.__wordLength=8
            
        if "parity" in kwargs.keys():
            self.__wordParity=kwargs["parity"]
        else:
            self.__wordParity='N'

        if "timeout" in kwargs.keys():
            self.__timeout=kwargs["timeout"]
        else:
            self.__timeout=5
        
        if "bytesToRead" in kwargs.keys():
            self.__bytesToRead=kwargs["bytesToRead"]
        else:
            self.__bytesToRead=1

        self.__serialInstance = serial.Serial(port=self.__portName, baudrate=self.__baudRate, bytesize=self.__wordLength, parity=self.__wordParity, stopbits=self.__stopBit, timeout=self.__timeout)
        self.__serialInstance.close()

        self.sh_fh_pipe = sh_fh_pipe
      
    def run(self):
        self.p = Process(target=subProcessFunction, args=(self,))
        self.p.start()
    
    def join(self):
        self.p.join()

    def readData(self, **kwargs):
        messageRead = bytes()
        if "size" in kwargs.keys():
            bytesToRead = kwargs["size"]
        else:
            bytesToRead = self.__bytesToRead

        if "startChar" in kwargs.keys() and "endChar" in kwargs.keys():
            attempt=0
            startChar = kwargs["startChar"]
            while True:
                charReceived = self.__serialInstance.read(size=1)
                if charReceived == startChar:
                    charReceived = self.__serialInstance.read(size=1)
                    while charReceived != kwargs["endChar"]:
                        messageRead+=charReceived
                        charReceived=self.__serialInstance.read(size=1)
                    if charReceived==kwargs["endChar"]:
                        break
                elif attempt>=200:
                    if len(messageRead) > 0:
                        if messageRead[0] == bytes([0x3F]):
                            return messageRead[0] + b'ReadError'
                        else:
                            return b'ReadError'
                    else:
                        return b'ReadError'
                else:
                    attempt+=1
        
        elif "startChar" in kwargs.keys() and not "endChar" in kwargs.keys():
            attempt=0
            startChar = kwargs["startChar"]
            while True:
                charReceived = self.__serialInstance.read(size=1)
                if charReceived == startChar:
                    for i in range(0, bytesToRead):
                        messageRead+=(self.__serialInstance.read(1))
                    break
                elif attempt>=bytesToRead:
                    return b'ReadError'           
                else:
                    attempt+=1

        else:
            for i in range(0, bytesToRead):
                messageRead+=(self.__serialInstance.read(1))
        
        return messageRead
    
    def writeData(self, **kwargs):
        if "byte" in kwargs.keys():
            self.__serialInstance.write(kwargs["byte"])
        else:
            self.__serialInstance.write(b'\x01')
        self.__serialInstance.flush()

    def getInfo(self):
        return self.__serialInstance.get_settings()

    def openPort(self):
        self.__serialInstance.open()
        sleep(2)

    def closePort(self):
        self.__serialInstance.close()


    #TO-DO: scanCOMs works also for Linux O.S.
    #Method to list ALL the Serial ports (ONLY FOR WINDOWS)
    @classmethod
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
        # portList.append("/dev/ttyACM0") # under linux there aren't COM serial
        return portList