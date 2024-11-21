from classes import classes

def conditional_classes(type):
    match type:
        case "warrior":
            class Enemy(classes.Warrior):
                def __init__(self, lvl, hp, attack, magic):
                    super().__init__(self, lvl, hp, attack, magic)
        case "wizard":
            class Enemy(classes.Wizard):
                def __init__(self, lvl, hp, attack, magic):
                    super().__init__(self, lvl, hp, attack, magic)
        case "archer":
            class Enemy(classes.Archer):
                def __init__(self, lvl, hp, attack, magic):
                    super().__init__(self, lvl, hp, attack, magic)
    return Enemy
