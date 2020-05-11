from multiprocessing import Process, Pipe

from DataFrame import DataFrame
from SerialHandler import SerialHandler as sr
from FileHandler import FileHandler

class Controller(object):
    
    def __init__(self):

        self.__df = DataFrame() # oggetto DataFrame comune

        # pipes di comunicazione tra i processi
        self.__fh_sh_pipe, self.__sh_fh_pipe = Pipe()
        self.__gui_fh_pipe, self.__fh_gui_pipe = Pipe()

        # oggetti che rappresentano la logica dei processi che andranno ad essere parallelizzati
        self.__seriale = sr(sr.scanCOMs()[0], 115200, self.__sh_fh_pipe)
        self.__fh = FileHandler(self.__df, self.__fh_sh_pipe, self.__fh_gui_pipe)

        self.__seriale.run()
        self.__fh.run()

        # self.__seriale.join()
        # self.__fh.join()

    def getGUIPipe(self):
        return self.__gui_fh_pipe