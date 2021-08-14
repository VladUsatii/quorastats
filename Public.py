# Public.py --> Vlad Usatii @ youshould.readproduct.com
import sys, os, time, re
from requests import get
from bs4 import BeautifulSoup as bs

class Public(object):
	def __init__(self, username: str):
		self.username = username.replace(' ', '-')

		# source code
		self.url = f'https://www.quora.com/{self.username}'
		self.response = get(self.url).text

		# returns 200 if page found : else, returns real status code
		self.status = int(re.sub("[^0-9]", "", str(get(self.url))))

	# Returns int (low latency)
	def followingcount(self) -> int:
		skip = int(self.response.find('\\"followingCount\\":')) + len('\\"followingCount\\":')
		following = int(re.sub("[^0-9]", "", str(self.response[skip:skip + 8])))
		return following

	def followercount(self) -> int:
		skip = int(self.response.find('\\"followerCount\\":')) + len('\\"followerCount\\":')
		followers = int(re.sub("[^0-9]", "", str(self.response[skip:skip + 8])))
		return followers
