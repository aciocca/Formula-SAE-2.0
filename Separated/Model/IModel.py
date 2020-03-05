class IModel:
    __instance = None

    @staticmethod
    def getInstance():
        # Static access method.
        if IModel.__instance is None:
            IModel()
        return IModel.__instance
    
    def startThread(self):
        self.w = Writer.WriterThread(name="Stocazzo", instance=self.myInstance)
        self.w.start()       