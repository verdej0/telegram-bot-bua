#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Book:

    def __init__(self, data):
        
        self.title = ''
        self.author = ''
        self.returnDate = ''

        if len(data) > 0:
            self.title = data[0]
        if len(data) > 1:
            self.author = data[1]
        if len(data) > 2:
            self.returnDate = data[2]

    def __toString(self):
        info = ''
        if not self.title == '':
            info += self.title
        if not self.author == '':
            info += '|' + self.author
        if not self.returnDate == '':
            info += '|' + self.returnDate
        return info

    def __str__(self):
        return self.__toString()

    # ##DOC: Python2 and Python3 compatibility
    def __repr__(self):
        return self.__toString()