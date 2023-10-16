class employee:
    companyname = "reliance"
    noofemployee  = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        employee.noofemployee +=1
    def showdetails(self):
        print(f"the name of the employee is {self.name} and the raise amount in in {self.noofemployee} sized {self.companyname}is {self.raise_amount}")

emp1 = employee("rahul")
emp1.raise_amount = 0.3
emp1.companyname = "reliance India"
emp1.showdetails()
emp2 = employee("rohan")
emp2.companyname = "infosys"
emp2.showdetails()