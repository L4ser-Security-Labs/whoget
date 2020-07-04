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


import requests
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

def Google(ngnumber):
	"""Google search"""
	print ("-" * 30)
	print("[!] Searching on Google...")
	print ("-" * 30)
	query = "inurl:" + ngnumber
	URL = "https://www.google.com/search?q=%s&num=50&start=0" % query.replace("+", "%2B")	
	headers = {"user-agent": USER_AGENT}
	try:
		resp = requests.get(URL, headers=headers)
		print (resp.status_code )
		if resp.status_code == 200:
			soup = BeautifulSoup(resp.content, "html.parser")
		results = []
		for g in soup.find_all('div', class_='r'):
			anchors = g.find_all('a')
			if anchors:
				link = anchors[0]['href']
				title = g.find('h3').text
				item = {
					"title": title,
					"link": link
				}
				results.append(item)
		return results
	except Exception as e:
		print("err",e)

def DuckDuckGo(ngnumber):
    """DuckDuckGo search"""
    print ("-" * 30)
    print("[!] Searching on DuckDuckGo...")
    print ("-" * 30)
    try:
        query = ngnumber
        URL = "https://html.duckduckgo.com/html/?q=%s" % query.replace("+", "%2B")	
        headers = {"user-agent": USER_AGENT}
        resp = requests.get(URL, headers=headers)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
        results = []
        for results in soup.findAll("div", attrs={"class":"results"}):
            for title in results.findAll("a", attrs={"class":"result__a"}):
                t = title.text
                t = t.title()
                
            for link in results.findAll("a", attrs={"class":"result__url"}):
                l = link.get("href")
                print ("[✓] Found",l) 
        pass
        
    except Exception as e:
        print(e)