from tkinter import *
from tkinter import ttk


def createHome(frame):
    #Creates content for home page
    text = Label(frame, text="Content for home page")
    text.grid(column=0, row=0, sticky=(N))
    
def createOrders(frame):
    #Creates content for orders page
    text = Label(frame, text="Content for orders page")
    text.grid(column=0, row=0, sticky=(N))

def createStock(frame):
    #Creates content for stock page
    text = Label(frame, text="Content for stock page")
    text.grid(column=0, row=0, sticky=(N))

def createFinances(frame):
    #Creates content for finances page
    text = Label(frame, text="Content for finances page")
    text.grid(column=0, row=0, sticky=(N))

def createCooler(frame):
    #Creates content for cooler page
    text = Label(frame, text="Content for cooler page")
    text.grid(column=0, row=0, sticky=(N))

def createPromotions(frame):
    #Creates content for promotions page
    text = Label(frame, text="Content for promotions page")
    text.grid(column=0, row=0, sticky=(N))

def createLogo(frame):
    #Creates content for logo page
    text = Label(frame, text="Content for 'Punjab Meat Shop' logo page")
    text.grid(column=0, row=0, sticky=(N))
    

def clearWindow():
    #Clears all the information inside the content frame
    for widget in Frame.winfo_children(content):
        widget.destroy()
    #Clears all the information inside titleFrame
    for widget in Frame.winfo_children(titleFrame):
        widget.destroy()

def createTitle(title):
    #Creates the title which will be inside titleFrame
    text = Label(titleFrame, text=title)
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

#This code creates the whole frame

root = Tk()
root.minsize(width=500, height=250)
setTitle(root,"Punjab Meat Shop")

#This code creates a smaller frame within the whole frame

main = ttk.Frame(root, padding = (15,15,15,15))
main.grid(column=0, row=0, sticky=(N,E,S,W))

#This gives the whole frame a weight so that it grows

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

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

logoLabel = ttk.Button(main, text="Logo", command=buildLogo)
logoLabel.grid(column=0, row=6, sticky=(E,W))


main.grid_rowconfigure(6, weight=2) 

#This code is for main page when program is opened

titleFrame = ttk.Frame(main, padding = (5,5,5,5))
titleFrame.grid(column=1, row=0, sticky=(N,E,S,W), rowspan=2)
titleFrame.grid_columnconfigure(1, weight=2)

title = ttk.Label(titleFrame, text="Punjab Meat Shop")
title.grid(column=1, row=0, sticky=(N))

main.grid_columnconfigure(1, weight=2)

#This is to create the content frame

content = ttk.Frame(main, padding = (15,15,15,15))
content.grid(column=1, row=2, sticky=(N,E,S,W), rowspan=5)

textInContent = ttk.Label(content, text="Content for 'Punjab Meat Shop' logo page")
textInContent.grid(column=0, row=0, sticky=(N))

content.grid_rowconfigure(0, weight=2)
content.grid_columnconfigure(0, weight=2)
