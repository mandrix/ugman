class Parent:

    def __init__(self):
        self.vida = 100



class Child(Parent):

    def __init__(self, arm):
        super().__init__()
        self.arm = arm

prueba = Child(1)

print (prueba.vida)