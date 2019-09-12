__author__ = 'utkarsh_raghav'
import sqlite3


db = sqlite3.connect("Test.db")

c = db.cursor()

# #creating customer table
# c.execute("CREATE TABLE IF NOT EXISTS customer(custId INTEGER PRIMARY KEY, name TEXT, initial TEXT, address1 TEXT,"
#           "address2 TEXT, address3 TEXT, pincode TEXT, phone1 TEXT, phone2 TEXT, email TEXT)")

# #inserting data to customer table
# c.execute("INSERT INTO customer(name, initial, address1, address2, address3, pincode, phone1, phone2, email) VALUES ('TestName', 'Mr.', 'AddressTest1', 'AddressTest2', 'AddressTest3'"
#           ", '302020', '9123193213', '12311432141', 'utkarsh@raghav.com' )")
#
# c.execute("INSERT INTO customer(name, initial, address1, address2, address3, pincode, phone1, phone2, email) VALUES ('TestName', 'Mr.', 'AddressTest1', 'AddressTest2', 'AddressTest3'"
#           ", '302020', '9123193213', '12311432141', 'utkarsh@raghav.com' )")
#
# c.execute("INSERT INTO customer(name, initial, address1, address2, address3, pincode, phone1, phone2, email) VALUES ('TestName', 'Mr.', 'AddressTest1', 'AddressTest2', 'AddressTest3'"
#           ", '302020', '9123193213', '12311432141', 'utkarsh@raghav.com' )")

# #creating items table
# c.execute("CREATE TABLE IF NOT EXISTS itemDetails(itemNumber INTEGER PRIMARY KEY, itemName TEXT)")

# #creating orders table
# c.execute("CREATE TABLE IF NOT EXISTS orderDetails(orderId INTEGER PRIMARY KEY, custId TEXT, itemNumber INTEGER, "
#           "amountPaid INTEGER, amountDue INTEGER, totalAmount INTEGER,"
#           "FOREIGN KEY(custId) REFERENCES customer(custId), FOREIGN KEY(itemNumber) REFERENCES itemDetails(itemNumber))")

# #inserting data to itemDetails table
# c.execute("INSERT INTO itemDetails(itemName) VALUES ('TestItemName4')")
# c.execute("INSERT INTO itemDetails(itemName) VALUES ('TestItemName5')")
# c.execute("INSERT INTO itemDetails(itemName) VALUES ('TestItemName6')")

# #inserting data to orderDetails table
# c.execute("INSERT INTO orderDetails(custId, itemNumber, amountPaid, amountDue, totalAmount) VALUES ('2', 2, 105, 40, 145)")
# c.execute("INSERT INTO orderDetails(custId, itemNumber, amountPaid, amountDue, totalAmount) VALUES ('2', 3, 110, 24, 134)")
# c.execute("INSERT INTO orderDetails(custId, itemNumber, amountPaid, amountDue, totalAmount) VALUES ('1', 3, 111, 10, 121)")

db.commit()

c.execute("SELECT * FROM customer")
rows = c.fetchall()
print(rows)


c.execute("SELECT * FROM itemDetails")
rows = c.fetchall()
print(rows)


c.execute("SELECT * FROM orderDetails")
rows = c.fetchall()
print(rows)


c.execute("SELECT * FROM orderDetails JOIN itemDetails WHERE orderDetails.itemNumber =  itemDetails.itemNumber")
rows = c.fetchall()
print(rows)
