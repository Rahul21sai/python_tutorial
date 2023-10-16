import threading
import time

#indicates some task being dome

def func(seconds):
    print(f"sleeping for {seconds} seconds")
    time.sleep(seconds)
#normal code
# func(4)
# func(3)
# func(1)

#code using threads
t1 = threading.Thread(target=func, args=[4])
t2 = threading.Thread(target=func, args=[3])
t3 = threading.Thread(target=func, args=[1])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()