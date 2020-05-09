import multiprocessing
import sh
import fh
import time

# LA VELOCITA' DI TRASMISSIONE CON UNA PIPE E' DI CIRCA 1MB/S

def main():
	GuiPipeGuiEnd, GuiPipeSerialEnd = multiprocessing.Pipe(duplex = False)
	FilePipeFileEnd, FilePipeSerialEnd = multiprocessing.Pipe(duplex = False)

	print('gui is here')

	shProcess = multiprocessing.Process(target=startSerialH, args=(GuiPipeSerialEnd, FilePipeSerialEnd))
	fhProcess = multiprocessing.Process(target=startFileH, args=(FilePipeFileEnd,))

	shProcess.start()
	# fhProcess.start()

	print('gui is also here')

	time.sleep(2)
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())
	print(GuiPipeGuiEnd.recv())

	# b = 0
	# while True:
	# 	a = GuiPipeGuiEnd.recv()
	# 	if (a-b>1):
	# 		print('DIOCANEDIOCANEDIOCANE')
	# 	b = a
	# 	# print('a ' + str(a))
	# 	if a==999:
	# 		break
	# print(type(a))



def startSerialH(GuiPipeSerialEnd, FilePipeSerialEnd):
	sh.main(GuiPipeSerialEnd, FilePipeSerialEnd)

def startFileH(FilePipeFileEnd):
	fh.main(FilePipeFileEnd)

if __name__ == '__main__':
	main()