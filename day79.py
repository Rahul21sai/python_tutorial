# multiple inhertence

class employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"the name is{self.name}")

class dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"the dance is {self.dance}")

class danceremployee(dancer,employee):
    def __init__(self,name,dance):
        self.dance = dance
        self.name = name

o = danceremployee("rahul","dancer")
print(o.dance,o.name)
o.show()

print(danceremployee.mro()) #the python finds which method comes first

