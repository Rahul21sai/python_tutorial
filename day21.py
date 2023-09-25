# def average(a=4,b=6):#default argumnets
#     print("average is :",(a+b)/2)
# average()
#
# average(b=8)
#
# def name(fname, mname="john",lname="whatson"):
#     print("hello,",fname,mname,lname)
#
# name("amy",)
#
# average(b=8,a=10)#keyword arguments
def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("average is :", sum/len(numbers))
    return sum/len(numbers)
average(5,6,5,4)
c=average(5,6,5,4)
print(c)


def name(**name):
    print("hello," ,name["fname"],name["mname"],name["lname"])

name(mname="buchanan",lname = "baranes",fname="james")

