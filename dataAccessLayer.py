import sqlite3


class DataAccessLayer:
    def __init__(self):
        with sqlite3.connect("Test.db", check_same_thread=False) as self.connection:
            self.c = self.connection.cursor()

    def addCustomerToDb(self, customer):
        insert_query = "INSERT INTO customer(name, initial, address1, address2, address3, pincode, phone1, phone2, " \
                       "email) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}' )". \
            format(customer['name'], customer['initial'], customer['address1']
                   , customer['address2'], customer['address3'], customer['pincode']
                   , customer['phone1'], customer['phone2'], customer['email'])
        try:
            self.c.execute(insert_query)
            self.connection.commit()
            return 1
        except sqlite3.Error:
            return 0

    def addItemToDb(self, item):
        insert_query = "INSERT INTO itemDetails(itemName) VALUES ('{}')".format(item['itemName'])
        try:
            self.c.execute(insert_query)
            self.connection.commit()
            return 1
        except sqlite3.Error:
            return 0

    def addOrderToDb(self, order):
        insert_query = "INSERT INTO orderDetails(custId, itemNumber, amountPaid, amountDue, totalAmount)" \
                       " VALUES ('{}', '{}', '{}', '{}', '{}' )". \
            format(order['custId'], order['itemNumber'], order['amountPaid']
                   , order['amountDue'], order['totalAmount'])
        try:
            self.c.execute(insert_query)
            self.connection.commit()
            return 1
        except sqlite3.Error:
            return 0

    def getCustomersFromDb(self, phone1=-1):
        if phone1 == -1:
            query = "SELECT * FROM customer"
            print(query)
            try:
                self.c.execute(query)
                rows = self.c.fetchall()
                return rows
            except sqlite3.Error:
                return 0
        else:
            query = "SELECT * FROM customer where phone1 like '{}%' OR phone2 like '{}%' OR name like '{}%'".format(phone1, phone1,
                                                                                                        phone1)
            print(query)
            self.c.execute(query)
            try:
                self.c.execute(query)
                rows = self.c.fetchall()
                return rows
            except sqlite3.Error:
                return 0

    def getItemsFromDb(self, itemNumber=-1):
        if itemNumber == -1:
            query = "SELECT * FROM itemDetails"
            try:
                self.c.execute(query)
                rows = self.c.fetchall()
                return rows
            except sqlite3.Error:
                return 0
        else:
            query = "SELECT * FROM itemDetails where itemNumber = {}".format(itemNumber)
            self.c.execute(query)
            try:
                self.c.execute(query)
                rows = self.c.fetchone()
                return rows
            except sqlite3.Error:
                return 0

    def getCustomerOrders(self, custId):
        query = "SELECT orderId, itemName, weight, amountPaid, totalAmount FROM orderDetails, itemDetails WHERE " \
                "custId = {} AND orderDetails.itemNumber = itemDetails.itemNumber".format(custId)
        try:
            self.c.execute(query)
            rows = self.c.fetchall()
            return rows
        except sqlite3.Error:
            return 0

    def getItemOrders(self, itemId):
        query = "SELECT * FROM orderDetails WHERE itemNumber = {}".format(itemId)
        try:
            self.c.execute(query)
            rows = self.c.fetchall()
            return rows
        except sqlite3.Error:
            return 0

    def getOrderDetails(self, orderId):
        query = "SELECT orderId, itemName, weight, amountPaid, totalAmount FROM orderDetails, itemDetails WHERE " \
                "orderId = {} AND orderDetails.itemNumber = itemDetails.itemNumber".format(orderId)
        try:
            self.c.execute(query)
            rows = self.c.fetchall()
            return rows
        except sqlite3.Error:
            return 0
