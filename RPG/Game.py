from classes.Character import Character
from randomizer import spawn # AJOUT POUR MESSAGE ALLEATOIRE
import Gameplay, Decoration, random

class Game():

    @staticmethod
    def run():
        print("Vous appelez comment ? Rep.")
        player = Character(input())
        Decoration.deko()
        print(random.choice(spawn["welcome"]).format(name=player.get_name())) # AJOUT POUR MESSAGE ALLEATOIRE
        Decoration.separator()
        player.show_stats()
        Decoration.deko()
        exit = False
        while(exit is False):
            print("Bonjour mon mignon, tu veux faire quoi mon gourmand ? (pex, exit, beat, stats, drink)")
            valeur = input().split(" ")
            match valeur[0]:
                case "pex":
                    Gameplay.pexing(player)
                case "exit":
                    print("wesh tu pars ou quoi ?")
                    exit = True
                case "beat":
                    print("tabasser grave " + valeur[1])
                case "stats":
                    player.show_stats()
                case "drink":
                    player.drink()
                case _:
                    print("Soit pex, soit exit et fais pas chier.")