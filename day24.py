#tuples-unchangeable

tup = (1,33,43,"rahul",True,3744,24,245,35245,0)
print(tup,type(tup),len(tup))
print(tup[0])
print(tup[4])
print(tup[8])
print(tup[-1])
#check an item
if 23 in tup:
    print("yes it is present in tuple")

# when slicing a new tuple will be formed from the old tupple
tup2 = tup[1:6]
print(tup2)
print(tup[5:])
print(tup[:10])
print(tup[:-1])
print(tup[:-1:2])