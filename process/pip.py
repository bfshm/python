from multiprocessing import Process, Pipe

def receiver(recv_pip):
    while True:
        try:
            res = recv_pip.recv()
            print('recv:', res)
        except EOFError:
            break

if __name__ == '__main__':
    print('start')
    send_pip, recv_pip = Pipe()
    proc_recv = Process(target=receiver, args=(recv_pip, ))
    proc_recv.start()

    for i in range(1,5):
        send_pip.send(i)
        print('send:', i)
    send_pip.close()

    proc_recv.join()
    print('end')