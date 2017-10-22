#!/usr/bin/python
# -*- coding: utf-8 -*-


##TODO: Improve the next two lines
import sys
sys.path.append("Bot/")


#from Bot import BUABot
 

def main():
    buaBot = BUABot()
    buaBot.login('0XXXXXXXX', 'YYYY')
    buaBot.showLoans()


if __name__=='__main__':
    main()