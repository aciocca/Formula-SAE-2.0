from multiprocessing import Process, Pipe
import time

def f1(conn):
    print("invio...")
    conn.send({"adsa":12123, "sd": 212})
    print("invio...")
    conn.send([42, None, 'hello'])
    print("invio...")
    conn.send([42, None, 'hello'])
    conn.close()

def f2(conn):
    print(conn.recv()["adsa"])
    time.sleep(3)
    print(conn.recv())
    time.sleep(7)
    print(conn.recv())

    conn.close()

if __name__ == '__main__':
    in_, out_ = Pipe()
    p1 = Process(target=f1, args=(out_,))
    p1.start()
    
    p2 = Process(target=f2, args=(in_,))
    p2.start()

    p1.join()
    p2.join()