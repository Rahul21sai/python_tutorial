import absl.logging


class person:
    def __init__(self,n,o):#it is a constructor
      print("hey i a person")
      self.name = n
      self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a= person("rahul","student")
a.info()

#default constructor
class details:
    def __init__(self):
        print("animal")
object1=details()