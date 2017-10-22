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
from CatalogException import NoSearchException, OnlyOnePageException


class BUA:

    def __init__(self):
        self.service = BUAService()
        self.catalog = BUACatalog()
        self.__loansBooks = BUALoanBooks()

        self.__isOnCatalog = False
        self.isLogged = False
        self.__isRenovatingBooks = False

    def login(self, user, secret):
        if not self.isLogged:
            self.isLogged = self.service.login(user, secret)
            if not self.isLogged:
                raise InvalidCredentialsException()
        else:
            raise AlreadyLoggedUserException()

    def showLoans(self):
        self.__isOnCatalog = False
        self.catalog.clean()
        self.__loansBooks.clean()
        if not self.isLogged:
            raise UnloggedUserException()

        self.__isRenovatingBooks = True
        self.__loansBooks.setBooks(self.service.showLoans())
        return self.__loansBooks.books

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
        self.catalog.clean()
        self.__loansBooks.clean()
        self.__isRenovatingBooks = False
        dataForBookSearched = self.service.searchBooks(name)
        self.catalog.setBooks(dataForBookSearched[0])
        self.catalog.page = 1
        self.catalog.numPages = dataForBookSearched[1]
        self.catalog.pageIndexs = dataForBookSearched[2]
        self.__isOnCatalog = True
        return self.catalog.books

    def nextPage(self):
        if not self.__isOnCatalog:
            raise NoSearchException()
        
        if self.catalog.numPages==1:
            raise OnlyOnePageException()

        self.catalog.setBooks(self.service.nextPageOfCatalog())
        return self.catalog.books
        

    def lastPage(self):

        if not self.__isOnCatalog:
            raise NoSearchException()

        if self.catalog.numPages==1:
            raise OnlyOnePageException()
        
        self.catalog.setBooks(self.service.lastPageOfCatalog())    
        return self.catalog.books