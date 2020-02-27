#Classe di snodo del controller che permette di ricevere dati dal model e inserirli in delle code (queue)
#volatili gestite da questa stessa classe (riempimento, richiesta dati e disponibilitÓ)
class IController:
    __instance = None
    @staticmethod 
    def getInstance():
        #Static access method.
        if IController.__instance == None:
            IController()
        return IController.__instance
    def __init__(self):
        #media dati 100Hz ogni 10 dati
        #media dati 10Hz ogni 10 dati
        #media dati 4Hz ogni elemento (nessuna media)
        self.BUF_SIZE100=10
        self.BUF_SIZE10=10
        self.BUF_SIZE4=1
        #Virtually private constructor.
        if IController.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            IController.__instance = self
    def initializeGlobalVariables(master):
        self.q100=queue.Queue(BUF_SIZE100)
        self.q10=queue.Queue(BUF_SIZE10)
        self.q4=queue.Queue(BUF_SIZE4)
    #100Hz methods
    def add100HzData(self,item):
        if self.q100.full():
            self.q100.get()
        self.q100.put(item)
    def get100HzData(self):
        #da fare la media dei primi 10 valori della queue
        data=0
        items=0
        if not self.q100.empty():
            #il "listing" e' un'operazione atomica quindi NON DOVREBBE bloccare il thread
            for elem in list(self.q100.queue):
                data=data+elem
                items=items+1
        return (data/items)
    def q100HzFull(self):
        return self.q100.full()
    #10Hz methods
    def add10HzData(self,item):
        if self.q10.full():
            self.q10.get()
        self.q10.put(item)
    def get10HzData(self):
        #da fare la media dei primi 10 valori della queue
        data=0
        items=0
        if not self.q100.empty():
            #il "listing" e' un'operazione atomica quindi NON DOVREBBE bloccare il thread
            for elem in list(self.q10.queue):
                data=data+elem
                items=items+1
        return (data/items)
    def q10HzFull(self):
        return self.q10.full()
    #4Hz methods
    def add4HzData(self,item):
        if self.q4.full():
            self.q4.get()
        self.q4.put(item)
    def get4HzData(self):
        #Non servono medie, do il dato esattamente come e'
        if self.q4.empty():
            item=None
        else:
            item=self.q4.get()
        return item
    def q4HzFull(self):
        return self.q4.full()
    #debug methods: stampano i contenuti delle code
    def list100Hz(self):
        return list(self.q100.queue)
    def list10Hz(self):
        return list(self.q10.queue)
    def list4Hz(self):
        return list(self.q4.queue)