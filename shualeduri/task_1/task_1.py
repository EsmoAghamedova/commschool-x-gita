from book_data import books

print("========= Mini Library =========")
print("1. Show books")
print("2. Borrow books")
print("3. Add books")
print("4. Search books")
print(f"Type (exit) to quit")
print("================================")

while True:
    user = input("which one: ")

    if user == "exit":
        break
    elif user == "1":
        for book in books:
            status = "Available" if book["status"] else "Borrowed"
            print(f"{book['name']} - {book['author']}, {book['year']} | {status}")
    elif user == "2":
        print("choose book: \n")
        for book in books:
            print(f"{book['name']} - {book['author']}, {book['year']}")
        book = input("Book name: ")
        found = False
        for b in books:
            if book in b["name"]:
                found = True
                if not b['status']:
                    print("book isn't available for now")
                    break
                else:
                    b["status"] = False
                    print(f"you take out book: {b['name']}")
                    break

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
        print("Book added successfully!")
    elif user == "4":
        found = False
        book = input("search book: ")
        for b in books:

            if book.lower() in b["name"].lower():
                found = True
                status = "Available" if b["status"] else "Borrowed"
                print(f"{b['name']} - {b['author']} ({b['year']}) | {status}")
        if not found:
            print("cant find book")
