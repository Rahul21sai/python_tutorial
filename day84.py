import time


def usingwhile():
    i = 0
    while i<5000:
        i = i+1
        print(i)
def usingfor():
    for i in range(5000):
        print(i)


init = time.time()
usingfor()
t1= time.time()-init
init = time.time()
usingwhile()
print(time.time()-init)
print(t1)

print(4)
time.sleep(3)
print("this is printed after 3 seconds")

t = time.localtime()
f = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(f)