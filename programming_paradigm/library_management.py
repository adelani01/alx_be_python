class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.__is_checked_out = False

    def check_out_book(self):
        if  self.__is_checked_out == False:
            self.__is_checked_out = True
            return True
        else:
            return False
        
    def is_checked_out(self):
        return self.__is_checked_out
    
    def return_book(self):
        if  self.__is_checked_out == True:
            self.__is_checked_out = False
            return True
        else:
            return False
        
            

class Library:
    def __init__(self):
        self._books = []
        

    def add_book(self,book):
            self._books.append(book)
            return True
    
    def check_out_book(self,title):
        for each_books in self._books:
            if each_books.title == title:
                return each_books.check_out_book()
        return False
        
    def return_book(self,title):
        for each_books in self._books:
            if each_books.title == title:
                if  each_books.is_checked_out():
                    return each_books.return_book()
        
        return False
        
    def list_available_books(self):
        available_books = []
        for each_books in self._books:
            if  not each_books.is_checked_out():
                available_books.append(each_books)

        return available_books
            

            
          