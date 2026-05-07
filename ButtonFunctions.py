from openpyxl import load_workbook
from tkinter import *
from tkinter import messagebox
from main import rightPanel

def addBook(title, author, genre, year, description):
    workbook=load_workbook("BooksList.xlsx")
    sheet=workbook.active

    row=[title, author, genre, year, description]
    sheet.append(row)
    workbook.save("BooksList.xlsx")
    messagebox.showinfo("Saved", "Your book has been saved!!")

def clearRightPanel():
    for widget in rightPanel.winfo_children():
        widget.destroy()

def showAddBookForm():
    clearRightPanel()

    Label(rightPanel, text="Add a Book", font=("Brush Script MT", 16), bg="#f40808").pack(pady=10)

    titleEntry=Entry(rightPanel, width=30)
    titleEntry.pack(pady=5)
    titleEntry.insert(0, "Book Title")

    authorEntry = Entry(rightPanel, width=30)
    authorEntry.pack(pady=5)
    authorEntry.insert(0, "Author")

    genreEntry = Entry(rightPanel, width=30)
    genreEntry.pack(pady=5)
    genreEntry.insert(0, "Genre")

    yearEntry = Entry(rightPanel, width=30)
    yearEntry.pack(pady=5)
    yearEntry.insert(0, "Year")

    descriptionEntry = Entry(rightPanel, width=30)
    descriptionEntry.pack(pady=5)
    descriptionEntry.insert(0, "Description")

    def save():
        addBook(
            titleEntry.get(),
            authorEntry.get(),
            genreEntry.get(),
            yearEntry.get(),
            descriptionEntry.get()
        )

    Button(rightPanel, text="Save", bg="pink", command=save).pack(pady=10)