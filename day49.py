#
# reading the file
# f = open('myfile.txt','r')
# # print(f)
#
# text = f.read()
# print(text)
# f.close()

#writing the file
f = open('myfile.txt','w')
f.write('hello wrold!')
f.close()
f = open('myfile2.txt','w')

with open('myfile2.txt','a'):
    f.write("hey i am inside with")