a= "Rahul !!!Rahul"
print(len(a))
#upper case
#string methods
# strings are immutable
print(a.upper())
print(a.lower())
#rstrip ->removes trailing chracters
print(a.rstrip("!"))
print(a.replace("Rahul","rohith"))
print(a.split(" "))

blog = "introduction to Js"
print(blog.capitalize())

#center -> aligns the string to the center as per the parameters given by the user
str1 = "welcome to the Console!!!"
print(str1.center(50,"."))
print(a.count("Rahul"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4,10))
str1 = "He's name is dan. he is an honest man."
print(str1.find("is"))
# print(str1.index("ishh"))#similar to find but shows an exception
str1="welcometothe console"
print(str1.isalnum())
print(str1.islower())
print(str1.isprintable())
str2="    "#using space bar
print(str2.isspace())
sttr="World Health"
print(sttr.istitle())
print(sttr.startswith("World"))
print(sttr.swapcase())
print(str1.title())