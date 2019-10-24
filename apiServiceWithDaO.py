from flask import Flask, jsonify, request
from werkzeug.exceptions import abort

from dataAccessLayer import DataAccessLayer

app = Flask(__name__)

db_obj = DataAccessLayer()


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

    statusCode = db_obj.addCustomerToDb(customer)
    if statusCode == 1:
        return jsonify(customer), 201
    else:
        return abort(404)


@app.route("/addItem", methods=["POST"])
def addItem():
    item = {'itemName': request.json['itemName']}
    statusCode = db_obj.addItemToDb(item)
    if statusCode == 1:
        return jsonify(item), 201
    else:
        return abort(404)


@app.route("/addOrder", methods=["POST"])
def addOrder():
    order = {
        "custId": request.json['custId'],
        "itemNumber": request.json['itemNumber'],
        "amountPaid": request.json['amountPaid'],
        "weight": request.json['weight'],
        "totalAmount": request.json['totalAmount']
    }

    statusCode = db_obj.addOrderToDb(order)
    if statusCode == 1:
        return jsonify(order), 201
    else:
        return abort(404)


@app.route("/getCustomer")
def getCustomers():
    rows = db_obj.getCustomersFromDb()
    if not rows or rows == 0:
        return abort(404)
    else:
        return jsonify(rows)


@app.route("/getCustomer/<string:custId>")
def getCustomer(custId):
    rows = db_obj.getCustomersFromDb(custId)
    if not rows or rows == 0:
        return abort(404)
    else:
        return jsonify(rows)


@app.route("/getItems")
def getItems():
    rows = db_obj.getItemsFromDb()
    if not rows or rows == 0:
        return abort(404)
    else:
        return jsonify(rows)


@app.route("/getItems/<int:itemId>")
def getItem(itemId):
    rows = db_obj.getItemsFromDb(itemId)
    if not rows or rows == 0:
        return abort(404)
    else:
        return jsonify(rows)


@app.route("/getCustomerOrder/<int:custId>")
def getCustomerOrders(custId):
    rows = db_obj.getCustomerOrders(custId)
    if not rows or rows == 0:
        return abort(404)
    else:
        return jsonify(rows)


@app.route("/getCustomerData")
def getCustomerData():
    name = request.args.get('name')
    phone = request.args.get('phone')
    rows = db_obj.getCustomerData(name, phone)
    if not rows or rows == 0:
        return abort(404)
    else:
        return jsonify(rows)


@app.route("/getItemOrders/<int:itemId>")
def getItemOrders(itemId):
    rows = db_obj.getItemOrders(itemId)
    if not rows or rows == 0:
        return abort(404)
    else:
        return jsonify(rows)


@app.route("/getOrder/<int:orderId>")
def getOrder(orderId):
    rows = db_obj.getOrderDetails(orderId)
    if not rows or rows == 0:
        return abort(404)
    else:
        return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True)
