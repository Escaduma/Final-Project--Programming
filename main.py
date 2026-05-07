from tkinter import *
from tkinter import messagebox

book=Tk()
book.title("Book Database")
book.geometry("600x400")

textLabel=Label(book, text="Welcome to Your Personal Library", font=("Brush Script MT", 30))
textLabel.pack()

leftFrame=Frame(book)
leftFrame.pack(side="left", fill="y", padx=20)

addBookButton=Button(leftFrame, text="Add Book", width=20, height=2, font=("Brush Script MT", 20), bg="pink", activebackground="hotpink", activeforeground="black", bd=1, relief="solid")
addBookButton.grid(row=0, column=0, pady=10)

remBookButton=Button(leftFrame, text="Remove Book", width=20, height=2, font=("Brush Script MT", 20), bg="pink", activebackground="hotpink", activeforeground="black", bd=1, relief="solid")
remBookButton.grid(row=1, column=0, pady=10)

recBookButton=Button(leftFrame, text="Recommend a Book", width=20, height=2, font=("Brush Script MT", 20), bg="pink", activebackground="hotpink", activeforeground="black", bd=1, relief="solid")
recBookButton.grid(row=2, column=0, pady=10)

rightPanel = Frame(book, bg="#f0f0f0", width=400, height=400)
rightPanel.pack(side="left", fill="both", expand=True, padx=20, pady=20)


book.mainloop()