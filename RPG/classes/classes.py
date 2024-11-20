from classes.character import Character
import random

class Warrior(Character):
    
    def __init__(self):
        self.__lvl = 5
        self.__exp = 0
        self.__next_lvl = 60
        self.__hp = 15
        self.__max_hp = 15
        self.__attack = 6
        self.__magic = 6
        self.__dodge = 1
        self.__name = "warrior"

    def get_name(self):
        return self.__name

    def strategy():
        pass

class Wizard(Character):
    
    def __init__(self):
        self.__lvl = 5
        self.__exp = 0
        self.__next_lvl = 60
        self.__hp = 15
        self.__max_hp = 15
        self.__attack = 6
        self.__magic = 6
        self.__dodge = 1
        self.__name = "wizard"
    
    def get_name(self):
        return self.__name

    def strategy():
        pass
    
    def healing():
        pass

class Archer(Character):
    
    def __init__(self):
        self.__lvl = 5
        self.__exp = 0
        self.__next_lvl = 60
        self.__hp = 15
        self.__max_hp = 15
        self.__attack = 6
        self.__magic = 6
        self.__dodge = 1
        self.__name = "archer"
    
    def get_name(self):
        return self.__name
    
    def strategy():
        pass

    def dodge():
        random.random()