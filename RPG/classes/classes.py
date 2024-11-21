from classes.character import Character
from modules.json_selector import jsons_selector
import random

class Homeless(Character):

    def __init__(self, lvl, hp, attack, magic):
        Character.__init__(self)
        self.__lvl = lvl
        self.__next_lvl = lvl*10
        self.__hp = hp
        self.__max_hp = hp
        self.__attack = attack
        self.__magic = magic
        self.__class = "homeless"

    ## LEVEL ##
    def get_lvl(self):
        return self.__lvl
    
    def set_lvl(self):
        self.__lvl += 1
        print(jsons_selector("lvl", "events", variable=self.__lvl, single=True))

    def up(self):
        self.set_lvl()
        self.set_hp()
        self.set_attack()
        self.set_magic()
        self.reset_exp()
        self.set_next_lvl()
    
    def get_next_lvl(self):
        return self.__next_lvl
    
    def set_next_lvl(self):
        self.__next_lvl += 10
    ###########

    ## ATTRIBUTES ##
    def get_class(self):
        return self.__class

    def get_hp(self):
        return self.__hp
    
    def get_max_hp(self):
        return self.__max_hp
    
    def set_hp(self):
        self.__max_hp += 1

    def check_hp(self):
        print(jsons_selector("attributes", "hp", "attributes", variable=self.__hp))

    def get_attack(self):
        return self.__attack
    
    def set_attack(self):
        self.__attack += 1

    def check_attack(self):
        print(jsons_selector("attributes", "attack", "attributes", variable=self.__attack))

    def get_magic(self):
        return self.__magic
    
    def set_magic(self):
        self.__magic += 1

    def check_magic(self):
        print(jsons_selector("attributes", "magic", "attributes", variable=self.__magic))
    ################

    def strategy():
        pass

class Warrior(Homeless):
    
    def __init__(self, lvl, hp, attack, magic):
        Homeless.__init__(self, lvl, hp, attack, magic)
        self.__class = "warrior"
    
    def set_hp(self):
        self.__max_hp += 3
    
    def set_attack(self):
        self.__attack += 2

    def set_magic(self):
        self.__magic += 0

class Wizard(Homeless):
    
    def __init__(self, lvl, hp, attack, magic):
        Homeless.__init__(self, lvl, hp, attack, magic)
        self.__class = "wizard"
    
    def set_attack(self):
        self.__attack += 0

    def set_magic(self):
        self.__magic += 3

    def strategy():
        pass
    
    def healing(self):
        heal = self.__hp + self.__max_hp/2
        # Vérification que la valeur de dépasse pas les HP max du personnage
        heal == self.self.__max_hp if heal > self.__max_hp else heal == self.__hp

class Archer(Homeless):
    
    def __init__(self, lvl, hp, attack, magic):
        Homeless.__init__(self, lvl, hp, attack, magic)
        self.__class = "archer"
    
    def set_hp(self):
        self.__max_hp += 2

    def set_dodge(self):
        self.__magic += 2

    def up(self):
        self.set_dodge()
        return super().up()
    
    def strategy():
        pass

    def dodge(self):
        if (random.random() < (self.__dodge/100)):
            return True
        else:
            return False