num = int(input("enter the number:"))
if num < 0:
    print("number is  negative")
elif (num > 0):
    if (num <= 10):
        print("number is between 1-10")
    elif (num > 10 and num <= 20):
        print("number is bwtween 11-20")
    else:
        print("number is greater than 20")
else:
    print("number is zero")