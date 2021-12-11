import json
import random
import time
import barcode
import shutil

errors = []


def getErros():
    return errors

def getCardDetails(card_number):
    with open("cards.txt") as json_f:
        data = json.load(json_f)
        defined = None 

        try:
            defined = data[str(card_number)]
        except:
            idcode = random.randint(1000000, 9000000)
            errors.append(idcode)
            return False

        for infos in defined:   
            tab = []
            tab.append(infos['name'])
            tab.append(infos['surname'])
            tab.append(infos['plan'])
            tab.append(infos['charghed'])
            tab.append(card_number)
            return tab
    

def writeEditCardDetails(new_json):
    with open("cards.txt", "r+") as json_f:
        data = json.load(json_f)
        data.update(new_json)

        json_f.seek(0)
        json.dump(data, json_f)
        json_f.truncate()
    
    return data




