#!/usr/bin/env python3
from Public import Public

p = Public('vlad usatii')
p2 = Public('fdhjsafdu8saf09hds8af9hdsa')

# prints counts
print(p.followercount(), p.followingcount())

# prints real status of user page
print(p.status, p2.status)
