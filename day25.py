# note#if you want to add ,remove,or change the tuple items then you must covert thr tuple to a list,then perform
# operation on list and convert back to tuple

countries = ("spain", "italy", "india")
temp = list(countries)
temp.append("russia")
temp.pop(2)
temp[1] = "finland"
countries = tuple(temp)
print(countries)

# we can directly concatenate two tuples
countries2 = ("europe", "usa", "austral")
southasia = countries2 + countries
print(southasia)
# count


tup = (1,2,2,2, 33, 2, 2, 2, 2, 243, "rahul", True, 3744, 24, 24, 24, 23, 245, 35245, 0)
res = tup.count(2)
print(res)
# index first occurrence
# tuple.index(element,start,end)
res = tup.index(2)
res1 = tup.index(2,4,9)
print(res1)

print("rahul"*4)



