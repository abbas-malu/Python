import json

class Book:
    def __init__(self, name: str, author: str, genre: str, price: int, publisher=None):
        self.name = name
        self.author = author
        self.genre = genre
        self.price = price
        self.publisher = publisher
    def save(self):
        """
        Saving The Book In The List
        """
        pass

class Admin():
    def __init__(self, name,email,username,password,role=None):
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
        with open(f'{self.username}.json', 'w') as user:
            user_obj = {'name':self.name,'email':self.email,'username':self.username,'password':self.password}
            json.dump(user_obj,user)