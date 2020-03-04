import threading
import serial


class WriterThread(threading.Thread):
    def __init__(self, name, instance):
        super(WriterThread, self).__init__()
        self.name = name
        self.instance = instance
        self.ser = serial.Serial('COM12', 19200, timeout=1)
        if self.ser.is_open:
            print("Serial is opened")
            self.loop = True

    def run(self):
        print("opened")
        with open("testWriter.txt", "a+") as file:
            while(self.loop):
                item = int.from_bytes(self.ser.readline(1), "big")
                if item is not None:
                    file.write("Appended line %d\n" % item)
                    self.instance.getInstance().add100HzData(item)
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
