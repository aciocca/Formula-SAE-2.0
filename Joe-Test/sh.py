import multiprocessing
import time
import sys

def main(GuiPipeSerialEnd, FilePipeSerialEnd):
	print("hi i'm sh")
	sys.stdout.flush()
	# while True:
	# 	print('sh sending 1 to gui')
	# 	GuiPipeSerialEnd.send(1)
	# 	print('sh sending 1 to fh')
	# 	FilePipeSerialEnd.send(1)

	# 	time.sleep(0.5)

	# 	print('sh sending 2 to gui')
	# 	GuiPipeSerialEnd.send(2)
	# 	print('sh sending 2 to fh')
	# 	FilePipeSerialEnd.send(2)
	
		# time.sleep(1)
	# for i in range(1000):
	# 	if i == 100:
	# 		pass
	# 	else:
	# 		# print('s '+ str(i))
	# 		GuiPipeSerialEnd.send(i)
	# 	time.sleep(0.001)

	GuiPipeSerialEnd.send(1)
	GuiPipeSerialEnd.send(2)
	GuiPipeSerialEnd.send(3)
	GuiPipeSerialEnd.send(4)
	GuiPipeSerialEnd.send(5)
	GuiPipeSerialEnd.send(6)
	GuiPipeSerialEnd.send(7)
	GuiPipeSerialEnd.send(8)
	GuiPipeSerialEnd.send(9)
	GuiPipeSerialEnd.send(10)
	GuiPipeSerialEnd.send(11)
	print('sh died')
	sys.stdout.flush()