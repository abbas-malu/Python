import os
from datetime import datetime

from .dataObjects import Book


def addNewBook(username):
    """
    Adding a New Book 
    """
    print('======Welcome to Add Book Wizard======')
    name = input('Enter Name of the book\n>> ')
    print()
    authorName = input('Enter Author Name of the book\n>> ')
    print()
    availableGenres = os.listdir('booksArea')
    if availableGenres == []:
        genre = input('Enter Genre of the book\n>> ')
    else:
        print()
        print('Following genres are available')
        for Genre in availableGenres:
            print(Genre)
        print()
        genre = input('Enter genre of the book from above list or enter a new one\n>> ').lower()
    print()
    price = '' 
    while type(price) != int:
        try:
            price = int(input('Enter price of the book\n>> '))
        except Exception:
            # e
            print('Enter a valid price')
            print()
    print()
    userGivenPublisher = input('Enter publisher of the book (optional)\n>> ')
    publisher = None if userGivenPublisher=='' else userGivenPublisher
    genreExists = True if genre in availableGenres else False
    newBook = Book(name=name,author=authorName,genre=genre,genreExists=genreExists,price=price,dateAdded=str(datetime.now()),addedBy=username,publisher=publisher)
    newBook.save()

# print(os.listdir('booksArea/'))

