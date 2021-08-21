# Public.py --> Vlad Usatii @ youshould.readproduct.com
# -*- coding: utf-8 -*-

# regex and os
import sys, os, time, re

# scrape
from requests import get
from bs4 import BeautifulSoup
from urllib.request import urlopen

class Public(object):
	def __init__(self, username: str):
		# name
		self.username = username.replace(' ', '-')
		self.names = username.split()
		self.firstname = self.names[0]
		if len(self.names) == 2:
			self.lastname = self.names[1]
		elif len(self.names) == 3:
			self.middlename = self.names[1]
			self.lastname = self.names[2]
		elif len(self.names) > 3:
			self.lastname == self.names[-1]

		# source code
		self.url = f'https://www.quora.com/{self.username}'
		self.response = self.Rget()

		# returns 200 if account found : else status code
		self.status = int(re.sub("[^0-9]", "", str(get(self.url))))

		self.scrape_headers = {
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'
			'AppleWebKit/537.36 (KHTML, like Gecko)'
			'Chrome/64.0.3282.167 Safari/537.36'
		}

	# core functions

	def sub(self, response: str) -> int:
		return re.sub("[^0-9]", "", response)

	# self.response == Rget()
	def Rget(self): 
		url = self.url
		return get(url).text

	# int parse
	def intparser(self, newresp: str, text: str, skipLen = 8) -> int:
		skip = newresp.find(text) + len(text)
		parsed = self.sub(newresp[skip:skip + skipLen])
		return parsed

	def boolparser(self, newresp: str, text: str, skipLen = 8) -> bool:
		skip = newresp.find(text) + len(text)
		halfparse = newresp[skip:skip + skipLen]
		if 'true' in halfparse:
			return True
		else:
			return False

	def asciiparser(self, text: str, find: str, skipLen = 8) -> str:
		pass

	# library functions

	def followingcount(self) -> int:
		newresp = get(self.url).text # must include new func call every time
		return self.intparser(newresp, '\\"followingCount\\":')

	def followercount(self) -> int:
		newresp = get(self.url).text # must include new func call every time
		return self.intparser(newresp, '\\"followerCount\\":')

	def viewcount(self) -> int:
		newresp = get(self.url).text # must include new func call every time
		return self.intparser(newresp, '\\"viewCount\\":')

	def lastmonthviews(self) -> int:
		newresp = get(self.url).text # must include new func call every time
		return self.intparser(newresp, '\\"lastMonthPublicContentViews\\"')

	def answercount(self) -> int:
		newresp = get(self.url).text # must include new func call every time
		return self.intparser(newresp, '\\"numPublicAnswers\\"')

	def questioncount(self) -> int:
		newresp = get(self.url).text # must include new func call every time
		return self.intparser(newresp, '\\"numProfileQuestions\\":')

	def questionshares(self) -> int:
		newresp = get(self.url).text # must include new func call every time
		return self.intparser(newresp, '\\"quoraSharesCount\\":')

	## more complex calls

	def userdescription(self) -> str:
		user = self.username
		# non-raw source code
		url = urlopen(f'http://www.quora.com/{self.username}/').read()
		soup = BeautifulSoup(url, 'html.parser')
		match = soup.find('meta', attrs={'name': 'description'})
		print(match) # returns None for some reason, probably a GraphQL patch

	def questions(self) -> str: # returns json
		user = self.username
		pass

	def totalanswerstousersquestions(self) -> int:
		url = self.url + '/questions/'
		response = get(url).text

		pass

	# . . .

	def isblocked(self) -> bool:
		newresp = get(self.url).text # clean func call
		return self.boolparser(newresp, '\\"isUserBanned\\":', 6)

	def isFlagged(self, flags = None) -> bool:
		newresp = get(self.url).text # clean func call
		if flags is not None and flags == 'BOTH':
			if self.boolparser(newresp, '\\"isFlaggedForFakeName\\":') == False:
				t = False
				print(f'Flagged for Fake Name: {t}; Account is active')
			else:
				t = True
				print(f'Flagged for Fake Name: {t}; Account is inactive')
			if self.boolparser(newresp, '\\"isFlaggedForBadName\\":') == False:
				t = False
				print(f'Flagged for Bad Name: {t}; Account is active')
			else:
				t = True
				print(f'Flagged for Bad Name: {t}; Account is disabled for bad name')
		if flags == None:
			if self.boolparser(newresp, '\\"isFlaggedForFakeName\\":') == False and self.boolparser(newresp, '\\"isFlaggedForBadName\\":') == False:
				print("All returned not flagged")
				return False
			else:
				print("One or more returned flagged")
				return True
		return 'done'
