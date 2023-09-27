#seek
with open('myfile5.txt', 'r') as f:
    print(type(f))
    #move to the 10 th byte in  the file
    f.seek(10)

    #read the next 5 bytes
    print(f.tell())
    data = f.read(5)
    print(data)

#tell returns the current position within the file in bytes
with open('sample.txt','w') as f:
    f.write('hello world3!')
    f.truncate(3)

with open('sample.txt', 'r') as f:
    print(f.read())

