 # Map

# noermal merhtod
def cube(x):
    return x *x*x

print(cube(2))

l = [1,2,5,6,8]
# newl =[]
# for item in l:
#     newl.append(cube(item))
# print(newl) old method we use map to get

newl = list(map(cube,l))
print(newl)
#filter
def filter_function(a):
    return a >2
newnewl = list(filter(filter_function,l))
print(newnewl)

# reduce
from functools import reduce
numbers =[1,2,3,4,5]
# calculate the sum of the numbers using the reduce function
def mysum(x,y):
    return x + y
sum = reduce(mysum,numbers)
print(sum)