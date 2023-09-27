# local variable -->that is defined with in the function and is only accesible with in that function
#global --> defined outside function and is accessible from with in any function in oyur code

x = 4
print(x)

def hello():
    global x
    x = 8
    print(f"the local x  is {x}")
    print("hello harry")
print(f"the global x is {x}")
hello()
print(f"the global variable x is {x}")