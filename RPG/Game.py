from classes.Character import Character
import Gameplay
import Decoration

class Game():

    @staticmethod
    def run():
        print("Vous appelez comment ? Rep.")
        player = Character(input())
        Decoration.deko()
        player.show_stats()
        exit = False
        while(exit is False):
            print("Bonjour mon mignon, tu veux faire quoi mon gourmand ? (pex, exit, beat)")
            valeur = input().split(" ")
            match valeur[0]:
                case "pex":
                    Gameplay.pexing(player)
                case "exit":
                    print("wesh tu pars ou quoi ?")
                    exit = True
                case "beat":
                    print("tabasser grave " + valeur[1])
                case _:
                    print("Soit pex, soit exit et fais pas chier.")