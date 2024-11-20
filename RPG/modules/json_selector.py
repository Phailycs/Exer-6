import random, json

def jsons_selector(asset, value, index="", variable="", single = False):
    # Ouverture du fichier
    if single == False:
        with open("RPG/assets/" + asset + ".json", "r") as file:
            data = json.load(file)
            json_data = data[index]
            # Boucle qui récupère l'attribut KEY dans la liste d'ATTRIBUTES
            for key in json_data:
                # Création d'une liste des éléments de la KEY (key + events)
                list_values = list(key.values())
                if list_values[0] == value:
                    events_list = list_values[1]
                    break
                else :
                    KeyError
    else:
        with open("RPG/assets/" + asset + ".json", "r") as file:
            data = json.load(file)
        events_list = data[value]
    if variable != "":
        return random.choice(events_list) % variable
    else:
        return random.choice(events_list)