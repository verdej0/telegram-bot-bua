#!/usr/bin/python
# -*- coding: utf-8 -*-

##TODO: Improve the next two lines

import sys
sys.path.append('Services/')
sys.path.append('Model/Exceptions/')

from BUAService import BUAService
from BUALoanBooks import BUALoanBooks
from BUACatalog import BUACatalog
from LoginException import InvalidCredentialsException, UnloggedUserException, AlreadyLoggedUserException


class BUA:

    def __init__(self):
        self.bua = BUAService()
        self.catalog = BUACatalog()
        self.loansBooks = BUALoanBooks()

        self.isOnCatalog = False
        self.isLogged = False
        self.isRenovatingBooks = False

    def login(self, user, secret):
        if not self.isLogged:
            self.isLogged = self.bua.login(user, secret)
            if not self.isLogged:
                raise InvalidCredentialsException()
        else:
            raise AlreadyLoggedUserException()

    def showLoans(self):
        self.isOnCatalog = False
        self.loansBooks.clean()
        if not self.isLogged:
            raise UnloggedUserException()

        self.isRenovatingBooks = True
        self.loansBooks.setBooks(self.bua.showLoans())
        return self.loansBooks.books

    def loanSelectedBooks(self, selectedBooks):

        if not self.isLogged:
            raise UnloggedUserException()

        # #TODO

        print 'loanSelectedBooks'

    def loanAllBooks(self):

        if not self.isLogged:
            raise UnloggedUserException()

        # #TODO

        print 'loanAllBooks'

    def searchBook(self, name):
        self.isRenovatingBooks = False
        books = self.bua.searchBooks(name)
        self.isOnCatalog = True
        return books

    def nextPage(self):
        if not self.isOnCatalog:
            print 'You need to seach a book before do that'

        print 'nextPage'

    def lastPage(self):
        if not self.isOnCatalog:
            print 'You need to seach a book before do that'