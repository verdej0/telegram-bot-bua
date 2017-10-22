#!/usr/bin/python
# -*- coding: utf-8 -*-

##TODO: Improve the next two lines
import sys
sys.path.append("Bot/")

from Bot import BUABot

##TODO: Change the content of these variables by yours BUA credials. Only for testing. Remember to erase it when you push a change in the repo.
username = '0XXXXXXXX'
secret = 'YYYY'


def main():
    buaBot = BUABot()
    buaBot.login(username, secret) 
    buaBot.showLoans()


if __name__=='__main__':
    main()