#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def count_subscribers(subreddit_name):
    """Retrieve the number of subscribers for a subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit_name)
    response = requests.get(url, headers={'User-Agent': 'os:0x16.api.advanced:v1.0'})
    if response.status_code != 200:
        return 0
    subreddit_data = response.json()['data']
    return subreddit_data['subscribers']

