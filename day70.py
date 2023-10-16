# a = "rahul-12-python"
# print(a.split("-")) split function is used to get the list

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])

e1 = employee("rahul",12000)
print(e1.name)
print(e1.salary)

string = "john-12000"
e2 = employee.fromStr(string)
# e2 = employee(string.split("-")[0],string.split("-")[1])
print(e2.name,e2.salary)
