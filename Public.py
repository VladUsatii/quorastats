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

	def totalanswerstoquestions(self) -> int:
		url = self.url + '/questions/'
		response = get(url).text

		pass

	# . . .

	def isblocked(self) -> bool:
		newresp = get(self.url).text # must include new func call every time
		return self.boolparser(newresp, '\\"isUserBanned\\":', 6)

