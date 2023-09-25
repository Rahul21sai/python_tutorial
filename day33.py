dic = {
    1:"rahul",
    2:"shubham",
    3:"zakir",
    4:"neha"
}
print(dic[1])
print(dic[2])
print(dic.get(3))#if vaalue not there it print none
print(dic.keys())#used to print the all keys in the dic.

# for values you can
for key in dic.keys():
    print(f"the value corresponding to the key{key} is {dic[key]}")
print(dic.values())
print(dic.items())
for key,value in dic.items():
    print(f"the value corresponding to the key{key} is {value}")