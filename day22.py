l = [3,4,5,6,"rahul",True,4,87,6,7,5,56435,3,3,442,42]# we can add strings and bollean in the list-lists are changeable
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[5])
print(l[-1])
print(l[-4])

if "rahul" in l:
    print("yes")
else:
    print("no")

#range of index:
# listname[start:end:jumpindex]
print(l)
print(l[:])
print(l[1:])
print(l[1:-1])
print(l[1:-1:2])
print(l[1::4])
#lsit comprehension
lst =[i*i for i in range(10)]
print(lst)
lst =[i*i for i in range(10) if i%2==0]
print(lst)



