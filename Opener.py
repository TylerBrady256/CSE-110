with open("books.txt") as books_files:
    for lines in books_files:
        print(lines.strip())