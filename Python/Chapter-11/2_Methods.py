class Animal:
    animalNos = 1
    def __init__(self, name, noOflegs):
        self.noOflegs = noOflegs
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

    @classmethod #Class method to access class variable
    def number_of_animals(cls, newCount):
        cls.animalNos = newCount
        return cls.animalNos
    
    @property
    def get_legs(self): #Property decorator to access method like an attribute
        return self.noOflegs

    @name.setter
    def name(self, newName): #Setter to set the value of a private attribute
        self._name = newName

class Dog(Animal):
    def __init__(self, name, breed, noOflegs):
        super().__init__(name, noOflegs)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks")

my_dog = Dog("Buddy", "Golden Retriever",4)

my_dog.speak()       
print(my_dog.breed) 
print(my_dog.number_of_animals(5))
print(my_dog.get_legs)
