import praw

reddit = praw.Reddit('bot1')

for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
