import sqlite3  
conn = sqlite3.connect('Punjab Meat Shop.db') 
c = conn.cursor()


'''Products Table'''

c.execute("DROP TABLE Products") 
c.execute("CREATE TABLE Products (Product_Number INTEGER PRIMARY KEY, Price FLOAT, Meat_Type TEXT, Meat_Part TEXT, Costs FLOAT, Quantity FLOAT)")

#Chicken
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.55, 'Chicken', 'Whole',  0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (2.55, 'Chicken', 'Fillet', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.49, 'Chicken', 'Drum Sticks', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.99, 'Chicken', 'Legs', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (2.45, 'Chicken', 'Thigh Meat', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.99, 'Chicken', 'Wings', 0, 0)")

#Lamb
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (4.69, 'Lamb', 'Legs', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (4.19, 'Lamb', 'Shoulder', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (3.99, 'Lamb', 'Chops', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (3.99, 'Lamb', 'Back', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (3.99, 'Lamb', 'Mince', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.99, 'Lamb', 'Ribs', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.99, 'Lamb', 'Neck', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (4.29, 'New Zealand Lamb', 'Leg', 0, 0)")

#Specialties
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (2.49, 'Pork', 'Leg', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (3.59, 'Masala Fish', 'N/A', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (2.20, 'Marinated Chicken', 'Wings', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.80, 'Marinated Chicken', 'Legs', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.95, 'Marinated Chicken', 'Drum Sticks', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (3.89, 'Goat', 'Meat', 0, 0)")

'''Sales Table'''

c.execute("DROP TABLE Sales")
c.execute("CREATE TABLE Sales (Sales_ID INTEGER PRIMARY KEY, Products TEXT, Date_Time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, Total FLOAT)")
c.execute("INSERT INTO Sales (Products, Total) VALUES ('Lamb Leg', 8.90)")

'''Sales Details Table'''

#c.execute("DROP TABLE Sales_Details")
#c.execute("CREATE TABLE Sales_Details (Sales_Det INTEGER PRIMARY KEY, Product_Number, Sales_ID, FOREIGN KEY(Product_Number) REFERENCES Products(Product_Number), FOREIGN KEY(Sales_ID) REFERENCES Sales(Sales_ID))")

'''Cooler Table'''
c.execute("DROP TABLE Cooler")
c.execute("CREATE TABLE Cooler (Check_Number INTEGER PRIMARY KEY, Date_Time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, Water_Bucket FLOAT, Temperature FLOAT, Rating INTEGER, Time_Taken INTEGER, Capacity_Utilisation FLOAT)")
c.execute("INSERT INTO Cooler (Water_Bucket, Temperature, Rating, Time_Taken, Capacity_Utilisation) VALUES (3.45, 3.1, 4, 8, 88.9)")


conn.commit() #saves all the changes always do this so it saves the work and closes the db properly
conn.close() #closes the connection

