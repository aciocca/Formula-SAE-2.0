from Controller import IController

class Manager:
    def consume(self):
        myController = IController.IController()
        myInstance = myController.getInstance()
        print('Getting ' + str(myInstance.get100HzData()) + ' from 100Hz buffered queue\n')
        print('Getting ' + str(myInstance.get10HzData()) + ' from 10Hz buffered queue\n')
        print('Getting ' + str(myInstance.get4HzData()) + ' from 4Hz buffered queue\n')

    def list(self):
        print('Getting ' + str(IController.getInstance().list100()) + ' \n')
        print('Getting ' + str(IController.getInstance().list10()) + ' \n')
        print('Getting ' + str(IController.getInstance().list4()) + ' \n')
