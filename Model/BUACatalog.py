#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Book import Book


class BUACatalog:

    def __init__(self):
        self.clean()

    def clean(self):
        self.books = []
        self.page = 1
        self.pageIndexs = []

    def setPageIndexs(self, pageIndexs):
        self.pageIndexs = pageIndexs

    def setPage(self, page):
        self.page = page

    def setBooks(self, dataBooks):
        for book in dataBooks:
            self.books.append(Book(book))