## Final Project
## May 11, 2026
## Title: My personal Library

# Description:
    The program was designed to manage the books that you have in your house using a graphical interface, meaning that the user can add, remove, and view the books saved in an Excel file, it also recommends book based on genre and read status.

# Installation:
    The libraries openpyxl, tkinter, and random are needed

# Usage:
    1. Run the file main.py
    2. Use the buttons on the left panel to navigate
    3. Add books by filling out the form and clicking Save
    4. View your books, remove them, or get a recommendation

# Features:
    -Add books with title, author, genre, year, and description
    -Mark books as already read with a checkboox
    -Remove books by title
    -Views all saved books with their read status
    -Get book recommendations filtered by genre and read status

# Testing:
    -Add a book and verify it appears in the Book List
    -Mark a book as Read and check the status in the book list
    -Remove a book and verify it not longer appears in the Book List
    -Use the Recommendation filter with a genre and verify only matching books appear.
    -Try remmoving a book that does not exist and verify the warning message appears

# Files:
    ~main.py: Main window and buttons
    ~ButtonFunctions.py: Functions for each button
    ~info/BooksList.xlsx: Excel file where books are stored
    ~info/: Folder containing images and the Excel File
    ~starterCode/: Original code before AI assistance

# Author:
    Macie Escalera-Duron