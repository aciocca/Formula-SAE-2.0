import multiprocessing

def main(FilePipeFileEnd):
	print("hi i'm fh")
	while True:
		print('fh recieved a ' + str(FilePipeFileEnd.recv()))