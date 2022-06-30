class Weapon:
    def __init__(self, name, damage):
        self.__name = name
        self.__damage = damage
    def get_damage(self):
        return self.__damage
    def get_name(self):
        return self.__name    
        
    def set_damage(self, damage):
        self.__damage += damage
    

class Dagger(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
    def sharpen(self):
        self.set_damage(1) 
        print(f"{self.get_name()} is sharpened. The updated attack damage is {self.get_damage()}")

class Sword(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
    def sharpen(self):
        self.set_damage(4)
        print(f"{self.get_name()} is sharpened. The updated attack damage is {self.get_damage()}")

class Mace(Weapon):
    def __init__(self, name, damage):
        super().__init__(name, damage)
    def imbue(self):
        self.set_damage(10)
        print(f"{self.get_name()} is imbued with holy magic. The updated attack damage is {self.get_damage()}")
    def sharpen(self):
        print(f"{self.get_name()} cannot be sharpened, it is a blunt object, duh!")

class Player:
    def __init__(self, name, hp):
        self.__weapon = None
        self.__name = name
        self.__hp = hp
        
    def get_hp(self):
        return self.__hp
    def get_weapon(self):
        return self.__weapon
    def get_name(self):
        return self.__name
    
    def set_weapon(self, weapon):
        self.__weapon = weapon 
    def set_hp(self, damage):
        self.__hp -= damage
    
    def attack(self, target):
        weapon = self.get_weapon()
        print(f"{self.get_name()} attacks {target.get_name()} using the {weapon.get_name()} for {weapon.get_damage()}.")
        if weapon.get_damage() >= target.get_hp():
            target.set_hp(weapon.get_damage()) 
            print(f"{self.name} kills {target.name}!")
        else:
            target.set_hp(weapon.get_damage())
            print(f"{target.get_name()} has {target.get_hp()} hp remaining!")
        
class Enemy:
    def __init__(self, name, hp):
        self.__weapon = None
        self.__name = name
        self.__hp = hp
    
    def get_hp(self):
        return self.__hp
    def get_weapon(self):
        return self.__weapon
    def get_name(self):
        return self.__name
    def set_hp(self, damage):
        self.__hp -= damage
    def set_weapon(self, weapon):
        self.__weapon = weapon 
    
    def attack(self, target):
        weapon = self.get_weapon()
        print(f"{self.get_name()} attacks {target.get_name()} using the {weapon.get_name()} for {weapon.get_damage()}.")
        target.set_hp(weapon.get_damage())
        print(f"{target.get_name()} has {target.get_hp()} remaining!")

player = Player("Mr Fong", 100)
player_two = Player("Mrs Fong", 100)
sword = Dagger("Big Sword", 1)
mace = Mace("Mace of Holy Power", 10)
player.set_weapon(sword)
player_two.set_weapon(mace)
player.attack(player_two)
player_two.attack(player)
