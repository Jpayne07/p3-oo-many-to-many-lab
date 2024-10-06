
class Author:
    all=[]
    def __init__(self, name=""):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
            

    def books(self):
        return [contract.book for contract in Contract.all if  contract.author == self]
            

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        Contract.all.append(contract)
        return contract
    
    def total_royalties(self):
        amount_of_royalties = 0
        for contract in Contract.all:
            if contract.author == self:
                amount_of_royalties += contract.royalties
        return amount_of_royalties
        
    
class Book:
    all=[]
    def __init__(self, title = ""):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
            
    def authors(self):           
        return [contract.author for contract in Contract.all if contract.book == self]

    

class Contract:
    all = []

    def __init__(self, author, book, date="", royalties=0):
        self._author = None
        self._book = None
        self._date = None
        self._royalties = None

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception('The contract author is not of class Author')

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception('The contract book is not of class Book')

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception("The date is not of type string")

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise Exception("The royalties is not of type int")

    @classmethod    
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


author = Author("Jacob")
book = Book("Title")
contract = Contract(author, book, '01/01/2001', 50000)

# for contract in contract.all:
# print(contract.all[0].author.name)
print(author.books())