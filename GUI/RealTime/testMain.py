from DataFrame import DataFrame
from SerialHandler import SerialHandler as sr
from FileHandler import FileHandler
from multiprocessing import Process, Pipe



if __name__ == "__main__":
    print("INIZIO PROGRAMMA")
    lista = []

    #Creo 3 threads, avvio threads, join ai thread.
    fh_sh_pipe, sh_fh_pipe = Pipe()
    gui_fh_pipe, fh_gui_pipe = Pipe()

    seriale = sr(sr.scanCOMs()[0], 115200, sh_fh_pipe)
    df = DataFrame()
    fh = FileHandler(df, fh_sh_pipe, fh_gui_pipe)

    #seriale.run()
    fh.run()

    #seriale.join()
    fh.join()


    print("FINE PROGRAMMA")