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

    def disconnect(self):
        try:
            self.bua.disconnect()
            print 'Disconnect sucessful'
        except UnloggedUserException:
            print 'UnloggedUserException'

    def showLoans(self):
        try:
            print self.bua.showLoans()
        except UnloggedUserException:
            print 'UnloggedUserException'

    def searchBook(self, name):
            books = self.bua.searchBook(name)
            print books


    def nextPage(self):
        try:
            print self.bua.nextPage()
        except NoSearchException:
            print 'NoSearchException'
        except OnlyOnePageException:
            print 'OnlyOnePageException'

    def lastPage(self):
        try:
            print self.bua.lastPage()
        except NoSearchException:
            print 'NoSearchException'
        except OnlyOnePageException:
            print 'OnlyOnePageException'

    def loanSelectedBooks(self, selectedBooks):
        ##Check if the indexs of selected books are correct
        try:
            print self.bua.loanSelectedBooks(selectedBooks)
        except UnloggedUserException:
            print 'UnloggedUserException'

    def loanAllBooks(self):

        try:
            print self.bua.loanAllBooks()
        except UnloggedUserException:
            print 'UnloggedUserException'