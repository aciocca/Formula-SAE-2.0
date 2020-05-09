from multiprocessing import Process, Pipe

from DataFrame import DataFrame
from SerialHandler import SerialHandler as sr
from FileHandler import FileHandler

if __name__ == "__main__":
    print("INIZIO PROGRAMMA")
    
    df = DataFrame() # oggetto DataFrame comune

    # pipes di comunicazione tra i processi
    fh_sh_pipe, sh_fh_pipe = Pipe()
    gui_fh_pipe, fh_gui_pipe = Pipe()

    # oggetti che rappresentano la logica dei processi che andranno ad essere parallelizzati
    seriale = sr(sr.scanCOMs()[0], 115200, sh_fh_pipe)
    fh = FileHandler(df, fh_sh_pipe, fh_gui_pipe)

    seriale.run()
    fh.run()

    seriale.join()
    fh.join()

    print("FINE PROGRAMMA")