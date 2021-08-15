#!/usr/bin/env python3
import time
from Public import Public

p = Public("Vlad Usatii") # real account
p2 = Public("fdsfdsafdsafdsafdsafd") # fake account

# prints real status of user page
print(p.status, p2.status)

while True:
	print(p.followingcount(), p.followercount(), p.viewcount(), p.answercount(), p.questioncount(), p.isblocked())
	time.sleep(10)
