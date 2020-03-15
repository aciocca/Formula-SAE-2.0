from DataFrame import DataFrame
from SerialHandler import SerialHandler as sr
from FormatData import FormatData as fd
from FileHandler import FileHandler

print("INIZIO PROGRAMMA")
lista = []
df = DataFrame()
fh = FileHandler(df)
seriale = sr(sr.scanCOMs()[0], 115200)
seriale.openPort()
i = 0
while True:
    a = seriale.readData(startChar = b'\x02', endChar=b'\x03')
    lista.append(a)
    fd.setData(df, lista[i], fh)
    i = i+1
    
seriale.closePort()

print("FINE PROGRAMMA")