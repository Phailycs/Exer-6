from classes.Monster import Monster
import random

def pexing(player):
    monster = Monster("SANGLIER", 2)
    fight = True
    while(fight is True):
        player.attack(monster)
        if monster.get_hp() == 0:
            print("Toi t'es un bon.")
            player.gain_exp(10)
            fight = False
        monster.attack(player)
        if player.get_hp() == 0:
            print("Looser va.")
            fight = False

def gain_class(player):
    print("Tu viens d'obtenir une classe ! La classe nan ?")
    match random.choice(["warrior", "wizard", "archer"]):
        case "warrior":
            player.Warrior()
        case "wizard":
            player.Wizard()
        case "archer":
            player.Archer()