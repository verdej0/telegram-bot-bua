#!/usr/bin/python
# -*- coding: utf-8 -*-

##TODO: Improve the next two lines

import sys
sys.path.append('Common/')

import requests
import re
import Utils
from bs4 import BeautifulSoup as bs

header = {'content-type': 'application/x-www-form-urlencoded'}
nameSearchForm = 'searchform'
nameNewSessionForm = 'loginform'
nameHitlistForm = 'hitlist'
urlBase = 'http://gaudi.ua.es'
firstAction = '/uhtbin/cgisirsi/x/x/0/49/'


class BUACrawler:

    def __init__(self):
        urlBua = urlBase + firstAction
        self.currentPage = requests.get(urlBua).content
        self.__urlScrapped = None
        self.__currentUrl = ''
        self.__isLogged = False

    def __getActionOfForm(self, formName):
        self.__urlScrapped = bs(self.currentPage, 'html.parser')
        forms = self.__urlScrapped.find_all('form')
        action = ''
        for form in forms:
            if form.attrs.get('name') == formName:
                action = form.attrs.get('action')
                break
        return action

    def __catalogLastPageIndex(self):
        self.__urlScrapped = bs(self.currentPage, 'html.parser')
        setOfP = self.__urlScrapped.find_all('p', {'class': 'searchsum'})
        bookSearchPages = []
        for p in setOfP:
            if 'href' in str(p):
                pages = p.find_all('a')
                if len(pages) == 3:
                    bookSearchPages = [1, 20]
                else:
                    last = (len(pages) - 2) * 20
                    bookSearchPages = [last - 19, last]
                break

        return bookSearchPages

    def searchBooks(self, bookName):

        ## Go to catalog menu section
        books = []
        self.__urlScrapped = bs(self.currentPage, 'html.parser')
        setOfTd = self.__urlScrapped.find_all('td', {'class': 'rootbarcell'})
        action = ''
        for td in setOfTd:
            if 'href' in str(td):
                action = td.find_all('a')[0].attrs.get('href')
                break

        if action == '':
            return books

        self.__currentUrl = urlBase + action
        self.currentPage = requests.get(self.__currentUrl).content

        action = self.__getActionOfForm(nameSearchForm)
        self.__currentUrl = urlBase + action
        payload = {
            'query_type': 'search',
            'searchdata1': bookName,
            'srchfield1': 'GENERAL^SUBJECT^GENERAL^^Todos los campos',
            'library': '',
            'sort_by': 'TI',
            }
        response = requests.post(self.__currentUrl, data=payload, headers=header)
        self.currentPage = response.content
        pagesIndex = self.__catalogLastPageIndex()
        numPages = 1
        if len(pagesIndex) == 2:
            numPages = pagesIndex[1]/20 + 1
        return [books, numPages, pagesIndex]

    def nextPageOfCatalog(self, indexPagination):
        booksData = []
        action = self.__getActionOfForm(nameHitlistForm)
        self.__currentUrl = urlBase + action
        payload = {'first_hit': indexPagination[0],
                    'last_hit': indexPagination[1],
                    'form_type': 'SCROLL^F'}
        response = requests.post(self.__currentUrl, data=payload,
                headers=header)
        self.currentPage = response.content
        ##TODO #booksData = extractBooksOfCurrentPage()

        return booksData

    def lastPageOfCatalog(self, indexPagination):
        booksData = []
        action = self.__getActionOfForm(nameHitlistForm)
        self.__currentUrl = urlBase + action
        payload = {'first_hit': indexPagination[0],
                    'last_hit': indexPagination[1],
                    'form_type': 'SCROLL^B'}
        response = requests.post(self.__currentUrl, data=payload,
                headers=header)
        self.currentPage = response.content
        
        ##TODO #booksData = extractBooksOfCurrentPage()
        return booksData

    def showLoans(self):

        # This enters in link 'Servios al usuario'
        books = []
        self.__urlScrapped = bs(self.currentPage, 'html.parser')
        setOfTd = self.__urlScrapped.find_all('td', {'class': 'rootbarcell'})
        action = ''
        for td in setOfTd:
            if 'href' in str(td):
                action = td.find_all('a')[-2].attrs.get('href')
                break

        if action == '':
            return books

        self.__currentUrl = urlBase + action
        self.currentPage = requests.get(self.__currentUrl).content

        # This enters in link 'Renovar Prestamos'
        self.__urlScrapped = bs(self.currentPage, 'html.parser')
        tables = self.__urlScrapped.find_all('table',
                {'class': 'defaultstyle'})
        action = tables[0].find_all('a')[-1].attrs.get('href')

        if action == '':
            return books

        self.__currentUrl = urlBase + action
        self.currentPage = requests.get(self.__currentUrl).content

        # Now, we're on loan page
        ##DELETE: Remove this line for production
        self.currentPage = Utils.testPage
        matches = re.finditer(Utils.regex, self.currentPage)
        for match in matches:
            books.append(match.groups())

        return books

    def loanSelectedBook(self):
        ##TODO
        pass

    def loanAllBooks(self):
        ##TODO
        pass

    def login(self, user, secret):
        action = self.__getActionOfForm(nameNewSessionForm)
        self.__currentUrl = urlBase + action
        payload = {'user_id': user, 'password': secret}
        response = requests.post(self.__currentUrl, data=payload, headers=header)
        self.currentPage = response.content

        ##TODO: Check if login is failed return False
        # if response.status == 200:
        #   self.isLogged = True

        return True

    def disconnect(self):
        self.__urlScrapped = bs(self.currentPage, 'html.parser')
        tables = self.__urlScrapped.find_all('table', {'class': 'gatewaystyle'})
        action = tables[0].find_all('a')[-1].attrs.get('href')
        self.__currentUrl = urlBase + action
        self.currentPage = requests.post(self.__currentUrl).content
        
        self.__isLogged = False
        self.__urlScrapped = None
        self.__currentUrl = urlBase + firstAction
        self.currentPage = requests.get(self.__currentUrl).content