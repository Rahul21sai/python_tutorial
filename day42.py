#enumerate function
marks = [1,2,35,45,46,6567,4,3,223,4,34,344]
index = 0
for mark in marks:
    print(mark)
    if(index==3):
        print("awesome")
    index = index +1
print("program 1 end")

#its alter method is to
#using enumerate function
for index,mark in enumerate(marks):
    print(mark)
    if(index==3):
        print("rahul,awesome!")
#you change the starting of index by using (marks,1)
