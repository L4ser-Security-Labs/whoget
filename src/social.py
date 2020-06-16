#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "L4ser Secruity Labs"
__DATE__	= "15/06/2020"
__VERSION__	= "0.0.1"
__GITHUB__	= "https://github.com/L4ser-Security-Labs"

'''OSINT tool  for Nigerian Phone numbers'''

"""
    Copyright (C) 2020 L4ser Security Labs
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
"""

import urllib
import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

def twitter(ngnumber):
	"""Twitter search"""
	print ("-" * 30)
	print("[x] Twitter not yet supported...")
	print ("-" * 30)

def instagram(ngnumber):
    """Instagram search"""
    print ("-" * 30)
    print("[x] Instagram not yet supported...")
    print ("-" * 30)

def facebook(ngnumber):
    """Facebook search"""
    print ("-" * 30)
    print("[x] Facebook not yet supported...")
    print ("-" * 30)
	
