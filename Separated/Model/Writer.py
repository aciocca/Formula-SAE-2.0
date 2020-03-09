import threading
import serial


class WriterThread(threading.Thread):
    def __init__(self, name, ser):
        super(WriterThread, self).__init__()
        self.name = name
        self.ser =ser
        if self.ser.is_open:
            print("Serial is opened")
            self.loop = True

    def readData(self, **kwargs):
        specs = IController.getSpecs()
        if specs != False:
            serialInstance = IController.getSerialInstance()
            messageRead = bytes()
            if "size" in kwargs.keys():
                bytesToRead = kwargs["size"]
            else:
                bytesToRead = specs["bytesToRead"]
            
            if "startChar" in kwargs.keys() and not "endChar" in kwargs.keys():
                attempt=0
                startChar = kwargs["startChar"]
                while True:
                    charReceived = serialInstance.read(size=1)
                    if charReceived == startChar:
                        for i in range(0, bytesToRead):
                            messageRead+=(serialInstance.read(1))
                        break
                    elif attempt>=bytesToRead:
                        return b'ErrorReading'           
                    else:
                        attempt+=1

            elif "startChar" in kwargs.keys() and "endChar" in kwargs.keys():
                attempt=0
                startChar = kwargs["startChar"]
                while True:
                    charReceived = serialInstance.read(size=1)
                    if charReceived == startChar:
                        charReceived = serialInstance.read(size=1)
                        while charReceived != kwargs["endChar"]:
                            messageRead+=charReceived
                            charReceived = serialInstance.read(size=1)
                        if charReceived==kwargs["endChar"]:
                            break
                    elif attempt>=200:
                    return b'ErrorReading'
                    else:
                        attempt+=1
            else:
                for i in range(0, bytesToRead):
                    messageRead+=(serialInstance.read(1))
            
            return messageRead

    def run(self):
        print("opened")
        with open("testWriter.txt", "a+") as file:
            while(self.loop):
                item = int.from_bytes(self.ser.readline(1), "big")
                if item is not None:
                    file.write("Appended line %d\n" % item)
                    IController.getInstance().add100HzData(item)
                    self.instance.getInstance().add10HzData(item)
                    self.instance.getInstance().add4HzData(item)
        return

    def shutdown(self):
        self.loop = False

    def restart(self):
        self.loop = True
        self.run()

    def ping(self):
        self.run(once=True)
