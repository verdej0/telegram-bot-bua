#!/usr/bin/env python
# -*- coding: utf-8 -*-


##TODO: Improve the next two lines
import sys
sys.path.append("../Model/")
sys.path.append("../Model/Exceptions/")


from BUA import BUA
from LoginException import InvalidCredentialsException, UnloggedUserException, AlreadyLoggedUserException


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