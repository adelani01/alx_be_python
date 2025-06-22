class Book:
    def __init__(self,title,author,is_checked_out = False):
        self.title = title
        self.author = author
        self.__is_checked_out = is_checked_out

    
    def check_out(self):
        if  not self.__is_checked_out:
            self.__is_checked_out = True
            return True
        return False
    
    def is_checked_out(self):
        return self.__is_checked_out
    
    def return_book(self):
        if  self.__is_checked_out:
            self.__is_checked_out = False
            return True
        return False
        

class Library:
    def __init__(self):
        self.__books = []

    def add_book(self,book):
            self.__books.append(book)

    def check_out_book(self,title):
       for books in self.__books:
            if books.title == title:
                return books.check_out()
       return False
    
    def return_book(self,title):
        for books in self.__books:
            if books.title == title and books.is_checked_out():
                  return books.return_book()
        return False
    
    def list_available_books(self):
        available_books = []
        for books in self.__books:
            if not books.is_checked_out():
                 available_books.append(books)
        return available_books
        
