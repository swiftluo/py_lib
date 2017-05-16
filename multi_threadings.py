import threading
import time


def task():
    now_time = time.time()
    print(now_time)


thread = threading.Thread(target=task)
thread.start()
