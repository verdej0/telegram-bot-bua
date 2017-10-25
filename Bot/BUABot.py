#!/usr/bin/env python
# -*- coding: utf-8 -*-

#verdej0 added a string return with the success, error or the data

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
        text=''
        print('TUPUTAMADRE')
        try:
            self.__bua.login(user, secret)
            text+= 'Login sucessful'
        except InvalidCredentialsException:
            text+= 'InvalidCredentialsException'
        except AlreadyLoggedUserException:
            text+= 'AlreadyLoggedUserException'
        return text

    def disconnect(self):
        text=''
        try:
            self.__bua.disconnect()
            text= 'Disconnect sucessful'
        except UnloggedUserException:
            text= 'UnloggedUserException'
        
        return text

    def showLoans(self):
        text=''
        try:
            text= self.__bua.showLoans()
        except UnloggedUserException:
            text= 'UnloggedUserException'
        return text

    def searchBook(self, name):
            text=''
            books = self.__bua.searchBook(name)
            if len(books)==0:
                text = 'No books found'
            else:

                text = books
            return text

    def localizationForBook(self, idBook):
        text=''
        try:
            locations = self.__bua.localizationsForBook(idBook)
            text = locations
        except NoSearchException:
            text= 'NoSearchException'
        except BookIndexOutbound:
            text = 'BookIndexOutbound'
        return text

    def nextPage(self):
        text=''
        try:
            books = self.__bua.nextPage()
            text= books
        except NoSearchException:
            text= 'NoSearchException'
        except OnlyOnePageException:
            text= 'OnlyOnePageException'
        return text

    def lastPage(self):
        text=''
        try:
            books = self.__bua.lastPage()
            text= books
        except NoSearchException:
            text= 'NoSearchException'
        except OnlyOnePageException:
            text= 'OnlyOnePageException'

        return text

    def loanAllBooks(self):
        text=''
        try:
            text= self.__bua.loanAllBooks()
        except UnloggedUserException:
            text= 'UnloggedUserException'
        return text 


