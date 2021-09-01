# Ryan von Lutzow
# AR
# 8-31-21

from tkinter import *
#from PIL import ImageTk, Image
#import os

iconPath = "Files\sus.ico"
imagePath = "Files\CM.png"

def Button1Click():
    pass
def Button2Click():
    pass
def Button3Click():
    pass
def Button4Click():
    pass
def Button5Click():
    print("Exiting Program... ")
    exit(0)

root = Tk()
root.iconbitmap(iconPath)
root.title("DGS, LLC Customer Sales Database")

#img = ImageTk.PhotoImage(Image.open(imagePath))
#panel = tk.Label(root, image=img)
#panel.pack(side="bottom", fill="both", expand="yes")

#Entry1 = Entry(root)
#Entry1.grid(column=1, row=1)

EmptyLabel1 = Label(root, text="")
EmptyLabel1.grid(column=1, row=0)
Label1 = Label(root, text="DGS, LLC", font=("Arial", 25))
Label1.grid(column=0, row=1)
Label2 = Label(root, text="Customer Sales", font=("Arial", 25))
Label2.grid(column=1, row=1)
Label3 = Label(root, text="Database", font=("Arial", 25))
Label3.grid(column=2, row=1)
EmptyLabel2 = Label(root, text="")
EmptyLabel2.grid(column=1, row=2)

Button1 = Button(root, command=Button1Click, text="Customers", width=25, height=5, bg="black", fg="orange")
Button1.grid(column=0, row=3)
Button2 = Button(root, command=Button2Click, text="Products", width=25, height=5, bg="black", fg="orange")
Button2.grid(column=1, row=3)
Button3 = Button(root, command=Button3Click, text="Sales", width=25, height=5, bg="black", fg="orange")
Button3.grid(column=2, row=3)
Button4 = Button(root, command=Button4Click, text="Reports", width=25, height=5, bg="black", fg="orange")
Button4.grid(column=0, row=4)
Button5 = Button(root, command=Button5Click, text="Exit", width=25, height=5, bg="black", fg="orange")
Button5.grid(column=2, row=4)

root.mainloop()
