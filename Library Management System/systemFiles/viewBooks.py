import json
import os 
import tabulate

def listBooks():
    """
    Listing all the available books
    """
    genreList = os.listdir('booksArea/')
    for genre in genreList:
        bookList = os.listdir(f'booksArea/{genre}')
        # genre = genre.capitalize()
        print(f'{genre} Books')
        bookDetails = []
        for book in bookList:
            with open(f'booksArea/{genre}/{book}','r') as bookFile:
                bookData = json.load(bookFile)
                bookDetails.append([
                    bookData['bookId'],
                    bookData['name'],
                    bookData['author'],
                    bookData['price'],
                    bookData['dateAdded'],
                    bookData['addedBy'],
                    bookData['publisher'],
                    bookData['isAvailable'],
                ])
        print(tabulate.tabulate(bookDetails,
        headers=[
            'Book-ID',
            'Name',
            'Author',
            'price',
            'Date Added',
            'Added By',
            'Published By',
             'Available For Issue?',
            ]))
        print()
        print()


