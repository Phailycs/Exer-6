from modules.json_selector import jsons_selector

class Character():

    def __init__(self):
        self.__lvl = 1
        self.__exp = 0
        self.__next_lvl = 10
        self.__hp = 10
        self.__max_hp = 10
        self.__attack = 1
        self.__magic = 1
        self.__dodge = 1

    ## LEVEL ##
    def get_lvl(self):
        return self.__lvl
    
    def set_lvl(self):
        self.__lvl += 1
        print(jsons_selector("lvl", "events", variable=self.__lvl, single=True))
    
    def get_exp(self):
        return self.__exp
    
    def up(self):
        self.set_lvl()
        self.set_attack()
        self.set_magic()
        self.reset_exp()
        self.set_next_lvl()

    def reset_exp(self):
        self.__exp = 0

    def set_exp(self):
        self.__exp += 10

    def get_next_lvl(self):
        return self.__next_lvl
    
    def set_next_lvl(self):
        self.__next_lvl += 10
    ###########

    ## ATTRIBUTES ##
    def get_hp(self):
        return self.__hp
    
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

    def get_dodge(self):
        return self.__dodge
    
    def check_dodge(self):
        print(jsons_selector("attributes", "dodge", "attributes", variable=self.__dodge))
    ################