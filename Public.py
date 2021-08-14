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

		# returns 200 if page found : else, returns real status code
		self.status = int(re.sub("[^0-9]", "", str(get(self.url))))

	# core functions

	def sub(self, response: str) -> int:
		return int(re.sub("[^0-9]", "", response))

	# library functions

	# Returns int (low latency)
	def followingcount(self) -> int:
		text = '\\"followingCount\\":'
		skip = self.response.find(text) + len(text)
		following = self.sub(self.response[skip:skip + 8])
		return following

	def followercount(self) -> int:
		text = '\\"followerCount\\":'
		skip = self.response.find(text) + len(text)
		followers = self.sub(self.response[skip:skip + 8])
		return followers

	def viewcount(self) -> int:
		text = '\\"viewCount\\":'
		skip = self.response.find(text) + len(text)
		viewcount = self.sub(self.response[skip:skip + 8])
		return viewcount

	def answercount(self) -> int:
		pass

	def questioncount(self) -> int:
		pass

p = Public("vlad usatii")
print(p.followingcount(), p.followercount(), p.viewcount())
