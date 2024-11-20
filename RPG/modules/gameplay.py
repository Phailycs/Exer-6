from classes import classes
from modules.json_selector import jsons_selector
import random

def pex(player):
    # Calculer un % de réussite
    if random.random() < 0.80 + (0.01 * int(player.get_lvl())):
        print(jsons_selector("pex","winner", "outcome"))
        # Une fois réussie, le joueur gagne l'exp
        player.set_exp()
        # Vérification s'il y a lvl up
        if int(player.get_exp()) == int(player.get_next_lvl()):
            print("--------------------------------------------------------")
            lvl_up(player)
    else:
        print(jsons_selector("pex", "looser", "outcome"))

def beat(player):
    pass

def lvl_up(player):
    player.up()
    if player.get_lvl() == 5:
        classe = [classes.Warrior(), classes.Wizard(), classes.Archer()]
        player=random.choice(classe)
        print("Bravo, You specialised in the " + str(player.get_name()) + " class.")

def spawn(player):
    print("======================================================================================================")
    print("Description:")
    print(jsons_selector("spawn", "events", single=True))
    print("--------------------------------------------------------")
    print("Welcome to the incredible world of Tristania, where the only thing sad is your life.\nYour rank is defined by your level, so smash monsters to be simply the best.")
    print("--------------------------------------------------------")
    print("Stats : HP: " + str(player.get_hp()) + " | Attack: " + str(player.get_attack()) + " | Magic: " + str(player.get_magic()) + " | Dodge: " + str(player.get_dodge()))
    print("======================================================================================================")