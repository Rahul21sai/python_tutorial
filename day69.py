class employee:
    company = "apple"
    def show(self):
        print(f"the name is {self.name} and company is{self.company}")
    @classmethod
    def changecompany(cls,newcompany):
        cls.company = newcompany


e1 = employee()
e1.name = "rahul"
e1.show()
e1.changecompany("tesla")
e1.show()
print(employee.company)

