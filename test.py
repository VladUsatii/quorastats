#!/usr/bin/env python3
import time
from Public import Public

p = Public("vlad usatii") # real account
p2 = Public("fdsfdsafdsafdsafdsafd") # fake account

# prints real status of user page
# print(p.status, p2.status)

# most of public resources
# print(f'{p.followingcount()}  {p.followercount()}  {p.viewcount()}  {p.answercount()}  {p.questioncount()}  {p.isblocked()}\n\n{p.questions()}')

# print(f'\n\n{p.isFlagged("BOTH")}')
# print(f'{p.canSeeDeletedContent()}	{p.canReviewAnswers()}')

# downloading profile image
# p.downloadprofilepic()

#print(f'{p.userdescription()}')

#print(f'{p.joindate()}')



print(f'{p.questioncount()} {p.publicquestioncount()}')
print(f'{p.privatequestioncount()}')
