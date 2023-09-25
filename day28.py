letter = "hey my name is {} and i am from {}"
country = "india"
name = "raahul"

print(letter.format(name,country))

#fstring
print(f"hey my name is {name} and i am from {country}")

price = 49.0999
txt = f"for only {price:.2f} dollars!"
print(txt)
print(type(f"{2 * 30}"))
