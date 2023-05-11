'''
Program name: SDEV 140 Final Project
Author name: Kevin Sims
Date last modified: May 10, 2023
Purpose: As an introduction to GUI, I am trying to develop a simple app that could be used to initiate the development of
a food product.  The app asks the user to choose a protein, fat and carbohydrate source as starting points for the product 
'''


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("SDEV 140 Final Project - Sims")

#creating and locating the title label
fpd = Label(root, text="          Food Product Design (FPD)          ", padx=70, pady=20, fg="blue", bg="yellow")
fpd.grid(row=0, column=2)

#creating and locating the contact information label 
contact = Label(root, text="Question?  Contact FPD \n 812-555-1234", padx=50, pady=20)
contact.grid(row=11, column=0)

#creating and locating the career opportunities label
career = Label(root, text="FPD Career Opportunities \n 812-555-5678", padx=50, pady=20)
career.grid(row=11, column=3)



#creating the functions for the three buttons.  These functions when called will open a new window with 3 radio buttons that display appropriate options for that ingredient category.
#The new window also has a "close window" button that when clicked will close the window and return the user to the root window.

def prot():
    p = IntVar() #declaring an integer variable "p" so that the radio buttons will not show as selected when the window is first opened
    top1 = Toplevel() #creating a variable "top1" that will open a new window that is not associated with the root window
    top1.title("Protein Options") #creating a title for the new window that reflects the ingredient category and the options available
    Radiobutton(top1, text="Beef", variable=p, value=1).pack(anchor=W)
    Radiobutton(top1, text="Pork", variable=p, value=2).pack(anchor=W)
    Radiobutton(top1, text="Chicken", variable=p, value=3).pack(anchor=W)
    close_prot = Button(top1, text="Close window", command=top1.destroy, padx=10, pady=10).pack(anchor=E) #creating the "Close window" button that when clicked will return the user to the root window.

#the end of line comments made for the prot function above apply to the fat and cho functions below as well.  Only changes are related specifically to the ingredient category.  
def fat():
    f = IntVar() 
    top2 = Toplevel()
    top2.title("Fat Options")
    Radiobutton(top2, text="Soy Oil", variable=f, value=1).pack(anchor=W)
    Radiobutton(top2, text="Corn Oil", variable=f, value=2).pack(anchor=W)
    Radiobutton(top2, text="Sunflower Oil", variable=f, value=3).pack(anchor=W)
    close_fat = Button(top2, text="Close window", command=top2.destroy, padx=10, pady=10).pack(anchor=E)

def cho():
    c = IntVar()
    top3 = Toplevel()
    top3.title("Carbohydrate Options")
    starch = Radiobutton(top3, text="Corn Starch", variable=c, value=1).pack(anchor=W)
    malto = Radiobutton(top3, text="Maltodextrin", variable=c, value=2).pack(anchor=W)
    sucrose = Radiobutton(top3, text="Sucrose", variable=c, value=3).pack(anchor=W)
    close_cho = Button(top3, text="Close Window", command=top3.destroy, padx=10, pady=10).pack(anchor=E)


#creating the three key buttons in the root window that can be clicked to access the functions above
protein = Button(root, text="Choose a protein", padx=50, pady=10, command=prot)
fat = Button(root, text="Choose a fat", padx=50, pady=10, command=fat)
cho = Button(root, text="Choose a carbohydrate", padx=50, pady=10, command=cho)

#locating the three key buttons in the root window
protein.grid(row=5, column=0) 
fat.grid(row=5, column=2) 
cho.grid(row=5, column=3)

#creating and locating the "exit program" button in the root window.  When clicked the button exits the program AND closes the root window
btn_exit = Button(root, text="Exit Program", command=root.destroy, padx=50, pady=10)
btn_exit.grid(row=15, column=3)


#adding two images to the root window using a Label widget.  Image locations determined by trial & error after getting all the other widgets in the root window
fruit = ImageTk.PhotoImage(Image.open("c:/images/fruit.png"))
vegetable = ImageTk.PhotoImage(Image.open("c:/images/vegetables.png"))

fruitLabel = Label(image=fruit)
vegLabel = Label(image=vegetable)

fruitLabel.grid(row=0, column=0)
vegLabel.grid(row=0, column=3)


#root.geometry("800x400") #used initially to set the size of the root window so I could visually see the various labels, buttons and images (width x height).  
root.mainloop()

