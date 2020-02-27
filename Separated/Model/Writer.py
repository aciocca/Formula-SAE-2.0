import threading
import random
import serial
from Controller.IController import IController
class WriterThread(threading.Thread):
    def __init__(self,name):
        super(WriterThread,self).__init__()
        self.name = name
        self.q=queue
        self.ser = serial.Serial('COM3', 19200, timeout=1)
        if self.ser.is_open==True:
            print("Serial is opened")
            self.loop=True
    def run(self):
        print("opened")
        with open("testWriter.txt","a+") as file:
            while (self.loop):
                item = int.from_bytes(self.ser.readline(1),"big")
                if item!=None:
                    file.write("Appended line %d\n" % item)
                    IController.getInstance().add100HzData(item)
                    IController.getInstance().add10HzData(item)
                    IController.getInstance().add4HzData(item)
        return
    def shutdown(self):
        self.loop=False
    def restart(self):
        self.loop=True
        self.run()
    def ping(self):
        self.run(once=True)
        