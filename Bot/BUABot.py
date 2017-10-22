#!/usr/bin/env python
# -*- coding: utf-8 -*-


##TODO: Improve the next two lines
import sys
sys.path.append("Model/")


from BUA import BUA
from LoginException import InvalidCredentialsException, UnloggedUserException, AlreadyLoggedUserException
from CatalogException import NoSearchException, OnlyOnePageException


##TODO: Add timeout for disconnect, for example, 15min...
class BUABot:

    def __init__(self):
        self.bua = BUA()
        
    def login(self, user, secret):
        try:
            self.bua.login(user, secret)
            print 'Login sucessful'
        except InvalidCredentialsException:
            print 'InvalidCredentialsException'
        except UnloggedUserException:
            print 'UnloggedUserException'
        except AlreadyLoggedUserException:
            print 'AlreadyLoggedUserException'

    def showLoans(self):
        try:
            books = self.bua.showLoans()
        except UnloggedUserException:
            print 'UnloggedUserException'

    def searchBook(self, name):
            self.bua.searchBook(name)

    def nextPage(self):
        try:
            self.bua.nextPage()
        except NoSearchException:
            print 'NoSearchException'
        except OnlyOnePageException:
            print 'OnlyOnePageException'

    def lastPage(self):
        try:
            self.bua.lastPage()
        except NoSearchException:
            print 'NoSearchException'
        except OnlyOnePageException:
            print 'OnlyOnePageException'

    def loanSelectedBooks(self, selectedBooks):
        ##Check if the indexs of selected books are correct
        try:
            self.bua.loanSelectedBooks(selectedBooks)
        except UnloggedUserException:
            print 'UnloggedUserException'

    def loanAllBooks(self):

        try:
            self.bua.loanAllBooks()
        except UnloggedUserException:
            print 'UnloggedUserException'
