#!/usr/bin/python
# -*- coding: utf-8 -*-

##TODO: Improve the next two lines

import sys
sys.path.append('Crawler/')
sys.path.append('Model/Exceptions/')

from BUACrawler import BUACrawler
from BUALoanBooks import BUALoanBooks
from BUACatalog import BUACatalog
from LoginException import InvalidCredentialsException, UnloggedUserException, AlreadyLoggedUserException
from CatalogException import NoSearchException, OnlyOnePageException


class BUA:

    def __init__(self):
        self.crawler = BUACrawler()
        self.catalog = BUACatalog()
        self.__loansBooks = BUALoanBooks()

        self.__isOnCatalog = False
        self.isLogged = False
        self.__isRenovatingBooks = False

    def login(self, user, secret):
        if not self.isLogged:
            self.isLogged = self.crawler.login(user, secret)
            if not self.isLogged:
                raise InvalidCredentialsException()
        else:
            raise AlreadyLoggedUserException()

    def disconnect(self):
        if not self.isLogged:
            raise UnloggedUserException()

        self.crawler.disconnect()    
        self.isLogged = True
        self.__isOnCatalog = False
        self.__isRenovatingBooks = False
    

    def showLoans(self):
        self.__isOnCatalog = False
        self.catalog.clean()
        self.__loansBooks.clean()
        if not self.isLogged:
            raise UnloggedUserException()

        self.__isRenovatingBooks = True
        self.__loansBooks.setBooks(self.crawler.showLoans())
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
        dataForBookSearched = self.crawler.searchBook(name)
        self.catalog.setBooks(dataForBookSearched[0])
        self.catalog.page = 1
        self.catalog.numPages = dataForBookSearched[1]
        self.catalog.pageIndexs = dataForBookSearched[2]
        self.__isOnCatalog = True
        return self.catalog.books

    def stepBackward(self):
        self.crawler.stepBackward()

    def localizationsForBook(self, viewId):
        if not self.__isOnCatalog:
            raise NoSearchException()
        locations = self.crawler.localizationsForBook(viewId, self.catalog.page)
        self.stepBackward()
        return locations

    def nextPage(self):
        if not self.__isOnCatalog:
            raise NoSearchException()
        
        if self.catalog.numPages==1:
            raise OnlyOnePageException()

        if self.catalog.page < self.catalog.numPages:
            self.catalog.page += 1
            self.catalog.setBooks(self.crawler.nextPageOfCatalog(self.catalog.pageIndexs))

        return self.catalog.books
        

    def lastPage(self):

        if not self.__isOnCatalog:
            raise NoSearchException()

        if self.catalog.numPages==1:
            raise OnlyOnePageException()
        
        if self.catalog.page > 1:
            self.catalog.page -= 1
            self.catalog.setBooks(self.crawler.nextPageOfCatalog(self.catalog.pageIndexs))
        return self.catalog.books