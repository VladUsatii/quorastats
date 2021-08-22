# Public Documentation

Assuming you specified profile via init, the following applies:

```bash
p = Profile('account name')
```

## User Status

### Names

The following return strings of username, list of family names, first name only, and last few names based on input (lastname function), respectively.

```python3
p.username
p.names # -> list
p.firstname
p.lastname # returns last name, no last name, or multiple last names
# ---
p.middlename # only if applicable
```

### Requests

```python3
p.url # returns string of user's page.
p.response # returns quora page html (react)
p.status # reutrns state of quora page (200: OK, 404: PNF)
p.scrape_headers # returns scrape headers if using selenium
```

## Profile Counts

### Followers

```python3
p.followercount()
```

Returns integer of followers.

### Following

```python3
p.followingcount()
```

Returns integer of following.

### Counts

The following return integers of view counts (of user's posts), answer counts (of user), question count (of user), and question shares respectively:

```python3
p.viewcount()
p.answercount()
p.questioncount()
p.questionshares()
```

### Download

The following downloads account profile image:

```python3
p.downloadprofilepic()
# Saved in relative path as {self.username}_profileimage.jpg.
```

### Content

The following function returns a string of user description:

```python3
p.userdescription()
```

### Flag/Ban Bool

```
# Bans
p.isblocked() # returns if user is banned

# Flags
p.isFlagged(flags=None) # flags = 'BOTH' returns both statuses
p.canSeeDeletedContent() # returns if user can see deleted content
p.canReviewAnswers() # returns if user can review answers
```

## More Soon

Submit pull request to add more.
