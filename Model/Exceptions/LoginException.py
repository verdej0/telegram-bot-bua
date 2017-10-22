#!/usr/bin/env python
# -*- coding: utf-8 -*-

class InvalidCredentialsException(Exception):
    pass

class UnloggedUserException(Exception):
    pass

class AlreadyLoggedUserException(Exception):
    pass