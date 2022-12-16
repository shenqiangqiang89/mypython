import threading
import time

def target():
    print(f"{threading.current_thread().ident}---{threading.current_thread().name}")
    time.sleep(1)

t = threading.Thread(target = target)
t.start()
t.join()
print("all done")