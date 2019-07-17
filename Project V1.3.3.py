from tkinter import *
from tkinter import ttk

def createHome(frame):
    #Creates content for home page
    profit = ttk.Button(frame, text="Profit: ")
    profit.grid(column=1, row=1, sticky=(N))
    revenue = ttk.Button(frame, text="Revenue: ")
    revenue.grid(column=1, row=3, sticky=(N))
    noOfSales = ttk.Button(frame, text="Number of Sales: ")
    noOfSales.grid(column=1, row=5, sticky=(N))
    reorder = ttk.Button(frame, text="Reorder Quantity Level: ")
    reorder.grid(column=3, row=2, sticky=(N))
    capacityUtil = ttk.Button(frame, text="Capacity Utilisation: ")
    capacityUtil.grid(column=3, row=4, sticky=(N))
    
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
    #Creates content for orders page
    add = ttk.Button(frame, text="Add Order")
    add.grid(column=1, row=0, sticky=(N))
    delete = ttk.Button(frame, text="Delete Order")
    delete.grid(column=3, row=0, sticky=(N))
    view = ttk.Button(frame, text="View Orders")
    view.grid(column=5, row=0, sticky=(N), padx=5)

    content.grid_columnconfigure(0, weight=1)
    content.grid_columnconfigure(2, weight=1)
    content.grid_columnconfigure(4, weight=1)
    content.grid_columnconfigure(6, weight=1)

def createStock(frame):
    #Creates content for stock page
    text = ttk.Label(frame, text="Content for stock page")
    text.grid(column=0, row=0, sticky=(N))

def createFinances(frame):
    #Creates content for finances page
    text = ttk.Label(frame, text="Content for finances page")
    text.grid(column=0, row=0, sticky=(N))

def createCooler(frame):
    #Creates content for cooler page
    text = ttk.Label(frame, text="Content for cooler page")
    text.grid(column=0, row=0, sticky=(N))

def createPromotions(frame):
    #Creates content for promotions page
    text = ttk.Label(frame, text="Content for promotions page")
    text.grid(column=0, row=0, sticky=(N))

def logOutButton():
    root.destroy()

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
    

def clearWindow():
    #Clears all the information inside the content frame
    for widget in Frame.winfo_children(content):
        widget.destroy()
    #Clears all the information inside titleFrame
    for widget in Frame.winfo_children(titleFrame):
        widget.destroy()

def createTitle(title):
    #Creates the title which will be inside titleFrame
    text = ttk.Label(titleFrame, text=title)
    text.grid(column=1, row=1)

def setTitle(root, title):
    #Creates the window title
    root.title(title)
    
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

def buildSystem():

    #This code creates the whole frame
    global root
    root = Tk()
    root.minsize(width=800, height=350)
    setTitle(root,"Punjab Meat Shop")

    #Idle Timer
    import time

    global started
    started = time.time()

    def checkIdle():
        current = time.time()
        print(current)
        timer = current - started
        if timer > 10:
            buildLogo()
        else:
            root.after(1000, checkIdle)

    def key(event):
        print ("Movement at", event.x, event.y)
        global started
        started = time.time()

    checkIdle()

    root.bind("<Motion>", key)
    
    global content, titleFrame, main

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

    textInContent = ttk.Label(content, text="Content for 'Punjab Meat Shop' logo page")
    textInContent.grid(column=0, row=0, sticky=(N))

    content.grid_rowconfigure(0, weight=2)
    content.grid_columnconfigure(0, weight=2)

    root.mainloop()

buildSystem()
