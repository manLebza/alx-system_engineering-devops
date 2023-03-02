#!/usr/bin/python3
"""
Function that queries the reddit API and prints
the top ten posts of a subreddit.
"""
import requests
import sys


def add_title(hot_list, hot_posts):
    """ Queries to the reddit API """
    u_agent = 'Mozilla/5.0'
    headers = {'User-Agent': u_agent}
    params = {'after': after}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(hot_list, hot_posts)
    after = dic['data']['after']
    if not after:
        return hot_list
    return recurse(subreddit, hot_list=hot_list, after=after)
