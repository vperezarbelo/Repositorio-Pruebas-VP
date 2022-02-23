'''books = {
    "Life of Pi": "Adventure Fiction", 
    "The Three Musketeers": "Historical Adventure",
    "Watchmen": "Comics", 
    "Bird Box": "Horror",
    "Harry Potter":"Fantasy Fiction",
    "Good Omens": "Comedy"
}

book = input("Escribe un título: ")

#change this part to use the .get() method
#if(book in books):
 #   print(books[book])
#else:
#    print("Book not found")
x = books.get(book, "Book not found")
print(x)'''
def suma_cinco(x):
    return (x+5)
nums = [11, 22, 33, 44, 55]
result = (map(suma_cinco))
