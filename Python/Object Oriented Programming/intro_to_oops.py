class Dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
    
    def bark(self):
        print(f"{self.breed} is barking!")

dog1 = Dog("Golden Retriever", "Golden")
dog2 = Dog("Bulldog", "White")

dog1.bark();
dog2.bark();