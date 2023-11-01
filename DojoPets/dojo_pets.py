class Pet:
    def __init__(self, name, type, tricks, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 45
        self.health = 400
        self.sound = sound
    
    def __repr__(self):
        display = f"{self.name}, Type: {self.type}, Tricks: {self.tricks}, Energy: {self.energy}, Health: {self.health}, Noise: {self.sound}"
        return display

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10 
        return self  

    def play(self):
        self.health += 5 
        return self

    def noise(self):
        print(self.sound)

pet1 = Pet("Trik", "Husky", "Rollover", "Howl")

class Ninja:
    def __init__(self, first_name, last_name , treats , pet_food , pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def __repr__(self):
        display = f"Ninja: {self.first_name}, {self.last_name}, Treats: {self.treats}, Pet Food: {self.pet_food}, Pet: {self.pet}"
        return display

    def walk(self):
        self.pet.play()
        return self
        
    def feed(self): 
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

ninja1 = Ninja("Frank", "Terrence", "bone", "Pedigree", pet1)
ninja1.feed().walk().bathe()
print(ninja1)


