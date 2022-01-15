class Pet:
    def __init__(self, name, type, tricks, health, energy, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.noise = noise
        
    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s energy increased by 25 after sleeping!")
        return self
        
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name}'s energy increased by 5 and health by 10 after feeding!")
        return self

    def play(self):
        self.health += 5
        self.energy -= 10
        print(f"{self.name}'s health increased by 5 after playing!")
        return self

    def noise1(self):
        print(f"{self.name} {self.noise}")
        return self

    def checkup(self):
        print(f"{self.name} --{self.health} Health -- {self.energy} Energy")

Butters = Pet("Butters", "Cat", "Keyboard Walking", 80, 100, "Meows Hungrily")

Butters.checkup()
