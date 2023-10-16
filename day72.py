class parentclass:
    def parentmethod(self):
        print("this is parent method")

class childclass(parentclass):
    def parentmethod(self):
        print("rahul")
        super().parentmethod()
    def childmethod(self):
        print("this is child method")
        super().parentmethod()

childobject = childclass()
childobject.childmethod()
childobject.parentmethod()

#super __init__

class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class programmer(employee):
    def __init__(self,name,id, lang):
        super().__init__(name,id)
        self.lang = lang

rohan = employee("rohandas","420")
rahul = programmer("rahul","23450","python")
print(rohan.name,rohan.id)
print(rahul.id,rahul.name,rahul.lang)
