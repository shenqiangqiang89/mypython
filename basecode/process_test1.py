from multiprocessing import process,queues

def write(q):
    q.put(1)