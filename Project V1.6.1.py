from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import uuid
import hashlib

'''

conn = sqlite3.connect('Punjab Meat Shop.db') 
c = conn.cursor()

"Products Table"

c.execute("CREATE TABLE Products (Product_Number INTEGER PRIMARY KEY, Price Per KG FLOAT, Meat_Type TEXT, Meat_Part TEXT, Costs Per KG FLOAT, Quantity KG FLOAT)")

#Chicken
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.70, 'Chicken', 'Whole',  0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.16, 'Chicken', 'Fillet', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.68, 'Chicken', 'Drum Sticks', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.45, 'Chicken', 'Legs', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.11, 'Chicken', 'Thigh Meat', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.90, 'Chicken', 'Wings', 0, 0)")

#Lamb
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (2.13, 'Lamb', 'Legs', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.90, 'Lamb', 'Shoulder', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.81, 'Lamb', 'Chops', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.81, 'Lamb', 'Back', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.81, 'Lamb', 'Mince', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.90, 'Lamb', 'Ribs', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.90, 'Lamb', 'Neck', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.95, 'New Zealand Lamb', 'Leg', 0, 0)")

#Specialties
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0, 'Turkey', 'Whole', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.13, 'Pork', 'Leg', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.63, 'Masala Fish', 'N/A', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.01, 'Marinated Chicken', 'Wings', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.82, 'Marinated Chicken', 'Legs', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (0.89, 'Marinated Chicken', 'Drum Sticks', 0, 0)")
c.execute("INSERT INTO Products (Price, Meat_Type, Meat_Part, Costs, Quantity) VALUES (1.76, 'Goat', 'Meat', 0, 0)")

"Sales Table"

c.execute("CREATE TABLE Sales (Sales_ID INTEGER PRIMARY KEY, Date_Time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, Meat_Type TEXT, Meat_Part TEXT, Meat_Weight 'KG' FLOAT, Total FLOAT)")

"Sales Details Table"

c.execute("CREATE TABLE Sales_Details (Sales_Det INTEGER PRIMARY KEY, Product_Number, Sales_ID, FOREIGN KEY(Product_Number) REFERENCES Products(Product_Number), FOREIGN KEY(Sales_ID) REFERENCES Sales(Sales_ID))")

"Cooler Table"

c.execute("CREATE TABLE Cooler (Check_Number INTEGER PRIMARY KEY, Date_Time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP, Water_Bucket FLOAT, Temperature FLOAT, Rating INTEGER, Time_Taken INTEGER, Capacity_Utilisation FLOAT)")

conn.commit() #saves all the changes always do this so it saves the work and closes the db properly
conn.close() #closes the connection

'''

def checkNum(entry):
    try:
        float(entry)
    except ValueError:
        messagebox.showinfo("Error!", "Please enter a numerical value in the entry box.")
        return False
    else:
        return True
    

