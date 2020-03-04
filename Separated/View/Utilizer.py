import Controller.Manager as Manager


def runUtil():
    manager = Manager.Manager()
    while True:
        comand = input("Inserisci la lettera C /o/ c per consumare, F /o/ f per vedere la lista e T per terminare:\n")
        if comand == "C" or comand == "c":
            manager.consume()
        elif comand == "F" or comand == "f":
            manager.list()
        elif comand == "T" or comand == "t":
            manager.shutdown()
# TODO: fare 3 code per le 3 frequenze da trasferire
#  in 3 liste per dare dati medi
