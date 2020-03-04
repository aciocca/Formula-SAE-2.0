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

    def list(self):
        print("Elements in q100:\n")
        for elem in self.myInstance.list100Hz():
            print("\t"+str(elem))
        print("\nElements in q10:\n")
        for elem in self.myInstance.list10Hz():
            print("\t"+str(elem))
        print("\nElements in q4:\n")
        for elem in self.myInstance.list4Hz():
            print("\t"+str(elem))
        print("End printing lists\n")

    def shutdown(self):
        print("Uninplemented yet.\n")
