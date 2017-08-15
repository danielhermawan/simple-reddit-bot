import praw
import os
import re
import pdb
import logging

from praw.exceptions import APIException


def log_request():
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger = logging.getLogger('prawcore')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

def main():
    log_request()
    reddit = praw.Reddit('bot1')
    if not os.path.isfile('posts_replied_to.txt'):
        posts_replied_to = []
    else:
        with open('posts_replied_to.txt', 'r') as f:
            posts_replied_to = f.read().split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))
    subreddit = reddit.subreddit('pythonforengineers')
    for submission in subreddit.hot(limit=5):
        if submission.id not in posts_replied_to:
            if re.search("i love python", submission.title, re.IGNORECASE):
                try:
                    submission.reply("Botty bot says: Me too!!")
                    posts_replied_to.append(submission.id)
                    with open("posts_replied_to.txt", "w") as f:
                        for post_id in posts_replied_to:
                            f.write(post_id + "\n")
                except(APIException):
                    print('Exceed request limit!')


if __name__ == '__main__':
    main()