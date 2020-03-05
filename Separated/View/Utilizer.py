from Controller import IController
def runUtil():
    while True:
        interface=IController.IController()
        comand = input("Inserisci la lettera C /o/ c per consumare, F /o/ f per vedere la lista:\n")
        if comand == "C" or comand == "c":
            interface.getInstance().consume()
        elif comand == "F" or comand == "f":
            interface.getInstance().list()
# TODO: fare 3 code per le 3 frequenze da trasferire
#  in 3 liste per dare dati medi
