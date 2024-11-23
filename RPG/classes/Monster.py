
class Monster():

    def __init__(self, name, lvl):
        self.__lvl = lvl
        self.__max_hp = 10 + lvl - 1
        self.__hp = self.__max_hp
        self.__attack = 1 + lvl - 1
        self.__magic = 1 + lvl - 1
        self.__dodge = 1 
        self.__name = name
    
    def get_name(self):
        return self.__name

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

    def set_lvl(self, valeur):
        self.__lvl = valeur
    
    def set_exp(self, valeur):
        self.__exp = valeur
    
    def set_next_lvl(self, valeur):
        self.__next_lvl = valeur

    def set_hp(self, valeur):
        self.__hp = valeur
        if self.__hp < 0 :
            self.__hp = 0
            print(self.get_name() + " a été vaincu.")
    
    def set_max_hp(self, valeur):
        self.__max_hp = valeur
    
    def set_attack(self, valeur):
        self.__attack = valeur
    
    def set_dodge(self, valeur):
        self.__dodge = valeur
    
    def set_magic(self, valeur):
        self.__magic = valeur

    def attack(self, victim):
        victim.receive_dmg(self.get_attack())
        print(self.get_name() + " TABASSE " + victim.get_name())

    def receive_dmg(self, damage):
        self.set_hp(self.get_hp() - damage)
        print(self.get_name() + " douille un max. Il a subit " + damage + " de dégat(s).")

    def show_stats(self):
        print("Level: " + str(self.get_lvl()))
        print("Exp: " + str(self.get_exp()) + " / " + str(self.get_next_lvl()))
        print("HP: " + str(self.get_hp()) + " / " + str(self.get_max_hp()))
        print("Attack: " + str(self.get_attack()))
        print("Dodge: " + str(self.get_dodge()))
        print("Magic: " + str(self.get_magic()))