import queue
import IController
class Manager:
    def consume(self):
        print('Getting ' + str(Icontroller.getInstance().get100HzData())+ ' from 100Hz buffered queue\n')
        print('Getting ' + str(Icontroller.getInstance().get10HzData())+ ' from 10Hz buffered queue\n')
        print('Getting ' + str(Icontroller.getInstance().get4HzData())+ ' from 14Hz buffered queue\n')
    #UNUSED    
    def list(self):
        print('Getting ' + str(IContoller.getInstance().list100()) + ' \n')
        print('Getting ' + str(IContoller.getInstance().list10()) + ' \n')
        print('Getting ' + str(IContoller.getInstance().list4()) + ' \n')
    def shutdown(self):
        self.w.shutdown()
    def restart(self):
        self.w.restart()