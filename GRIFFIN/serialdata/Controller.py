from multiprocessing import Process, Pipe
from serialdata.DataFrame import DataFrame
from serialdata.SerialHandler import SerialHandler as sr
from serialdata.FileHandler import FileHandler

class Controller(object):
    
    def __init__(self):

        self.__df = DataFrame() # oggetto DataFrame comune

        # pipes di comunicazione tra i processi

        # NOTA DALLA DOCUMENTAZIONE UFFICIALE, FINCHE ABBIAMO IN LETTURA E SCRITTURA UN SOLO PROCESSO SU OGNI END E' UN UTILIZZO PROCESS SAFE
        # Note that data in a pipe may become corrupted if two processes 
        # (or threads) try to read from or write to the same end of the pipe 
        # at the same time. Of course there is no risk of corruption from processes 
        # using different ends of the pipe at the same time.

        self.__fh_sh_pipe, self.__sh_fh_pipe = Pipe()
        self.__gui_fh_pipe, self.__fh_gui_pipe = Pipe()



    def start_serial_connection(self, serial_dict):
        # oggetti che rappresentano la logica dei processi che andranno ad essere parallelizzati
        # TODO: aggiungere altri dati da serial_dict
        # struttura serial_dict
        # connection_parameters = {"portname": self.portCombobox.get(), "baudrate": self.baudrateEntry.get(), "bytestoread": self.bytesEntry.get(),
        #                         "length": self.lengthEntry.get(), "parity": self.parityEntry.get(), "stopbit": self.sbEntry.get(), "timeout": self.timeoutEntry.get()}
        
        self.__seriale = sr(serial_dict["portname"], serial_dict["baudrate"], self.__sh_fh_pipe)
        self.__fh = FileHandler(self.__df, self.__fh_sh_pipe, self.__fh_gui_pipe)

        self.__seriale.run()
        self.__fh.run()

        # self.__seriale.join()
        # self.__fh.join()
    
    def check_avaible_ports(self):
        port_list = sr.scanCOMs()
        return port_list


    def getGUIPipe(self):
        return self.__gui_fh_pipe