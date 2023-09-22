class Mammal:
    #constructor
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

    def hunger(self):
        return f"{self.name} says I am HUNGRY"

    def speak(self):
        pass