#hybrid inheritence -combo of multipule and single inheritence

class baseclass:
    pass
class derived1(baseclass):
    pass

class derived2(baseclass):
    pass

class derived3(derived1,derived2):
    pass

#hierarchical inheritence

class baseclass1:
    pass
class d1(baseclass):
    pass
class d2(baseclass):
    pass

class d3(d1):
    pass
