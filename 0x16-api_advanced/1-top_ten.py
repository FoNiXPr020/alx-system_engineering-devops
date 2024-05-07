#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Send a GET request to the subreddit's hot posts page
    response = requests.get(url, allow_redirects=False)

    # Check if the response status code indicates a not-found error (404)
    if response.status_code == 404:
        print("None")
        return

    # Parse the JSON response and extract the 'data' section
    results = response.json().get("data")

    # Print the titles of the first 10 hottest posts
    try:
        [print(c.get("data").get("title"))
         for c in results.get("children")[:10]]
    except TypeError:
        pass
