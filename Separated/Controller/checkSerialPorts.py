from serial.tools import list_ports
x = list_ports.comports()
for elem in x:
    print(elem)