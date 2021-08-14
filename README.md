# quorastats

A Pythonic Quora API, capable of printing out the following user stats without login:

[Public Documentation 🔓](https://www.github.com/VladUsatii/quorastats/blob/main/PUBLICDOCS.md)

If content is private (i.e., hidden via account auth), you can use the following documentation to view these stats:

[Private Documentation 🔒](https://www.github.com/VladUsatii/quorastats/blob/main/PRIVATEDOCS.md)

## Getting Started

To download the module:

#### Pre-release
```bash
git clone https://www.github.com/VladUsatii/quorastats/
cd quorastats
pip -r install requirements.txt
# make your files relative to this directory
```

#### Post-release
```bash
python -m pip3 install quorastats
```

## A Basic Program

This program allows users to view a live counter of their followers, updated every _n_ seconds. **Warning: Update should be kept high if possible, due to influx of users to Quora's network. They may also ban IP if too low (please use best judgement).**

```python3
from Public import Public
import time

p = Public('vlad usatii')
p2 = Public('fdhjsafdu8saf09hds8af9hdsa')

# prints counts of a real account
while True:
	print(p.followercount(), p.followingcount())
	time.sleep(100)

# prints status of user page 1 and 2 (not a real account)
print(f'Account 1: {p.status}', f'Account 2: {p2.status}')
```

## Contributions

Submit a pull request to get a feature added.
