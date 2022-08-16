class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 50
        self.noise = noise
    
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5 
        self.health += 10
        return self

    def play(self):
        self.health += 10
        self.energy -= 15
        return self
    
    def noise(self):
        print(self.noise)

class Ninja:
    
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        if len(self.pet_food) > 0:
            food = self.pet_food.pop()
            print(f"Feeding {self.pet.name} {food}!")
            self.pet.eat()
        print("I'am hungry! ")
        return self

    def bathe(self):
        self.pet.noise()
        return self 

my_treats = ['Pizza','tacos', 'trash bag']
my_pet_food = ['Hot Dog','Burger']

peanut = Pet ('Mr. Peanuts', 'dog',['peanut is adorable'],'Woof, Woof')

aracely = Ninja('Aracely', 'Medrano',my_treats, my_pet_food, peanut)

aracely.feed()
aracely.feed()
aracely.feed()



