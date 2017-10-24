#!/usr/bin/env python
# -*- coding: utf-8 -*-


##TODO: Improve the next two lines
import sys
sys.path.append("Model/")


from BUA import BUA
from LoginException import InvalidCredentialsException, UnloggedUserException, AlreadyLoggedUserException
from CatalogException import NoSearchException, OnlyOnePageException, BookIndexOutbound


##TODO: Add timeout for disconnect, for example, 15min...
class BUABot:

    def __init__(self):
        self.__bua = BUA()
        
    def login(self, user, secret):
        try:
            self.__bua.login(user, secret)
            print 'Login sucessful'
        except InvalidCredentialsException:
            print 'InvalidCredentialsException'
        except AlreadyLoggedUserException:
            print 'AlreadyLoggedUserException'

    def disconnect(self):
        try:
            self.__bua.disconnect()
            print 'Disconnect sucessful'
        except UnloggedUserException:
            print 'UnloggedUserException'

    def showLoans(self):
        try:
            print self.__bua.showLoans()
        except UnloggedUserException:
            print 'UnloggedUserException'

    def searchBook(self, name):
            books = self.__bua.searchBook(name)
            if len(books)==0:
                print 'No books found'
            else:
                print books

    def localizationForBook(self, idBook):
        try:
            locations = self.__bua.localizationsForBook(idBook)
            print locations
        except NoSearchException:
            print 'NoSearchException'
        except BookIndexOutbound:
            print 'BookIndexOutbound'

    def nextPage(self):
        try:
            books = self.__bua.nextPage()
            print books
        except NoSearchException:
            print 'NoSearchException'
        except OnlyOnePageException:
            print 'OnlyOnePageException'

    def lastPage(self):
        try:
            books = self.__bua.lastPage()
            print books
        except NoSearchException:
            print 'NoSearchException'
        except OnlyOnePageException:
            print 'OnlyOnePageException'

    def loanAllBooks(self):
        try:
            print self.__bua.loanAllBooks()
        except UnloggedUserException:
            print 'UnloggedUserException'



