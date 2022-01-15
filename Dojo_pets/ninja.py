import pets

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
        if (self.pet_food) > 0:
            self.pet.eat()
            self.pet_food -= 1
        else: 
            print("You need to buy food")

    def bathe(self):
        self.pet.noise1()
        return self

    def checkup(self):
        self.pet.checkup()
        return self
    
    def bedtime(self):
        self.pet.sleep()


Sam = Ninja("Sam", "Green", "Temptations", 5, pets.Butters)

Sam.feed()
Sam.bathe()
Sam.checkup()
Sam.walk()
Sam.bedtime()