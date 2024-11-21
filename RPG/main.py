from classes import classes
from modules import gameplay

while(True):
    exit == False
    player = classes.Homeless(5, 10, 1, 1)
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
                print("======================================================================================================")
            case "beat":
                if (player.get_lvl() >= 5):
                    if(len(input_list) > 1): 
                        print("======================================================================================================")
                        gameplay.beat(player, input_list[1])
                        print("======================================================================================================")
                    else:
                        print("Missing argument.")
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