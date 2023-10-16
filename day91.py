def my_generator():
    for i in range(5000):
        yield i

gen = my_generator()
print(next(gen))

for j in gen:
    print(j)