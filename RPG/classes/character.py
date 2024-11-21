from modules.json_selector import jsons_selector

class Character():
    # Constructeur
    def __init__(self):
        self.__exp = 0
        self.__dodge = 1
        
    ## LEVEL ##
    def get_exp(self):
        return self.__exp

    def reset_exp(self):
        self.__exp = 0

    def set_exp(self):
        self.__exp += 10
    ###########

    ## ATTRIBUTES ##
    def get_dodge(self):
        return self.__dodge
    
    def check_dodge(self):
        print(jsons_selector("attributes", "dodge", "attributes", variable=self.__dodge))
    ################