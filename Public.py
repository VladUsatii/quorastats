#!/usr/bin/env python3
# Public.py --> Vlad Usatii @ youshould.readproduct.com
import sys, os, time, re
from requests import get

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
		self.response = get(self.url).text

		# returns 200 if account found : else status code
		self.status = int(re.sub("[^0-9]", "", str(get(self.url))))

	# core functions

	def sub(self, response: str) -> int:
		return int(re.sub("[^0-9]", "", response))

	# int parse
	def intparser(self, text: str, skipLen = 8) -> int:
		skip = self.response.find(text) + len(text)
		parsed = self.sub(self.response[skip:skip + skipLen])
		return parsed

	def boolparser(self, text: str, skipLen = 8) -> bool:
		skip = self.response.find(text) + len(text)
		halfparse = self.response[skip:skip + skipLen]
		if 'true' in halfparse:
			return True
		else:
			return False

	def asciiparser(self, text: str, find: str, skipLen = 8) -> str:
		pass

	# library functions

	def followingcount(self) -> int: return self.intparser('\\"followingCount\\":')

	def followercount(self) -> int: return self.intparser('\\"followerCount\\":')

	def viewcount(self) -> int: return self.intparser('\\"viewCount\\":')

	def lastmonthviews(self) -> int: return self.intparser('\\"lastMonthPublicContentViews\\"')

	def answercount(self) -> int: return self.intparser('\\"numPublicAnswers\\"')

	def questioncount(self) -> int: return self.intparser('\\"numProfileQuestions\\":')

	def questionshares(self) -> int: return self.intparser('\\"quoraSharesCount\\":')

	# . . .

	def isblocked(self) -> bool: return self.boolparser('\\"isUserBanned\\":', 6)


p = Public("Vlad Usatii")
print(p.followingcount(), p.followercount(), p.viewcount(), p.answercount(), p.questioncount(), p.isblocked())
