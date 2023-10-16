# classes and objects
class person:
    name = "rahul"
    occ = "student"
    networth = 0
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = person() #object
b = person()
a.name = "shunbham"
a.occ = "accountant"
b.name = "nikitha"
b.occ = "HR"
a.info()
b.info()
c = person()
c.info()
