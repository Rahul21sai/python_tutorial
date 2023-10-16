class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num +n # these are instance of the class

# these is static method not associated with any instance or class
    @staticmethod
    def add(a,b):
        return a +b

a = Math(5)
print(a.add(5,6))



