from Controller import IController
from Model import IModel
class Main:
    
    controllerInterface=IController.IController()
    modelInterface=IModel.IModel()
    while True:
        comand = input("Inserisci la lettera C /o/ c per consumare, F /o/ f per vedere la lista:\n")
        if comand == "C" or comand == "c":
            controllerInterface.getInstance().consume()
        elif comand == "F" or comand == "f":
            controllerInterface.getInstance().list()