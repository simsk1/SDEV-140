'''
Program name: SDEV 140 Final Project
Author name: Kevin Sims
Date last modified: April 30, 2023
Purpose: As an introduction to GUI, I am trying to develop a simple app that could be used to initiate the development of
a food product.  The app asks the user to choose a protein, fat and carbohydrate source.  
'''


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("SDEV 140 Final Project - Sims")

#creating and locating the title of the gui application
fpd = Label(root, text="          Food Product Design          ", padx=70, pady=20, fg="blue", bg="yellow")
fpd.grid(row=0, column=0, columnspan=600)

#creating the buttons
protein = Button(root, text="Choose a protein", pady=10)
fat = Button(root, text="Choose a fat", pady=10)
cho = Button(root, text="Choose a carbohydrate", pady=10)

#locating the buttons
protein.grid(row=5, column=10) 
fat.grid(row=7, column=10) 
cho.grid(row=9, column=10) 


#adding two images to the root window using a Label widget. Will worry about location later.
fruit = ImageTk.PhotoImage(Image.open("c:/images/fruit.png"))
vegetable = ImageTk.PhotoImage(Image.open("c:/images/vegetables.png"))

fruitLabel = Label(image=fruit)
vegLabel = Label(image=vegetable)

fruitLabel.grid(row=11, column=1)
vegLabel.grid(row=13, column=3)


root.geometry("800x800") #setting the 'default' size of the window to see everything for now (width x height)
root.mainloop()

