#walrus operator
a = True
print(a:=False)

numbers = [1,2,3,4,5]

while(n:= len(numbers))>0:
    print(numbers.pop())

# assigns values to variables as part of a larger expression
foods = list()
#normal
# while True:
#     food = input("what food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)
#walrus using
foods = list()
while(food:=input("what food do you like:")) !="quit":
    foods.append(food)