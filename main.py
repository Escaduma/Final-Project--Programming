# Imports for the graphical interface and button functions
from tkinter import *
from tkinter import messagebox
from ButtonFunctions import showAddBookForm, showRemoveBookForm, showRecommendation, showBookList

# Main window setup
book=Tk()
book.title("Book Database")
book.geometry("1200x800")
book.config(bg="#FFE4E1")

# Welcome label at the top
textLabel=Label(book, text="Welcome to Your Personal Library", font=("Brush Script MT", 30), bg="#FFE4E1")
textLabel.pack()

# Left panel where buttons are placed
leftFrame=Frame(book, bg="#FFE4E1")
leftFrame.pack(side="left", fill="y", padx=20)

# Button to open the Add Book form
addBookButton=Button(leftFrame, text="Add Book", width=20, height=2, font=("Brush Script MT", 20), bg="pink", activebackground="hotpink", activeforeground="black", bd=1, relief="solid", command=lambda: showAddBookForm(rightPanel))
addBookButton.grid(row=0, column=0, pady=10)

# Button to open the Remove Book form
remBookButton=Button(leftFrame, text="Remove Book", width=20, height=2, font=("Brush Script MT", 20), bg="pink", activebackground="hotpink", activeforeground="black", bd=1, relief="solid", command=lambda: showRemoveBookForm(rightPanel))
remBookButton.grid(row=1, column=0, pady=10)

# Button to open the Recommendation form
recBookButton=Button(leftFrame, text="Recommend a Book", width=20, height=2, font=("Brush Script MT", 20), bg="pink", activebackground="hotpink", activeforeground="black", bd=1, relief="solid", command=lambda: showRecommendation(rightPanel))
recBookButton.grid(row=2, column=0, pady=10)

# Right panel where content is displayed when a button is clicked
rightPanel = Frame(book, bg="#FFE4E1", width=400, height=400)
rightPanel.pack(side="left", fill="both", expand=True, padx=20, pady=20)
bg = PhotoImage(file="info/libros.png") # Default background image for the right panel
bgLabel = Label(rightPanel, image=bg)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
bgLabel.image = bg

# Button to show the full book list
showBooksButton = Button( 
    leftFrame, text="Show Books", width=20, height=2,
    font=("Brush Script MT", 20), bg="pink",
    activebackground="hotpink", activeforeground="black",
    bd=1, relief="solid",
    command=lambda: showBookList(rightPanel))
showBooksButton.grid(row=3, column=0, pady=10)

# Start the main loop
book.mainloop()