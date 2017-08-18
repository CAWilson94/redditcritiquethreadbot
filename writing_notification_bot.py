'''
Created on 18th August 2017
@author: Charlotte Alexandra Wilson

Last revision: 18th August 2017
See gihub for details:
https://github.com/CAWilson94/redditcritiquethreadbot

'''

import praw
import re
import constants

reddit = praw.Reddit('botwriting')

subreddit = reddit.subreddit('writing')

already_done = []

for submission in subreddit.new(limit=5):
	if re.search("writing", submission.title, re.IGNORECASE):
		print("Title: ", submission.title)
		print("Text: ", submission.selftext)
		print("Score: ", submission.score)
		print("---------------------------------\n")
		if submission.id not in already_done:
			reddit.redditor(constants.USER_NAME).message('WRITING POST', "NEW WRITING THREAD: GO POST!")
			already_done.append(submission.id)