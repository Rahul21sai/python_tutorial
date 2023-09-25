#recursion

def factorial(n):
     if n==0 | n ==1:
         return 1
     else:
         return n * factorial(n-1)
print(factorial(3))
print(factorial(5))
print(factorial(7))



def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n = int(input("enter the input number:"))
for n in range(0,n):
   print(fibonacci(n))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(4))



