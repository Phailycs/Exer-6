from math import ceil
import Gameplay

class Character():

    def __init__(self, name):
        self.__lvl = 1
        self.__exp = 0
        self.__next_lvl = self.__lvl * 10
        self.__max_hp = 10
        self.__hp = self.__max_hp
        self.__attack = 1
        self.__magic = 1
        self.__dodge = 1
        self.__name = name
        self.__class = 'Truand'
    
    def get_name(self):
        return self.__name
    
    def get_class(self):
        return self.__class

    def get_lvl(self):
        return self.__lvl
    
    def get_exp(self):
        return self.__exp
    
    def get_next_lvl(self):
        return self.__next_lvl

    def get_hp(self):
        return self.__hp
    
    def get_max_hp(self):
        return self.__max_hp
    
    def get_attack(self):
        return self.__attack
    
    def get_dodge(self):
        return self.__dodge
    
    def get_magic(self):
        return self.__magic
    
    def set_name(self, valeur):
        self.__name = valeur

    def set_class(self, valeur):
        self.__class = valeur

    def set_lvl(self, valeur):
        self.__lvl = valeur
    
    def set_exp(self, valeur):
        self.__exp = valeur
    
    def set_next_lvl(self, valeur):
        self.__next_lvl = valeur

    def set_hp(self, valeur):
        self.__hp = valeur
        if self.__hp <= 0 :
            self.__hp = 0
            print(self.get_name() + " a été vaincu.")
        if self.get_hp() > self.get_max_hp():
            self.__hp = self.get_max_hp()
    
    def set_max_hp(self, valeur):
        self.__max_hp = valeur
    
    def set_attack(self, valeur):
        self.__attack = valeur
    
    def set_dodge(self, valeur):
        self.__dodge = valeur
    
    def set_magic(self, valeur):
        self.__magic = valeur

    def drink(self):
        print("Vous buvez goulument la potion")
        self.receive_heal(10)

    def heal(self, entity):
        if entity.get_hp() == entity.get_max_hp():
            print(self.get_name() + " a déjà tous ses PV.")
            return
        entity.receive_heal(ceil(self.get_magic()/2))
        if entity.get_name() == self.get_name():
            print(self.get_name() + " se soigne.")
        else:
            print(self.get_name() + " FAIS DES POUTOUS A " + entity.get_name())

    def receive_heal(self, heal):
        if self.get_hp() == self.get_max_hp():
            print(self.get_name() + " a déjà tous ses PV.")
            return
        result=heal if (self.get_max_hp() - self.get_hp()) > heal else result=self.get_max_hp() - self.get_hp()
        self.set_hp(self.get_hp() + heal)
        print(self.get_name() + " reçoit " + str(result) + " de soins. Il possède " + str(self.get_hp()) + " PV.")

    def attack(self, victim):
        victim.receive_dmg(self.get_attack())
        print(self.get_name() + " TABASSE " + victim.get_name())

    def receive_dmg(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(self.get_name() + " douille un max. Il a subit " + str(damage) + " de dégat(s).")

    def gain_exp(self, montant):
        self.set_exp(self.get_exp() + montant)
        if self.get_exp() >= self.get_next_lvl():
            self.level_up()

    def level_up(self):
        print("BRAVO, vous avez level up, content ?")
        self.gain_stats()
        self.set_lvl(self.get_lvl() + 1)
        self.set_exp(0)
        self.set_next_lvl(self.get_next_lvl() + 10)
        self.set_hp(self.get_max_hp())
        if self.get_lvl == 5:
            Gameplay.gain_class()

    def gain_stats(self):
        self.set_attack(self.get_attack() + 1)
        self.set_max_hp(self.get_max_hp() + 1)
        self.set_magic(self.get_magic() + 1)

    def show_stats(self):
        print("Name: " + self.get_name())
        print("Class: " + self.get_class())
        print("Level: " + str(self.get_lvl()))
        print("Exp: " + str(self.get_exp()) + " / " + str(self.get_next_lvl()))
        print("HP: " + str(self.get_hp()) + " / " + str(self.get_max_hp()))
        print("Attack: " + str(self.get_attack()))
        print("Dodge: " + str(self.get_dodge()))
        print("Magic: " + str(self.get_magic()))