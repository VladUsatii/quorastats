#!/usr/bin/env python3
import time
from Public import Public

p = Public("real account") # real account
p2 = Public("fdsfdsafdsafdsafdsafd") # fake account

# prints real status of user page
print(p.status, p2.status)

print(f'{p.followingcount()}  {p.followercount()}  {p.viewcount()}  {p.answercount()}  {p.questioncount()}  {p.isblocked()}\n\n{p.questions()}')

print(f'\n\n{p.userdescription()}')
