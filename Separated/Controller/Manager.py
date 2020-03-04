from Controller import IController
from Model import Writer


class Manager:
    def __init__(self):
        myController = IController.IController()
        self.myInstance = myController.getInstance()
        self.w = Writer.WriterThread(name="Stocazzo", instance=self.myInstance)
        self.w.start()

    def consume(self):
        self.myInstance.getInstance()
        print('Getting ' + str(self.myInstance.get100HzData()) +
              ' from 100Hz buffered queue\n')
        print('Getting ' + str(self.myInstance.get10HzData()) +
              ' from 10Hz buffered queue\n')
        print('Getting ' + str(self.myInstance.get4HzData()) +
              ' from 4Hz buffered queue\n')
