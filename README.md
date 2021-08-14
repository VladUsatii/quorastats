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
import quorastats as qs

# grabbing follower-count is 
