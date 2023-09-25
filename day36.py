#exception handling in python using try method
#same as try and catch in java

a = input("enter the number:")
print(f"multiplication table of {a}is:")
try:
    for i in range(1,11):
        print(f"{int(a)}X {i} = {int(a)*i}")
except Exception as e:
    print(e)
    print("invalid I")
print('some lines of code')
print("end of the program")



try:
    num = int(input("enter an integer"))
    a = [6,3]
    print(a[num])
except ValueError as e:
    print(e)
    print("number entered is not an integer")
except IndexError as e:
    print(e)
    print("index error")
