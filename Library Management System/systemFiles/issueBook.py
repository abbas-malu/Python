import datetime
import json
import os

from .dataObjects import *


def issueBook():
    bookId = input('Enter Book ID of the book to be issued: ')
    genre = bookId.split('_')[0]
    bookAvailable = False
    if os.path.exists(f'booksArea/{genre}/{bookId}.json'):
        with open(f'booksArea/{genre}/{bookId}.json', 'r') as bookFile:
            bookData = json.load(bookFile)
            if bookData['isAvailable']:
                bookAvailable = True
        if bookAvailable:
            issueDate = str(datetime.date.today())
            returnDate = str(datetime.date.today() + datetime.timedelta(days=30))
            issuer_ch = ''
            while type(issuer_ch) != int:
                try:
                    print('Press 1 if customer is member and 2 if not')
                    issuer_ch = int(input('>> '))
                except Exception:
                    print('Enter Valid Choice')
            if issuer_ch == 1:
                memberId = input('Enter member Id: ')
                Book.issueBook(bookId=bookId, issueDate=issueDate, returnDate=returnDate,
                            isMember=True, isReturned=False, memberId=memberId, issuerName=None)
            else:
                issuerName = input('Enter name of customer: ')
                Book.issueBook(bookId=bookId, issueDate=issueDate, returnDate=returnDate,
                            isMember=False, isReturned=False, memberId=None, issuerName=issuerName)
        else:
            print('Sorry, currently this book is not available.')
    else:
        print('Invalid Book Id.')
