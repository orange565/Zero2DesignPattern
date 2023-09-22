import animals.mammal as ml

class Cat(ml):
    def __init__(self,name,age,color,breed):
        super().__init__(name,age,color)
        self.breed = breed
    
    def speak(self):
        return f"{self.name} says Meow!"
    
    def hunger(self):
        pass
