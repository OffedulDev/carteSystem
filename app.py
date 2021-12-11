from flask import *
from cardmanager import *

app = Flask(__name__)

@app.route("/<username>")
def home(username):
    det = getCardDetails(username)
    return render_template("index.html", name=det)

@app.route("/search")
def redSearch():
    return render_template("index.html")

@app.route("/")
def house():
    return render_template("index.html")

@app.route("/adminPanel", methods=['GET', 'POST'])
def idxs():
    if request.method == 'GET':
        return render_template("adminAccess.html")
    else:
        insertedPassword = request.form["text"]

        if insertedPassword == "camfil91":
            op = open("cards.txt")
            return 'Admin File Review: ' + op.read() + ' | Creato da Filippo Caminati | Copyright 2021'
        else:
            return 'Error: Access Denied.'


@app.route("/", methods=['POST'])
def searchCard():
    text = request.form["text"]
    processed_text = text.upper()
    
    data = getCardDetails(processed_text)
    
    if data != False:
        return render_template("foundCard.html", nome=data[0], cnome=data[1], abb=data[2], amm=data[3], cn=data[4], cardbarcode=url_for('static', filename=processed_text + ".svg"))
    else:
        return render_template("cardNotFound.html", cn=processed_text)

@app.route("/editCard", methods=['GET', 'POST'])
def indxs():
    print(str(request.method))
    if request.method == 'POST':
        newName = request.values.get("new_name")
        if newName == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY VALUE")
        newSurname = request.values.get("new_surname")
        if newSurname == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY VALUE")
        newPlan = request.values.get("new_plan")
        if newPlan == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY VALUE")
        newPrepaid = request.values.get("new_charghed")
        if newPrepaid == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY VALUE")
        cardNumber = request.values.get("cardToEdit")
        if cardNumber == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY CARD NUMBER")
        existCheck = getCardDetails(cardNumber)

        if existCheck == False: return render_template("cardNotFound.html", cn=cardNumber)
        jsonFormat = {}
        jsonFormat[cardNumber] = []
        jsonFormat[cardNumber].append({
            'name': newName,
            'surname': newSurname,
            'plan': newPlan,
            'charghed': newPrepaid,
            })

        writeEditCardDetails(jsonFormat)
        time.sleep(3)
    
        cardReturnInfo = getCardDetails(cardNumber)
        return render_template("foundCard.html", nome=cardReturnInfo[0], cnome=cardReturnInfo[1], abb=cardReturnInfo[2], amm=cardReturnInfo[3], cn=cardReturnInfo[4])
    else:
        return render_template("editCardPage.html")

@app.route("/newCard", methods=['GET', 'POST'])
def idsx():
    if request.method == 'GET':
        return render_template("createCardPage.html")
    else:
        newName = request.values.get("nm")
        if newName == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY VALUE")
        newSurname = request.values.get("cm")
        if newSurname == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY VALUE")
        newPlan = request.values.get("pl")
        if newPlan == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY VALUE")
        newPrepaid = request.values.get("ch")
        if newPrepaid == "": return render_template("cardNotFound.html", cn="USER TRIED TO SEND EMPTY VALUE")
        cardNumber = random.randint(1000000000, 9999999999)
        
        jsonFormat = {}
        jsonFormat[cardNumber] = []
        jsonFormat[cardNumber].append({
            'name': newName,
            'surname': newSurname,
            'plan': newPlan,
            'charghed': newPrepaid,
            })

        writeEditCardDetails(jsonFormat)
        time.sleep(3)
    
        cardReturnInfo = getCardDetails(cardNumber)
        return render_template("foundCard.html", nome=cardReturnInfo[0], cnome=cardReturnInfo[1], abb=cardReturnInfo[2], amm=cardReturnInfo[3], cn=cardReturnInfo[4])


        




