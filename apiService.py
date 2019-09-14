from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("Test.db", check_same_thread=False)
c = db.cursor()


@app.route("/addCustomer", methods=['POST'])
def addCustomer():
    customer = {
        'name': request.json['name'],
        'initial': request.json['initial'],
        'address1': request.json['address1'],
        'address2': request.json['address2'],
        'address3': request.json['address3'],
        'pincode': request.json['pincode'],
        'phone1': request.json['phone1'],
        'phone2': request.json['phone2'],
        'email': request.json['email']
    }

    insert_query = "INSERT INTO customer(name, initial, address1, address2, address3, pincode, phone1, phone2, " \
                   "email) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' )". \
        format(customer['name'], customer['initial'], customer['address1']
               , customer['address2'], customer['address3'], customer['pincode']
               , customer['phone1'], customer['phone2'], customer['email'])
    c.execute(insert_query)
    db.commit()
    return jsonify(customer)


@app.route("/addItem", methods=["POST"])
def addItem():
    item = {'itemName': request.json['itemName']}
    insert_query = "INSERT INTO itemDetails(itemName) VALUES ('{}')".format(item['itemName'])
    c.execute(insert_query)
    db.commit()
    return jsonify(item)


@app.route("/addOrder", methods=["POST"])
def addOrder():
    order = {
        "custId": request.json['custId'],
        "itemNumber": request.json['itemNumber'],
        "amountPaid": request.json['amountPaid'],
        "amountDue": request.json['amountDue'],
        "totalAmount": request.json['totalAmount']
    }

    insert_query = "INSERT INTO orderDetails(custId, itemNumber, amountPaid, amountDue, totalAmount)" \
                   " VALUES ('{}', '{}', '{}', '{}', '{}' )". \
        format(order['custId'], order['itemNumber'], order['amountPaid']
               , order['amountDue'], order['totalAmount'])
    c.execute(insert_query)
    db.commit()
    return jsonify(order)


@app.route("/getCustomer")
def getCustomers():
    query = "SELECT * FROM customer"
    c.execute(query)
    rows = c.fetchall()
    return jsonify(rows)


@app.route("/getCustomer/<int:custId>")
def getCustomer(custId):
    query = "SELECT * FROM customer where custId = {}".format(custId)
    c.execute(query)
    rows = c.fetchall()
    return jsonify(rows)

def getItems():
    pass


def getItem(itemId):
    pass


def getOrders(custId):
    pass


def getItemOrders(itemId):
    pass


if __name__ == "__main__":
    app.run(debug=True)
