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

from sys import path, argv
import argparse
import phonenumbers
path.append("src")
import phone 
import search
import social
import anonmitor


parser = argparse.ArgumentParser(description = "OSINT tool for Nigerian phone numbers",\
				add_help = False)

parser.add_argument("-h", "--help", help = "Shows this message and exits",\
			action = "store_true")

parser.add_argument("-p", help = "Phone number starting with +234", 
                    type = str)

parser.add_argument("-g", help = "Search information using search engines.",
                    type = str, choices=['google', 'duckduckgo'])

parser.add_argument("-s", help = "Find information on social media", 
                    type = str, choices=['twitter', 'facebook'])

parser.add_argument("-t", help = "Use tor for anonymity",  action = "store_true")

args = parser.parse_args()

def check_tor():
    if args.t:
        if anonmitor != False:
            anonmitor.tor().connect()
            return True
        else:
            pass

if __name__ == "__main__":
	import banner
	
	if len(argv) <= 1:
		parser.print_help()
		exit()
	else:
		if args.help == True:
			parser.print_help()
			exit()
		else:
			if args.p == None:
				parser.print_help()
				print("\nWhoGet: error: argument -p is required\n")
				exit()
			else:
				pass
	print("\n")
	print("*" * 75)
	
	if args.p[:4] != "+234":
		print("\nWhoGet: error: Phone number doesn't start with +234\n")
		parser.print_help()
		exit()	
	elif args.p[:4] == "+234":
		ngnumber = args.p

	if args.p:
		check_tor()
		# if args.t:
		# 	if anonmitor != False:
		# 		anonmitor.tor().connect()
		# 	else:
		# 		pass
		allinfo = phone.allinfo(ngnumber)
		print ("-" * 30)
		print ("[!] Phone number information")
		print ("-" * 30)
		for key, val in allinfo.items():
			print ("[✓]", key.title(), "=>", val) 
		if args.g == 'google':
			results = search.Google(ngnumber)
			for dic in results:
				print ("[✓]", dic['title'].title(), "=>", dic['link']) 
			exit()
		if args.g == 'duckduckgo':
			results = search.DuckDuckGo(ngnumber)
			exit()
		if args.s == 'twitter':
			results = social.twitter(ngnumber)
			if len(results) != 0:
				print("{} Tweets found! ".format(len(results)))
				for tweet in results: 
					print ("[✓] Tweeted on", tweet[0], "=>", "https://twitter.com/i/web/status/{}".format(tweet[1])) 	
			elif len(results) == 0: 
				print("No tweet found")
			exit()
		if args.s == 'facebook':
			results = social.fbook(ngnumber)
			if len(results) != 0:
				print("{} Facebook Page found! ".format(len(results)))
				for page in results: 
					print ("[✓] Name", "=>", page["name"], 
							"\n\t[.] Street: => {}, {}, {}".format(page['location']['street'], page['location']['city'], page['location']['country']), 
							"\n\t[.] Map: => https://maps.google.com/?q={},{}".format(page['location']['latitude'],page['location']['longitude']),
							"\n\t[.] Link: => {}".format(page['link']))
			elif len(results) == 0: 
				print("No result found")
			exit()
