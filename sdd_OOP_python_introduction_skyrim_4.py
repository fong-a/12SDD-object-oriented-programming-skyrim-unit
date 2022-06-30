import random

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Dagger(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
    def sharpen(self):
        self.damage += 1
        print(f"{self.name} is sharpened. The updated attack damage is {self.damage}")
        

class Mace(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
    def imbue(self):
        self.damage += 10
        print(f"{self.name} is imbued with holy magic. The updated attack damage is {self.damage}")

class Player:
    def __init__(self, name, hp):
        self.weapon = None
        self.name = name
        self.hp = hp
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name} using the {self.weapon.name} for {self.weapon.damage}.")
        if self.weapon.damage >= target.hp:
            target.hp -= self.weapon.damage
            print(f"{self.name} kills {target.name}!")
        else:
            target.hp -= self.weapon.damage
            print(f"{target.name} has {target.hp} hp remaining!")
        
class Enemy:
    def __init__(self, name, hp):
        self.weapon = None
        self.name = name
        self.hp = hp
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name} using the {self.weapon.name} for {self.weapon.damage}.")
        target.hp -= self.weapon.damage
        print(f"{target.name} has {target.hp} remaining!")

player = Player("Mr Fong", 100)
player_two = Player("Mrs Fong", 100)
dagger = Dagger("Rusty Dagger", 1)
mace = Mace("Mace of Holy Power", 10)

player.weapon = dagger
player.weapon.sharpen()
player_two.weapon = mace
player_two.weapon.imbue()
