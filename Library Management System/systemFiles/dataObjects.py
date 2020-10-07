import json
import os


class Book:
    def __init__(self, name: str, author: str, genre: str, genreExists: bool, price: int, dateAdded: str,addedBy:str, publisher=None):
        self.name = name
        self.author = author
        self.genre = genre
        self.price = price
        self.dateAdded = dateAdded
        self.genreExists = genreExists
        self.publisher = publisher
        if self.genreExists:
            noOfBooks = len(os.listdir(f'booksArea/{self.genre}'))
        else:
            os.mkdir(f'booksArea/{self.genre}')
            noOfBooks = 0
        self.bookId = self.genre + '_00' + str(noOfBooks+1) 
        self.addedBy = addedBy

    def save(self):
        """
        Saving The Book In The List
        """
        with open(f"booksArea/{self.genre}/{self.bookId}.json",'w') as bookFile:
            newBook = {
                'bookId':self.bookId,
                'name': self.name,
                'author':self.author,
                'genre':self.genre,
                'price':self.price,
                'dateAdded':self.dateAdded,
                'addedBy':self.addedBy,
                'publisher':self.publisher,
                'isAvailable':True,
                }
            json.dump(newBook,bookFile)


class Admin():
    def __init__(self, name, email, username, password, role=None):
        """
        Creating a new Admin.
        """
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.role = role

    def save(self):
        """
        Saving the Admin
        """
        with open(f'adminArea/admins/{self.username}.json', 'w') as user:
            user_obj = {'name': self.name, 'email': self.email,
                        'username': self.username, 'password': self.password}
            json.dump(user_obj, user)

    @staticmethod
    def isAdminValid(username, passowrd):
        """
        Checking Validity Of Admin
        """
        if os.path.exists(f'adminArea/admins/{username}.json'):
            with open(f'adminArea/admins/{username}.json', 'r') as admin_data:
                data = json.load(admin_data)
                if data['password'] == passowrd:
                    with open('adminArea/log.json', 'w') as log:
                        logs = {'logged_in': True, 'username': data['name']}
                        json.dump(logs, log)
                    return [True, data['name']]
                else:
                    return [False, 'Wrong Password']
        else:
            return [False, 'Admin Not Exists']

    @staticmethod
    def isAdminLogged():
        """
        Checking Login Status
        """
        with open('adminArea/log.json') as logFile:
            log = json.load(logFile)
            if log['logged_in'] == True:
                return [True, log['username']]
            else:
                return [False, ]

    @staticmethod
    def logout():
        """
        Logout Admin Superuser
        """
        with open('adminArea/log.json', 'w') as log:
            logs = {'logged_in': False, 'username': None}
            json.dump(logs, log)
