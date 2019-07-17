from tkinter import *
from tkinter import ttk

#This code is to create the buttons

root = Tk()
root.minsize(width=500, height=200)

main = ttk.Frame(root, padding = (15,15,15,15))
main.grid(column=0, row=0, sticky=(N,E,S,W))

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

homeButton = ttk.Button(main, text="Home")
homeButton.grid(column=0, row=0, sticky=(N,E,S,W))

orderButton = ttk.Button(main, text="Orders")
orderButton.grid(column=0, row=1, sticky=(N,E,S,W))

stockButton = ttk.Button(main, text="Stock")
stockButton.grid(column=0, row=2, sticky=(N,E,S,W))

financeButton = ttk.Button(main, text="Finances")
financeButton.grid(column=0, row=3, sticky=(N,E,S,W))

coolerButton = ttk.Button(main, text="Cooler")
coolerButton.grid(column=0, row=4, sticky=(N,E,S,W))

promotionButton = ttk.Button(main, text="Promotions")
promotionButton.grid(column=0, row=5, sticky=(N,E,S,W))

logoLabel = ttk.Button(main, text="Logo")
logoLabel.grid(column=0, row=6, sticky=(E,W))


main.grid_rowconfigure(6, weight=2) 

#This code is for title

title = ttk.Label(main, text="Punjab Meat Shop")
title.grid(column=1, row=0, sticky=(N))

main.grid_columnconfigure(1, weight=2)

#This is for content frame

content = ttk.Frame(main, padding = (15,15,15,15))
content.grid(column=1, row=1, sticky=(N,E,S,W), rowspan=5)

textInContent = ttk.Button(content, text="asdhfl \nasldh \nsaldhf \nsldhf \nasdfh")
textInContent.grid(column=0, row=0, sticky=(N,E,S,W))

content.grid_rowconfigure(0, weight=2)
content.grid_columnconfigure(0, weight=2)
