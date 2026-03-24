library = {}

# 1. Add Book
def add_book():
    book_id = input("Enter Book ID: ")
    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    library[book_id] = {"name": name, "author": author, "issued": False}
    print("Book added!\n")

# 2. View Books
def view_books():
    if len(library) == 0:
        print("No books in library\n")
    else:
        for i in library:
            print("ID:", i)
            print("Name:", library[i]["name"])
            print("Author:", library[i]["author"])
            print("Issued:", library[i]["issued"])
            print("------")
    print()

# 3. Search Book
def search_book():
    name = input("Enter book name: ")
    for i in library:
        if library[i]["name"] == name:
            print("Book Found:", library[i])
            return
    print("Book not found\n")

# 4. Issue Book
def issue_book():
    book_id = input("Enter Book ID: ")
    if book_id in library:
        if library[book_id]["issued"] == False:
            library[book_id]["issued"] = True
            print("Book issued\n")
        else:
            print("Already issued\n")
    else:
        print("Book not found\n")

# 5. Return Book
def return_book():
    book_id = input("Enter Book ID: ")
    if book_id in library:
        library[book_id]["issued"] = False
        print("Book returned\n")
    else:
        print("Book not found\n")

# 6. Delete Book
def delete_book():
    book_id = input("Enter Book ID: ")
    if book_id in library:
        del library[book_id]
        print("Book deleted\n")
    else:
        print("Book not found\n")

# 7. Menu
def menu():
    while True:
        print("1.Add  2.View  3.Search  4.Issue  5.Return  6.Delete  7.Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            issue_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            delete_book()
        elif choice == "7":
            break
        else:
            print("Invalid choice\n")

menu()