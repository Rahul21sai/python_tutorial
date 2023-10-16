# single inheritence

class animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("sound made by the animal")

class Dog(animal):
    def __init__(self,name,bread):
        animal.__init__(self,name,species="dog")

    def make_sound(self):
        print("bark")

d = Dog("dog","doggerman")
d.make_sound()

a = animal("dog","dog")
a.make_sound()

