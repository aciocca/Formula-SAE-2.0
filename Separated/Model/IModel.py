import serial
from Writer import WriterThread

class IModel:
    __instance=None
    
    @staticmethod
    def getInstance(cls):
        # Static access method.
        if IModel.__instance is None:
            IModel()
        return IModel.__instance
    
    def startThread(self, serialInstance):
        self.w = WriterThread("Writer thread", serialInstance)
        self.w.start()