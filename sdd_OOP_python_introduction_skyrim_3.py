import random

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

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
enemy = Enemy("Student", 100)
sword = Weapon("Silver Sword", 10)
player.weapon = sword
for i in range(10):
    player.attack(enemy)
