import threading
import time
import Controller.IController as IController


class ConsumerThread(threading.Thread):
    def __init__(self, name=None, args=()):
        super(ConsumerThread, self).__init__()
        self.name = name
        return

    def run(self):
        while True:
            print('Getting ' + str(IController.getInstance().get100HzData()) +
                  ' from 100Hz buffered queue\n')
            print('Getting ' + str(IController.getInstance().get10HzData()) +
                  ' from 10Hz buffered queue\n')
            print('Getting ' + str(IController.getInstance().get4HzData()) +
                  ' from 14Hz buffered queue\n')
            time.sleep(1/60)
        return
