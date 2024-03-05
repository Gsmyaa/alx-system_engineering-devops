#!/usr/bin/python3
'''
 Prints the titles of top-ten for a given subreddit.
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        returns the top 10 posts for a given subreddit
    '''
    user = {'User-Agent': 'geda'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])
