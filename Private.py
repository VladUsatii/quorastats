import requests

class Private(object):
	def __init__(self, username: str, password: str):
		self.payload = {"queryName": "LoginForm_loginDo_Mutation",
						"extensions":{"hash":"84c101336cf918326e85a2bfd01acba0a99e266346c3414a8472bc4e6e8b6415"},
						"variables":{"email":"vladusatii@gmail.com","password":"110975Scream@","captcha":""}}

p = Private('vlad usatii', password)
