#access modifier

# public access modifier
class employee():
    def __init__(self):
        self.name = "rahul"
        self.__name1 = "rahul2" # private
        self._name2 = "rahul3"#protected
a = employee()
print(a.name)# cannot br accessed directly
print(a._employee__name1)# can be accessed indirectly
# using name mangling
print(a._name2)
print(a.__dir__())# what are the methods are applied for the a

#protected
