# set - doesn't take the repeated values & once created it cannot be changable
s = {2, 4, 2, 6}
print(s)

info = {
    "rahul", 19, False, 6.9, 19
}
print(info)  # they donot maintain any order

rahul = set()
print(type(rahul))

for vlue in info:
    print(vlue)