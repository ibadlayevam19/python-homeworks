import csv
import json

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if len(self.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member cannot borrow more than 3 books.")
        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed.")
        self.borrowed_books.append(book)
        book.is_borrowed = True

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_borrowed = False

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.title] = book

    def add_member(self, member):
        self.members[member.name] = member

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book not found in the library.")
        self.members[member_name].borrow_book(self.books[book_title])

    def return_book(self, member_name, book_title):
        self.members[member_name].return_book(self.books[book_title])