def buildSystem():
    def setTitle(root, title):
        #Creates the window title
        root.title(title)
        
    #This code creates the whole frame
    global root
    root = Tk()
    root.minsize(width=800, height=350)
    setTitle(root,"Punjab Meat Shop")

    def createLogo(frame):
        #Creates content for logo page
        #Content to go in chicken table
        chick = ttk.Label(frame, text="Chicken (price per LB)")
        chick.grid(column=1, row=0, sticky=(N), padx=5)
        chwhole = ttk.Label(frame, text="Whole - £1.55")
        chwhole.grid(column=1, row=2, sticky=(N))
        chfillet = ttk.Label(frame, text="Fillet - £2.55")
        chfillet.grid(column=1, row=3, sticky=(N))
        chdrum = ttk.Label(frame, text="Drum Sticks - £1.49")
        chdrum.grid(column=1, row=4, sticky=(N))
        chlegs = ttk.Label(frame, text="Legs - £0.99")
        chlegs.grid(column=1, row=5, sticky=(N))
        chthigh = ttk.Label(frame, text="Thigh Meat - £2.45")
        chthigh.grid(column=1, row=6, sticky=(N))
        chwings = ttk.Label(frame, text="Wings - £1.99")
        chwings.grid(column=1, row=7, sticky=(N))
        #Content to go in lamb table
        lamb = ttk.Label(frame, text="Lamb (price per LB)")
        lamb.grid(column=3, row=0, sticky=(N))
        laLegs = ttk.Label(frame, text="Legs - £4.69")
        laLegs.grid(column=3, row=2, sticky=(N))
        laShoul = ttk.Label(frame, text="Shoulder - £4.19")
        laShoul.grid(column=3, row=3, sticky=(N))
        laChops = ttk.Label(frame, text="Chops - £3.99")
        laChops.grid(column=3, row=4, sticky=(N))
        laBack = ttk.Label(frame, text="Back - £3.99")
        laBack.grid(column=3, row=5, sticky=(N))
        laMince = ttk.Label(frame, text="Mince - £3.99")
        laMince.grid(column=3, row=6, sticky=(N))
        laRibs = ttk.Label(frame, text="Ribs - £1.99")
        laRibs.grid(column=3, row=7, sticky=(N))
        laNeck = ttk.Label(frame, text="Neck - £1.99")
        laNeck.grid(column=3, row=8, sticky=(N))
        nzLeg = ttk.Label(frame, text="N/Z Lamb Leg - £4.29")
        nzLeg.grid(column=3, row=9, sticky=(N))
        #Content to go in specialties table
        special = ttk.Label(frame, text="Specialties (price per LB)")
        special.grid(column=5, row=0, sticky=(N))
        porkLeg = ttk.Label(frame, text="Pork Leg - £2.49" )
        porkLeg.grid(column=5, row=2, sticky=(N))
        maFish = ttk.Label(frame, text="Masala Fish - £3.59")
        maFish.grid(column=5, row=3, sticky=(N))
        maWings = ttk.Label(frame, text="Marinated Chicken Wings - £2.20")
        maWings.grid(column=5, row=4, sticky=(N))
        maLegs = ttk.Label(frame, text="Marinated Chicken Legs - £1.80")
        maLegs.grid(column=5, row=5, sticky=(N))
        maDrum = ttk.Label(frame, text="Marinated Chicken Drum Sticks - £1.95")
        maDrum.grid(column=5, row=6, sticky=(N))
        goat = ttk.Label(frame, text="Goat Meat - £3.89")
        goat.grid(column=5, row=7, sticky=(N))
        #Log out button
        logOut = ttk.Button(frame, text="Log Out", command=logOutButton)
        logOut.grid(column=6, row=10, sticky=(E))

                
        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_columnconfigure(6, weight=1)
        content.grid_rowconfigure(2, weight=1)
        content.grid_rowconfigure(3, weight=1)
        content.grid_rowconfigure(4, weight=1)
        content.grid_rowconfigure(5, weight=1)
        content.grid_rowconfigure(6, weight=1)
        content.grid_rowconfigure(7, weight=1)
        content.grid_rowconfigure(8, weight=1)
        content.grid_rowconfigure(9, weight=1)
        

    #Idle Timer
    import time

    global started
    started = time.time()

    def checkIdle():
        current = time.time()
        timer = current - started
        if timer > 120:
            buildLogo()
        else:
            root.after(1000, checkIdle)

    def key(event):
        movement = (event.x, event.y)
        global started
        started = time.time()

    checkIdle()

    root.bind("<Motion>", key)

    def profitTotal():
        conn = sqlite3.connect("Punjab Meat Shop.db")
        c = conn.cursor()
        c.execute("SELECT Meat_Type, Meat_Part, Meat_Weight, Total FROM Sales")

        total = c.fetchall()

        conn.close()
        
        totalResult = 0

        meatCost = [ ]

        runningTotalProfit = 0
        
        for result in total:
            mType = result[0]
            mPart = result[1]
            mWeight = float(result[2])
            mTotal = float(result[3])
            
            conn = sqlite3.connect("Punjab Meat Shop.db")
            c = conn.cursor()
            c.execute("SELECT Costs FROM Products WHERE Meat_Type = ? AND Meat_Part = ?", (mType, mPart))
            costs = c.fetchall()
            conn.close()

            for cost in costs:
                meatCost.append(cost[0])

                totalMeatCost = meatCost[0] * mWeight
                totalProfit = mTotal - totalMeatCost
                runningTotalProfit = runningTotalProfit + totalProfit

        runningTotalProfit = round(runningTotalProfit, 2)
        return runningTotalProfit
    
    def revenueTotal():
        conn = sqlite3.connect("Punjab Meat Shop.db")
        c = conn.cursor()
        c.execute("SELECT Total FROM Sales")

        revenue = c.fetchall()

        conn.close()
        
        totalRevenue = 0

        for result in revenue:
            totalRevenue = totalRevenue + result[0]

        totalRevenue = round(totalRevenue, 2)

        return totalRevenue
            
    def createHome(frame):
        #Creates content for home page
        profit = ttk.Button(frame, text="Profit: ")
        profit.grid(column=1, row=1, sticky=(N))
        profitLabel = ttk.Label(frame, text = profitTotal())
        profitLabel.grid(column=3, row=1, sticky=(N))
        revenue = ttk.Button(frame, text="Revenue: ")
        revenue.grid(column=1, row=3, sticky=(N))
        revenueLabel = ttk.Label(frame, text = revenueTotal())
        revenueLabel.grid(column=3, row=3, sticky=(N))
        noOfSales = ttk.Button(frame, text="Number of Sales: ")
        noOfSales.grid(column=1, row=5, sticky=(N))
        reorder = ttk.Button(frame, text="Reorder Quantity Level: ")
        reorder.grid(column=5, row=2, sticky=(N))
        capacityUtil = ttk.Button(frame, text="Capacity Utilisation: ")
        capacityUtil.grid(column=5, row=4, sticky=(N))
        
        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_columnconfigure(6, weight=1)
        content.grid_rowconfigure(0, weight=2)
        content.grid_rowconfigure(1, weight=2)
        content.grid_rowconfigure(2, weight=2)
        content.grid_rowconfigure(3, weight=2)
        content.grid_rowconfigure(4, weight=2)
        content.grid_rowconfigure(6, weight=2)
        
    def createOrders(frame):
        def addOrder():
            changePage("addOrder")
        #Creates content for orders page
        add = ttk.Button(frame, text="Add Order", command=addOrder)
        add.grid(column=1, row=0, sticky=(N))
        delete = ttk.Button(frame, text="Delete Order")
        delete.grid(column=3, row=0, sticky=(N))
        view = ttk.Button(frame, text="View Orders")
        view.grid(column=5, row=0, sticky=(N), padx=5)

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_columnconfigure(6, weight=1)

    def individualMeatType():
        conn = sqlite3.connect('Punjab Meat Shop.db') 
        c = conn.cursor()

        c.execute("SELECT DISTINCT Meat_Type FROM Products")

        result = c.fetchall()

        meatType = [ ]
    
        for meat in result:
            meatType.append(meat[0])

        conn.commit()
        conn.close()

        return meatType
       
        
    def createOrder(frame):        
        def individualMeatPart(event):
            mType = varType.get()
            conn = sqlite3.connect('Punjab Meat Shop.db') 
            c = conn.cursor()

            c.execute("SELECT Meat_Part FROM Products WHERE Meat_Type = ?", (mType,))
            
            partResult = c.fetchall()

            meatPart = [ ]
        
            for meat in partResult:
                meatPart.append(meat[0])

            conn.commit()
            conn.close()
            varTypePart.set('Please Select...')

            popupMenuPart['values'] = meatPart
       
        def individualMeatPrice():
            mType = varType.get()
            mPart = varTypePart.get()
            conn = sqlite3.connect('Punjab Meat Shop.db') 
            c = conn.cursor()

            c.execute("SELECT Price FROM Products WHERE Meat_Type = ? AND Meat_Part = ?", (mType, mPart))

            priceResult = c.fetchall()

            meatPrice = [ ]
        
            for price in priceResult:
                meatPrice.append(price[0])
                
            mPrice = (meatPrice[0])

            return mPrice
        
            conn.commit()
            conn.close()
        
        meatType = ttk.Label(frame, text="Type of Meat:")
        meatType.grid(column=1, row=1, sticky=(N))
        varType = StringVar()
        choices = individualMeatType()
        varType.set('Please Select...')
        popupMenu = ttk.Combobox(frame, textvariable=varType)
        popupMenu['values'] = choices
        popupMenu.bind('<<ComboboxSelected>>', individualMeatPart)
        popupMenu.state(["readonly"])
        popupMenu.grid(column=3, row=1)
        
        meatPart = ttk.Label(frame, text="Part of Meat:")
        meatPart.grid(column=1, row=3, sticky=(N))
        varTypePart = StringVar()
        varTypePart.set('Please Select...')
        popupMenuPart = ttk.Combobox(frame, textvariable = varTypePart)
        popupMenuPart.state(["readonly"])
        popupMenuPart.grid(column=3, row=3)
               
        meatWeight = ttk.Label(frame, text="Weight of Meat:")
        meatWeight.grid(column=1, row=5, sticky=(N))
        weightEntry = ttk.Entry(frame)
        weightEntry.grid(column=3, row=5, sticky=(N))
        weightEntry.insert(END, "(kg)")

        def addButtonFunction():
            mT = varType.get()
            mP = varTypePart.get()
            mW = weightEntry.get()
            order = (mT, mP, mW, 'kg')
            if mT == 'Turkey':
                messagebox.showinfo("Error!", "Turkey orders can only be added on Promotions page.")
                buildOrders()
            elif checkNum(mW) == True: 
                confirm = messagebox.askquestion( "Are you sure you want to add this order?", order, icon='warning')
                if confirm == 'yes':
                    mPrice = individualMeatPrice()
                    mW = float(mW)
                    total = mPrice * mW
                    total = round(total, 2)
                    conn = sqlite3.connect('Punjab Meat Shop.db') 
                    c = conn.cursor()
                    c.execute("INSERT INTO Sales (Meat_Type, Meat_Part, Meat_Weight, Total) VALUES (?, ?, ?, ?)", (mT, mP, mW, total))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success!", "Your order was successfully added.")
                    buildOrders()
                else:
                    messagebox.showinfo("Unsuccessful!", "Your order was not added.")
                    buildOrders()
                
        addButton = ttk.Button(frame, text="Add Order", command=addButtonFunction)
        addButton.grid(column=4, row=6, sticky=(E))
        

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_rowconfigure(0, weight=2)
        content.grid_rowconfigure(2, weight=2)
        content.grid_rowconfigure(4, weight=2)
        content.grid_rowconfigure(6, weight=2)
        
    def createStock(frame):
        def addStock():
            changePage("addStock")
        #Creates content for stock page
        add = ttk.Button(frame, text="Add Stock", command=addStock)
        add.grid(column=1, row=0, sticky=(N))
        delete = ttk.Button(frame, text="Delete Stock")
        delete.grid(column=3, row=0, sticky=(N))
        view = ttk.Button(frame, text="View Stock")
        view.grid(column=5, row=0, sticky=(N), padx=5)

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_columnconfigure(6, weight=1)
        
    def stockAdd(frame):
        def individualMeatPart(event):
            mType = varType.get()
            conn = sqlite3.connect('Punjab Meat Shop.db') 
            c = conn.cursor()

            c.execute("SELECT Meat_Part FROM Products WHERE Meat_Type = ?", (mType,))
            
            partResult = c.fetchall()

            meatPart = [ ]
        
            for meat in partResult:
                meatPart.append(meat[0])

            conn.commit()
            conn.close()
            varTypePart.set('Please Select...')

            popupMenuPart['values'] = meatPart
            
        def individualMeatQuantity():
            mType = varType.get()
            mPart = varTypePart.get()
            conn = sqlite3.connect('Punjab Meat Shop.db') 
            c = conn.cursor()

            c.execute("SELECT Quantity FROM Products WHERE Meat_Type = ? AND Meat_Part = ?", (mType, mPart))

            quantityResult = c.fetchall()

            meatQuantity = [ ]
        
            for quantity in quantityResult:
                meatQuantity.append(quantity[0])
                
            mQuantity = (meatQuantity[0])

            return mQuantity
            conn.commit()
            conn.close()

        def individualMeatCost():
            mType = varType.get()
            mPart = varTypePart.get()
            conn = sqlite3.connect('Punjab Meat Shop.db') 
            c = conn.cursor()

            c.execute("SELECT Costs FROM Products WHERE Meat_Type = ? AND Meat_Part = ?", (mType, mPart))

            costResult = c.fetchall()

            meatCost = [ ]
        
            for cost in costResult:
                meatCost.append(cost[0])
                
            mCost = (meatCost[0])

            return mCost
            conn.commit()
            conn.close()
            
        meatType = ttk.Label(frame, text="Type of Meat:")
        meatType.grid(column=1, row=1, sticky=(N))
        varType = StringVar()
        choices = individualMeatType()
        varType.set('Please Select...')
        popupMenu = ttk.Combobox(frame, textvariable=varType)
        popupMenu['values'] = choices
        popupMenu.bind('<<ComboboxSelected>>', individualMeatPart)
        popupMenu.state(["readonly"])
        popupMenu.grid(column=3, row=1)
        
        meatPart = ttk.Label(frame, text="Part of Meat:")
        meatPart.grid(column=1, row=3, sticky=(N))
        varTypePart = StringVar()
        varTypePart.set('Please Select...')
        popupMenuPart = ttk.Combobox(frame, textvariable = varTypePart)
        popupMenuPart.state(["readonly"])
        popupMenuPart.grid(column=3, row=3)
        
        meatWeight = ttk.Label(frame, text="Weight of Meat:")
        meatWeight.grid(column=1, row=5, sticky=(N))
        weightEntry = ttk.Entry(frame)
        weightEntry.grid(column=3, row=5, sticky=(N))
        weightEntry.insert(END, "(kg)")

        cost = ttk.Label(frame, text="Total Cost: ")
        cost.grid(column=1, row=7, sticky=(N))
        costEntry = ttk.Entry(frame)
        costEntry.grid(column=3, row=7, sticky=(N))
        costEntry.insert(END, "(£)")
                
        def addButtonFunction():
            mT = varType.get()
            mP = varTypePart.get()
            mW = weightEntry.get()
            mC = costEntry.get()
            OldMQ = individualMeatQuantity()
            oldMeatCost = individualMeatCost()
            order = (mT, mP, mW, 'kg', 'for', '£', mC)
            if mT == 'Turkey':
                messagebox.showinfo("Error!", "Turkey stock can only be added on Promotions page.")
                buildStock()
            elif checkNum(mW) == True and checkNum(mC) == True: 
                confirm = messagebox.askquestion( "Are you sure you want to add this order?", order, icon='warning')
                if confirm == 'yes':
                    mType = varType.get()
                    mPart = varTypePart.get()
                    mW = float(mW)
                    mC = float(mC)
                    oldTotalMeatCost = oldMeatCost * OldMQ
                    newMQ = OldMQ + mW
                    newTotal = (oldMeatCost + mC) / newMQ
                    newTotal = round(newTotal, 2)
                    conn = sqlite3.connect('Punjab Meat Shop.db') 
                    c = conn.cursor()
                    c.execute("UPDATE Products SET Costs=?, Quantity=? WHERE Meat_Type = ? AND Meat_Part = ?", (newTotal, newMQ, mType, mPart))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success!", "Your order was successfully added.")
                    buildStock()
                else:
                    messagebox.showinfo("Unsuccessful!", "Your order was not added.")
                    buildStock()
                
        addButton = ttk.Button(frame, text="Add Stock", command=addButtonFunction)
        addButton.grid(column=4, row=8, sticky=(E))

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_rowconfigure(0, weight=2)
        content.grid_rowconfigure(2, weight=2)
        content.grid_rowconfigure(4, weight=2)
        content.grid_rowconfigure(6, weight=2)
        content.grid_rowconfigure(8, weight=2)

    def createFinances(frame):
        #Creates content for finances page
        profit = ttk.Button(frame, text="Profit:")
        profit.grid(column=1, row=1, sticky=(N))
        revenue = ttk.Button(frame, text="Revenue:")
        revenue.grid(column=1, row=3, sticky=(N))
        costs = ttk.Button(frame, text="Costs:")
        costs.grid(column=1, row=5, sticky=(N))

        content.grid_rowconfigure(0, weight=1)
        content.grid_rowconfigure(2, weight=1)
        content.grid_rowconfigure(4, weight=1)
        content.grid_rowconfigure(6, weight=1)
        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)

    def createCooler(frame):
        def capUtil():
            changePage("capUtil")
        def addCheck():
            changePage("addCheck")
        #Creates content for cooler page
        capUtil = ttk.Button(frame, text="Capacity Utilisation:", command=capUtil)
        capUtil.grid(column=1, row=1, sticky=(N))
        add = ttk.Button(frame, text="Add Check", command=addCheck)
        add.grid(column=1, row=3, sticky=(N))
        delete = ttk.Button(frame, text="Delete Check")
        delete.grid(column=3, row=3, sticky=(N))
        view = ttk.Button(frame, text="View Checks")
        view.grid(column=5, row=3, sticky=(N), padx=5)

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_columnconfigure(6, weight=1)
        content.grid_rowconfigure(0, weight=1)
        content.grid_rowconfigure(2, weight=1)
        content.grid_rowconfigure(4, weight=1)

    def createCapUtil(frame):
        meatType = ttk.Label(frame, text="Meat Type")
        meatType.grid(column=1, row=0, sticky=(N))

        meatPart = ttk.Label(frame, text="Meat Part")
        meatPart.grid(column=3, row=0, sticky=(N))

        currentCapacity = ttk.Label(frame, text="Current Capacity")
        currentCapacity.grid(column=5, row=0, sticky=(N))

        maximumCapacity = ttk.Label(frame, text="Maximum Capacity")
        maximumCapacity.grid(column=7, row=0, sticky=(N))

        capacityUtilisation = ttk.Label(frame, text="Capacity Utilisation")
        capacityUtilisation.grid(column=9, row=0, sticky=(N))

        backButton = ttk.Button(frame, text="Back")
        backButton.grid(column=0, row=7, sticky=(E,W), columnspan=11, ipady=5)

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_columnconfigure(6, weight=1)
        content.grid_columnconfigure(8, weight=1)
        content.grid_columnconfigure(10, weight=1)
        content.grid_rowconfigure(0, weight=1)
        content.grid_rowconfigure(2, weight=1)
        content.grid_rowconfigure(4, weight=1)
        content.grid_rowconfigure(6, weight=1)
        content.grid_rowconfigure(8, weight=1) 
    
    def createCheck(frame):
        water = ttk.Label(frame, text="Water: ")
        water.grid(column=1, row=1, sticky=(N))
        waterEntry = ttk.Entry(frame)
        waterEntry.grid(column=3, row=1, sticky=(N))
        waterEntry.insert(END, "(Litres)")

        temp = ttk.Label(frame, text="Temperature: ")
        temp.grid(column=1, row=3, sticky=(N))
        tempEntry = ttk.Entry(frame)
        tempEntry.grid(column=3, row=3, sticky=(N))
        tempEntry.insert(END, "(°C)")

        rating = ttk.Label(frame, text="Rating of Cleanliness: ")
        rating.grid(column=1, row=5, sticky=(N))
        ratingEntry = ttk.Entry(frame)
        ratingEntry.grid(column=3, row=5, sticky=(N))
        ratingEntry.insert(END, "(from 1 to 10)")

        time = ttk.Label(frame, text="Time Taken: ")
        time.grid(column=1, row=7, sticky=(N))
        timeEntry = ttk.Entry(frame)
        timeEntry.grid(column=3, row=7, sticky=(N))
        timeEntry.insert(END, "(Whole Minutes)")


        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_rowconfigure(0, weight=1)
        content.grid_rowconfigure(2, weight=1)
        content.grid_rowconfigure(4, weight=1)
        content.grid_rowconfigure(6, weight=1)
        content.grid_rowconfigure(8, weight=1)
        
    def createPromotions(frame):
        def promotionOrder():
            changePage("promotionOrder")
        def promotionStock():
            changePage("promotionStock")
        #Creates content for promotions page
        addOrder = ttk.Button(frame, text="Add Order", command=promotionOrder)
        addOrder.grid(column=1, row=0, sticky=(N))
        addStock = ttk.Button(frame, text="Add Stock", command=promotionStock)
        addStock.grid(column=3, row=0, sticky=(N))

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)

    def promotionOrderAdd(frame):
        def individualMeatPart(event):
            mType = varType.get()
            conn = sqlite3.connect('Punjab Meat Shop.db') 
            c = conn.cursor()

            c.execute("SELECT Meat_Part FROM Products WHERE Meat_Type = ?", (mType,))
            
            partResult = c.fetchall()

            meatPart = [ ]
        
            for meat in partResult:
                meatPart.append(meat[0])

            conn.commit()
            conn.close()
            varTypePart.set('Please Select...')

            popupMenuPart['values'] = meatPart
            
        meatType = ttk.Label(frame, text="Type of Meat:")
        meatType.grid(column=1, row=1, sticky=(N))
        varType = StringVar()
        choices = individualMeatType()
        varType.set('Please Select...')
        popupMenu = ttk.Combobox(frame, textvariable=varType)
        popupMenu['values'] = choices
        popupMenu.bind('<<ComboboxSelected>>', individualMeatPart)
        popupMenu.state(["readonly"])
        popupMenu.grid(column=3, row=1)
        
        meatPart = ttk.Label(frame, text="Part of Meat:")
        meatPart.grid(column=1, row=3, sticky=(N))
        varTypePart = StringVar()
        varTypePart.set('Please Select...')
        popupMenuPart = ttk.Combobox(frame, textvariable = varTypePart)
        popupMenuPart.state(["readonly"])
        popupMenuPart.grid(column=3, row=3)
        
        meatWeight = ttk.Label(frame, text="Weight of Meat:")
        meatWeight.grid(column=1, row=5, sticky=(N))
        weightEntry = ttk.Entry(frame)
        weightEntry.grid(column=3, row=5, sticky=(N))
        weightEntry.insert(END, "(kg)")

        price = ttk.Label(frame, text="Price of Meat: ")
        price.grid(column=1, row=7, sticky=(N))
        priceEntry = ttk.Entry(frame)
        priceEntry.grid(column=3, row=7, sticky=(N))
        priceEntry.insert(END, "(£)")
        
        def addButtonFunction():
            mT = varType.get()
            mP = varTypePart.get()
            mW = weightEntry.get()
            mPrice = priceEntry.get()
            order = (mT, mP, mW, 'kg', 'for', '£', mPrice)
            if checkNum(mW) == True and checkNum(mPrice) == True:
                confirm = messagebox.askquestion( "Are you sure you want to add this order?", order, icon='warning')
                if confirm == 'yes':
                    mPrice = float(mPrice)
                    mW = float(mW)
                    conn = sqlite3.connect('Punjab Meat Shop.db') 
                    c = conn.cursor()
                    c.execute("INSERT INTO Sales (Meat_Type, Meat_Part, Meat_Weight, Total) VALUES (?, ?, ?, ?)", (mT, mP, mW, mPrice))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success!", "Your order was successfully added.")
                    buildPromotions()
                else:
                    messagebox.showinfo("Unsuccessful!", "Your order was not added.")
                    buildPromotions()

                
        addButton = ttk.Button(frame, text="Add Order", command=addButtonFunction)
        addButton.grid(column=4, row=8, sticky=(E))

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_rowconfigure(0, weight=2)
        content.grid_rowconfigure(2, weight=2)
        content.grid_rowconfigure(4, weight=2)
        content.grid_rowconfigure(6, weight=2)
        content.grid_rowconfigure(8, weight=2)
        
    def promotionStockAdd(frame):
        meatType = ttk.Label(frame, text="Type of Meat:")
        meatType.grid(column=1, row=1, sticky=(N))
        typeEntry = ttk.Label(frame, text="Turkey")
        typeEntry.grid(column=3, row=1, sticky=(N))

        meatPart = ttk.Label(frame, text="Part of Meat:")
        meatPart.grid(column=1, row=3, sticky=(N))
        partEntry = ttk.Label(frame, text="Whole")
        partEntry.grid(column=3, row=3, sticky=(N))
        
        meatWeight = ttk.Label(frame, text="Weight of Meat:")
        meatWeight.grid(column=1, row=5, sticky=(N))
        weightEntry = ttk.Entry(frame)
        weightEntry.grid(column=3, row=5, sticky=(N))
        weightEntry.insert(END, "(kg)")

        cost = ttk.Label(frame, text="Total Cost: ")
        cost.grid(column=1, row=7, sticky=(N))
        costEntry = ttk.Entry(frame)
        costEntry.grid(column=3, row=7, sticky=(N))
        costEntry.insert(END, "(£)")
        
        def addButtonFunction():
            
            mW = weightEntry.get()
            mC = costEntry.get()
            order = ('Turkey', 'Whole', mW, 'kg', 'for', '£', mC)
            confirm = messagebox.askquestion( "Are you sure you want to add this stock?", order, icon='warning')
            if confirm == 'yes':
                messagebox.showinfo("Success!", "Your stock was successfully added.")
                buildPromotions()
            else:
                messagebox.showinfo("Unsuccessful!", "Your stock was not added.")
                buildPromotions()
                
        addButton = ttk.Button(frame, text="Add Stock", command=addButtonFunction)
        addButton.grid(column=4, row=8, sticky=(E))

        content.grid_columnconfigure(0, weight=1)
        content.grid_columnconfigure(2, weight=1)
        content.grid_columnconfigure(4, weight=1)
        content.grid_rowconfigure(0, weight=2)
        content.grid_rowconfigure(2, weight=2)
        content.grid_rowconfigure(4, weight=2)
        content.grid_rowconfigure(6, weight=2)
        content.grid_rowconfigure(8, weight=2)

    def logOutButton():
        root.destroy()

    def clearWindow():
        #Clears all the information inside the content frame
        for widget in Frame.winfo_children(content):
            widget.destroy()
        #Clears all the information inside titleFrame
        for widget in Frame.winfo_children(titleFrame):
            widget.destroy()

        content.grid_rowconfigure(0, weight=0)
        content.grid_rowconfigure(1, weight=0)
        content.grid_rowconfigure(2, weight=0)
        content.grid_rowconfigure(3, weight=0)
        content.grid_rowconfigure(4, weight=0)
        content.grid_rowconfigure(5, weight=0)
        content.grid_rowconfigure(6, weight=0)
        content.grid_rowconfigure(7, weight=0)
        content.grid_rowconfigure(8, weight=0)
        content.grid_rowconfigure(9, weight=0)
        content.grid_columnconfigure(0, weight=0)
        content.grid_columnconfigure(1, weight=0)
        content.grid_columnconfigure(2, weight=0)
        content.grid_columnconfigure(3, weight=0)
        content.grid_columnconfigure(4, weight=0)
        content.grid_columnconfigure(5, weight=0)
        content.grid_columnconfigure(6, weight=0)
        content.grid_columnconfigure(7, weight=0)
        content.grid_columnconfigure(8, weight=0)
        content.grid_columnconfigure(9, weight=0)
        content.grid_columnconfigure(10, weight=0)

    def createTitle(title):
        #Creates the title which will be inside titleFrame
        text = ttk.Label(titleFrame, text=title)
        text.grid(column=1, row=1)
        
    def changePage(page):
        clearWindow()
        if page == "Home":
            createTitle("Home")
            createHome(content)
        elif page == "Orders":
            createTitle("Orders")
            createOrders(content)
        elif page == "Stock":
            createTitle("Stock")
            createStock(content)
        elif page == "Finances":
            createTitle("Finances")
            createFinances(content)
        elif page == "Cooler":
            createTitle("Cooler")
            createCooler(content)
        elif page == "Promotions":
            createTitle("Promotions")
            createPromotions(content)
        elif page == "Logo":
            createTitle("Punjab Meat Shop")
            createLogo(content)
        elif page == "addOrder":
            createTitle("Add Order")
            createOrder(content)
        elif page == "addStock":
            createTitle("Add Stock")
            stockAdd(content)
        elif page == "capUtil":
            createTitle("Capacity Utilisation")
            createCapUtil(content)
        elif page == "addCheck":
            createTitle("Add Check")
            createCheck(content)
        elif page == "promotionOrder":
            createTitle("Add Order")
            promotionOrderAdd(content)
        elif page == "promotionStock":
            createTitle("Add Stock")
            promotionStockAdd(content)

    def buildHome():
        changePage("Home")

    def buildOrders():
        changePage("Orders")
        
    def buildStock():
        changePage("Stock")

    def buildFinances():
        changePage("Finances")

    def buildCooler():
        changePage("Cooler")

    def buildPromotions():
        changePage("Promotions")

    def buildLogo():
        changePage("Logo")

    #This code creates a smaller frame within the whole frame
    a = ttk.Style()
    a.configure('y.TFrame', background='yellow')
    s = ttk.Style()
    s.configure('TButton', background='blue', foreground='blue')
    main = ttk.Frame(root, padding = (15,15,15,15), style='y.TFrame', relief='sunken')
    main.grid(column=0, row=0, sticky=(N,E,S,W))

    #This gives the whole frame a weight so that it grows

    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    #Logo icon
    logoIcon = PhotoImage(file="Punjab Meat Shop Logo.gif")

    #This code creates all the buttons which are inside the main frame

    homeButton = ttk.Button(main, text="Home", command=buildHome)
    homeButton.grid(column=0, row=0, sticky=(N,E,S,W))

    orderButton = ttk.Button(main, text="Orders", command=buildOrders)
    orderButton.grid(column=0, row=1, sticky=(N,E,S,W))

    stockButton = ttk.Button(main, text="Stock", command=buildStock)
    stockButton.grid(column=0, row=2, sticky=(N,E,S,W))

    financeButton = ttk.Button(main, text="Finances", command=buildFinances)
    financeButton.grid(column=0, row=3, sticky=(N,E,S,W))

    coolerButton = ttk.Button(main, text="Cooler", command=buildCooler)
    coolerButton.grid(column=0, row=4, sticky=(N,E,S,W))

    promotionButton = ttk.Button(main, text="Promotions", command=buildPromotions)
    promotionButton.grid(column=0, row=5, sticky=(N,E,S,W))

    logoLabel = ttk.Button(main, image=logoIcon, command=buildLogo)
    logoLabel.grid(column=0, row=6, sticky=(E,W))


    main.grid_rowconfigure(6, weight=2) 

    #This code is for main page when program is opened
    titleFrame = ttk.Frame(main, padding = (5,5,5,5), relief='sunken')
    titleFrame.grid(column=1, row=0, sticky=(N,E,S,W), rowspan=2)
    titleFrame.grid_columnconfigure(1, weight=2)

    title = ttk.Label(titleFrame, text="Punjab Meat Shop")
    title.grid(column=1, row=0, sticky=(N))

    main.grid_columnconfigure(1, weight=2)

    #This is to create the content frame

    content = ttk.Frame(main, padding = (15,15,15,15), relief='sunken')
    content.grid(column=1, row=2, sticky=(N,E,S,W), rowspan=5)

    changePage("Logo")

    root.mainloop()



