from Controller import Controller

if __name__ == "__main__":

    controller = Controller()
    pipe = controller.getGUIPipe()

    while(True):

        dict100hz, dict10hz, dict4hz = pipe.recv()

        print("--------------------")
        print(dict100hz)
        print(dict10hz)
        print(dict4hz)
        print("--------------------")