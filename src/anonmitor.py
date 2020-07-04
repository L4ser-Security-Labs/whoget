#!/usr/bin/python

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



from mechanize import Browser
try:
	import urllib2 as u
except:
	import urllib.request as u

class tor(object):
	def __init__(self):
		pass

	def connect(self):
		def renew_tor():
			import socket

			s = socket.socket()
			s.connect(('localhost', 9050))

			s.send(b'AUTHENTICATE "123"\r\n')
			resp = s.recv(1024)

			if resp.startswith(b'250'):
				s.send("signal NEWNYM\r\n")
				resp = s.recv(1024)
				if resp.startswith('250'):
					print ("TOR Identity Renewed")
				else:
					print (resp.decode('UTF-8','ignore'))
			else:
				print (resp.decode('UTF-8','ignore'))

		try:
			renew_tor()
			import socks
			import socket
			import mechanize
			from mechanize import Browser

			def create_connection(address, timeout=None, source_address=None):
				sock = socks.socksocket()
				sock.connect(address)
				return sock

			socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)

			# patch the socket module
			socket.socket = socks.socksocket
			socket.create_connection = create_connection

			br = Browser()
			print ("[!] Changed identity to " + br.open('http://icanhazip.com').read().decode('UTF-8','ignore'))

		except Exception as e:
			print(" [-] " + str(e))
			print(" [!] " + "Is TOR running on 127.0.0.1:9050 ?")
			exit()

class conn(object):
	def __init__(self, target, agent):
		self.target = target
		self.agent = agent

	def HTTPcode(self):
		try:
			if self.agent == True:
				br = Browser()
				UserAgent = "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
				header = {"User-Agent" : UserAgent}
				br.set_handle_robots(False)
				br.addheaders = [("User-agent", "Fifefox")]
				
				resp = br.open(self.target).code
			else:
				resp = u.urlopen(self.target).getcode()
			return(resp)
		except (u.HTTPError, u.URLError):
			return(404)
	
	def redirect(self):
		try:
			if self.agent == True:
				br = Browser()
				UserAgent = "Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0"
				header = {"User-Agent" : UserAgent}
				br.set_handle_robots(False)
				br.addheaders = [("User-agent", "Fifefox")]
				
				remote_url = br.open(self.target).geturl()
			else:
				remote_url = u.urlopen(self.target).geturl()
			return(remote_url)
		except Exception as e:
			print(e)