def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

'''

conn = sqlite3.connect('Login Data.db')
c = conn.cursor()

entryPass = 'pms1'

hashed_password = [hash_password(entryPass)]

c.execute("CREATE TABLE Data (Username TEXT, Password TEXT)")
c.execute("INSERT INTO Data (Username) VALUES ('PMS')")
c.execute("INSERT INTO Data (Password) VALUES (?)", (hashed_password))

conn.commit()
conn.close()

'''

#This code creates the whole frame
def buildLogin():
        
        login = Tk()
        login.minsize(width=800, height=350)

        #This code creates a smaller frame within the whole frame
        a = ttk.Style()
        a.configure('y.TFrame', background='yellow')
        s = ttk.Style()
        s.configure('TButton', background='blue', foreground='blue')
        v = ttk.Style()
        v.configure('TLabel', background='yellow')
        mainLogin = ttk.Frame(login, padding = (15,15,15,15), style='y.TFrame', relief='sunken')
        mainLogin.grid(column=0, row=0, sticky=(N,E,S,W))

        #This gives the whole frame a weight so that it grows

        login.grid_columnconfigure(0, weight=1)
        login.grid_rowconfigure(0, weight=1)


        def loginPage(frame):

            loginPageText = ttk.Label(frame, text= "Punjab Meat Shop")
            loginPageText.grid(column=1, row=1, sticky=(N))
            
            username = ttk.Label(frame, text="Username")
            username.grid(column=1, row=2, sticky =(N))

            usernameEntry = ttk.Entry(frame)
            usernameEntry.grid(column=1, row=3,sticky=(N))

            textpassword = ttk.Label(frame, text="Password")
            textpassword.grid(column=1, row=5, sticky =(N))

            entrypassword = ttk.Entry(frame, show='*')
            entrypassword.grid(column=1, row=6 , sticky=(N))
            
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_columnconfigure(2, weight=1)
            frame.grid_rowconfigure(0,weight=1)
            frame.grid_rowconfigure(1,weight=1)
            frame.grid_rowconfigure(4,weight=1)
            frame.grid_rowconfigure(7,weight=1)
            frame.grid_rowconfigure(9,weight=1)

            def checkLogin():
                conn = sqlite3.connect('Login Data.db')
                c = conn.cursor()
                c.execute('SELECT Username, Password FROM Data')
                users = c.fetchall()
                hashed = (users[1])
                passw = hashed[1]
                conn.close()
                
                entrypass = entrypassword.get()
                entryuser= usernameEntry.get()

        
                correctlogin = False
        
                for x in users:

                    if x[0] == entryuser:
                        if check_password(passw, entrypass):
                            correctlogin = True

                if correctlogin == True:
                    for widget in Frame.winfo_children(login):
                        login.destroy()
                    buildSystem()
                    
                else:
                    messagebox.showinfo('Incorrect Username or Password', 'Please enter the correct Username and Password')

            loginButton = ttk.Button(frame, text="Log In", command=checkLogin)
            loginButton.grid(column=1, row=8, sticky=(N))

        loginPage(mainLogin)
        login.mainloop()

buildLogin()

