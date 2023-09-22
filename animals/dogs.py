import animals.mammal as ml

class Dog(ml):
    #constructor
    def __init__(self,name,age,color,breed):
        super().__init__(name,age,color)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} says Bark!"
    
    def hunger(self):
        pass

