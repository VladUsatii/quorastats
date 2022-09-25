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

	def stringparser(self, newresp: str, text: str, skipLen = 8) -> str:
		skip = newresp.find(text) + len(text)
		stringparse = newresp[skip:skip + skipLen]
		return stringparse

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

	def publicquestioncount(self) -> int:
		newresp = get(self.url).text
		return self.intparser(newresp, '\\"numPublicQuestions\\":')

	def privatequestioncount(self) -> int:
		return int(self.questioncount()) - int(self.publicquestioncount())

	def questionshares(self) -> int:
		newresp = get(self.url).text # must include new func call every time
		return self.intparser(newresp, '\\"quoraSharesCount\\":')

	def postcount(self) -> int:
		newresp = get(self.url).text # new every time
		return self.intparser(newresp, '\\"postsCount\\":')

	def followedtopics(self) -> int:
		newresp = get(self.url).text
		return self.intparser(newresp, '\\"numFollowedTopics\\":')

	def followedtribes(self) -> int: # not quite sure what a tribe is
		newresp = get(self.url).text
		return self.intparser(newresp, '\\"numFollowedTribes\\":')

	## more complex calls

	def contentlanguage(self) -> str:
		newresp = get(self.url).text # call
		skip = newresp.find('\\"contentLanguageCode\\":') + len('\\"contentLanguageCode\\":')
		parse = newresp[skip:skip + 6]
		if 'en' in parse:
			return 'English'
		elif 'ru' in parse:
			return 'Russian' # more coming, but have to learn the code names

	def downloadprofilepic(self):
		newresp = get(self.url).text # call
		skip = newresp.find('\\"profileImageUrl\\":') + len('\\"profileImageUrl\\":')
		parse = newresp[skip + 2:skip + 250]
		if '\\",\\"network\\":{\\"nid\\"' in parse:
			final = parse.split('\\",\\"network\\":{\\"nid\\"')[0]
			image = get(final).content
			with open(f'{self.username}_profileimage.jpg', 'wb') as handler:
				try:
					handler.write(image)
					print(f"Downloaded image. Link to picture is: {final}.\nSaved file is {self.username}_profileimage.jpg.")
				except IOError:
					print("Cound not save image.")

	def userdescription(self) -> str:
		newresp = get(self.url).text # must include per call
		skip = newresp.find("meta name=\'description\' content=\'") + len("meta name=\'description\' content=\'")
		parse = newresp[skip:10000]
		if "rel=\'canonical\' href" in parse:
			final = parse.split("link rel=\'canonical\' href")[0]
		return final[0:-5]

	def questions(self) -> str: # returns json
		user = self.username
		pass

	def totalanswerstousersquestions(self) -> int:
		url = self.url + '/questions/'
		response = get(url).text

		pass

	def joindate(self) -> str:
		newresp = get(self.url).text # call
		skip = newresp.find('\\"creationTime\\":') + len('\\"creationTime\\":')
		mid = int(self.intparser(newresp, '\\"creationTime\\":', 20))
		final = mid//365//24//60//60//60//60//60//60
		return final

	# . . .

	def isblocked(self) -> bool:
		newresp = get(self.url).text # clean func call
		return self.boolparser(newresp, '\\"isUserBanned\\":', 6)

	def isFlagged(self, flags = None) -> bool: # FLAGS: 'BOTH' -> See both flag statuses, FLAGS: None -> See both flag statuses
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

	def canSeeDeletedContent(self) -> bool:
		newresp = get(self.url).text # clean func call
		return self.boolparser(newresp, '\\"canSeeDeletedContent\\":', 6)

	def canReviewAnswers(self) -> bool:
		newresp = get(self.url).text # clean func call
		return self.boolparser(newresp, '\\"viewerCanReviewAnswers\\":', 6)

