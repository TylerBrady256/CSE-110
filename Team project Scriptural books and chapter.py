
sections = []
chapters = []
books=[]


with open("books_and_chapters.txt") as books_and_chapters:

    which_book = input("what book of scriptrue would you like to learn from? New Testament, Old Testament, Book of Mormon, Pearl of Great Price, or Docrtine and Covenants ")
    for i in  books_and_chapters:
        divided = i.split(":")
        
        if divided[2].lower().strip() == which_book.lower():
            sections.append(divided[2])
            chapters.append(int(divided[1])) 
            books.append(divided[0])
        
    
   


    highest = 0
    for chapter in chapters:
        if chapter > highest:
            highest = chapter 

    index_highest = chapters.index(highest)
    print (f"this is the book with the highest chapters {books[index_highest]} with {chapters[index_highest]} chapters")
    
    