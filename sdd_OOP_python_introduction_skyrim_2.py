import random

class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage # damage attribute

class Player:
    def __init__(self, name, hp):
        self.weapon = None
        self.name = name
        self.hp = hp
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name} using the {self.weapon.name} for {self.weapon.damage}.")
        
class Enemy:
    def __init__(self, name, hp):
        self.weapon = None
        self.name = name
        self.hp = hp
    
    def attack(self, target):
        print(f"{self.name} attacks {target.name} using the {self.weapon.name} for {self.weapon.damage}.")

player = Player("Mr Fong", 100)
enemy = Enemy("Student", 100)
sword = Weapon("Silver Sword", 10)
player.weapon = sword
player.attack(enemy)
    
