#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Retrieve the number of subscribers for a subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers={'User-Agent':
                                          'os:api.advanced:v1.0'})
    if response.status_code != 200:
        return 0
    data = response.json()['data']
    return data['subscribers']
