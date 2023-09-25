for i in range(1,20):
    if(i==11):
        break
    print("5 X",i,"=",5*i)
print("5 table is printed")

for i in range(1,20):
    if(i==10):
        print("skip the iteration")
        continue
    print("5 X",i,"=",5*i)
print("5 table is printed")


i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break


