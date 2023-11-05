import tkinter as tk
from tkinter import *
from tkinter import ttk


window = tk.Tk()  # instantiate an instance of a window
window.geometry("420x420")
window.title("EAFC24 Profit Calculator")

icon = PhotoImage(file="unnamed1.png")
window.iconphoto(True, icon)

label = tk.Label(window, text="EAFC24 Tax Calculator", font=("Arial, 18"))
label.pack(padx=20, pady=20)


def display_text():
    global buyPrice
    global sellPrice
    global numberPlayers
    sellPrice = int(sellPrice.get())
    buyPrice = int(buyPrice.get())
    numberPlayers = int(numberPlayers.get())
    string = int(sellPrice - (sellPrice * 0.05) - buyPrice) * numberPlayers
    label.configure(text=string)


# Initialize a Label to display the User Input
label = Label(window, text="", font=("Courier 22 bold"))
label.pack()


# Create an Entry widget to accept User Input
buyPrice = Entry(window, width=40)
sellPrice = Entry(window, width=40)
numberPlayers = Entry(window, width=40)
buyPrice.focus_set()
buyPrice.pack()
sellPrice.focus_set()
sellPrice.pack()
numberPlayers.focus_set()
numberPlayers.pack()


# Create a Button to validate Entry Widget
ttk.Button(window, text="Calculate Profit", width=20, command=display_text).pack(
    pady=20
)


window.mainloop()  # place window on computer screen, listen for events


# def userInput():
# buyPrice = int(input("Enter the buy price "))
# sellPrice = int(input("Enter the sell price "))
# numberPlayers = int(input("Enter the number of players "))
# profit = int((sellPrice - (sellPrice * 0.05)) - buyPrice) * numberPlayers
# print(profit)


# userInput()
