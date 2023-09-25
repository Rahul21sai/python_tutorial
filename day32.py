s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)
#single item use add
s1.add(6)
#remove()/discard to remove the elements
s1.remove(3)
print(s1)
s3 = s1.pop()
print(s3)
# del s1
# print(s1)
s1.clear()
print(s1)