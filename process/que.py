from multiprocessing import Process, Queue

def producer(que):
    print()
def comsumer(que):
    print()

if __name__ == '__main__':
    print('start')
    que = Queue()
    pro_producer = Process(target=producer, args=(que,))
    pro_comsumer = Process(target=comsumer, args=(que,))
    pro_producer.start()
    pro_comsumer.start()
    pro_producer.join()
    pro_comsumer.join()