'''
Created on 18th August 2017
@author: Charlotte Alexandra Wilson

Last revision: 18th August 2017
See gihub for details:
https://github.com/CAWilson94/redditcritiquethreadbot

'''

import praw
import re

reddit = praw.Reddit('botwriting')

subreddit = reddit.subreddit('writing')

for submission in subreddit.hot(limit=5):
	if re.search("Weekly Critique Thread", submission.title, re.IGNORECASE):
		print("Title: ", submission.title)
		print("Text: ", submission.selftext)
		print("Score: ", submission.score)
		print("---------------------------------\n")