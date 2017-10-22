#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Book import Book


class BUACatalog:

    def __init__(self):
        self.clean()

    def clean(self):
        self.books = []
        self.page = 0
        self.pageIndexs = []
        self.numPages = 0

    def setBooks(self, dataBooks):
        self.books = []
        for book in dataBooks:
            self.books.append(Book(book))