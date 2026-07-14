from book_data import books
print("what are you going to do:\n1. see books list\n2. take out book\n 3. add new book\n4. search book by name (to choose type number or exit to stop)")
while True:
    user = input("which one: ")

    if user == "exit":
        break
    elif user == "1":
        for book in books:
            print(f"{book['name']} - {book['author']}, {book['year']}")
    elif user == "2":
        print("choose book: \n")
        for book in books:
            print(f"{book['name']} - {book['author']}, {book['year']}")
        book = input("Book name: ")
        found = False
        for b in books:
            if book in b["name"]:
                found = True
                if b['status']:
                    b["status"] = False
                    print(f"you take out book: {b['name']}")
                    break
                else:
                    print("book isn't available for now")
        if not found:
            print("this book isn't in library")
    elif user == "3":
        name = input("name: ")
        author = input("author: ")
        year = int(input("year: "))
        books.append({
            "name": name,
            "author": author,
            "year": year,
            "status": True
        })
    elif user == "4":
        found = False
        book = input("search book: ")
        for b in books:

            if book in b["name"]:
                found = True
                status = "Available" if b["status"] else "Borrowed"
                print(f"{b['name']} - {b['author']} ({b['year']}) | {status}")
        if not found:
            print("cant find book")
