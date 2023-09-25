

def fun1():

  try:
    l = [1,3,4,5,6]
    i = int(input("enter the index:"))
    print(l[i])
    return 1
  except:
    print("some error occured")
    return 0
  finally:
    print("i am always excuted")
x = fun1()
print(x)


