#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Book import Book


class BUALoanBooks:

    def __init__(self):
        self.clean()

    def clean(self):
        self.books = []

    def setBooks(self, dataBooks):
        for book in dataBooks:
            self.books.append(Book(book))
