#multilevel inheritence


class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def show(self):
        print(f"name:{self.name}")
        print(f"species:{self.species}")

class dog(animal):
    def __init__(self,name,bread):
        animal.__init__(self,name,species="dog")
        self.bread = bread

    def show(self):
        animal.show(self)
        print(f"breed:{self.bread}")

class goldenretriever(dog):
    def __init__(self,name,color):
        dog.__init__(self,name,bread="golden retriever")
        self.color = color

    def show(self):
        dog.show(self)
        print(f"color:{self.color}")


o =goldenretriever("tommy","black")
o.show()
print(goldenretriever.mro())
