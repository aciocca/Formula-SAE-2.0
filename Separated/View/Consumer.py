import threading
import queue
from Controller.IController import IController
import time
class ConsumerThread(threading.Thread):
    def __init__(self, name=None,args=()):
        super(ConsumerThread,self).__init__()
        self.name = name
        return
    def run(self):
        while True:
            print('Getting ' + str(Icontroller.getInstance().get100HzData())+ ' from 100Hz buffered queue\n')
            print('Getting ' + str(Icontroller.getInstance().get10HzData())+ ' from 10Hz buffered queue\n')
            print('Getting ' + str(Icontroller.getInstance().get4HzData())+ ' from 14Hz buffered queue\n')
            time.sleep(1/60)
        return