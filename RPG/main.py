from classes import character
from modules import gameplay

while(True):
    exit == False
    player = character.Character()
    gameplay.spawn(player)
    while(exit != True):
        print("The commands available are: pex, beat {class}, lvl, hp.\nTo exit the program, type ‘exit’.") if player.get_lvl() > 5 else print("The commands available are: pex, lvl, hp.\nTo exit the program, type ‘exit’.")
        if player.get_lvl() == 5 :
            print("------------------------------")
            print("Now you can fight other classes with the command: beat {class}")
            print("------------------------------")
        print("What do you want to do?")
        x = input()
        input_list = x.split(" ")
        match input_list[0]:
            case "pex":
                print("======================================================================================================")
                gameplay.pex(player)
                print(player.get_exp())
                print(player.get_next_lvl())
                print("======================================================================================================")
            case "beat":
                if player.get_lvl() >= 5: 
                    print("======================================================================================================")
                    gameplay.beat(player, input_list[1])
                    print("======================================================================================================")
                else:
                    print("Can't you read or something?")
            case "lvl":
                print("You are lvl " + str(player.get_lvl()) + ".")
            case "hp":
                print("======================================================================================================")
                player.check_hp()
                print("======================================================================================================")
            case "exit":
                exit == True
                break
            case _:
                print("Can't you read or something?")
    break