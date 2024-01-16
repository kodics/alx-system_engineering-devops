#!/usr/bin/python3
"""
Queries the Reddit API and returns the number
of subscribers for a given subreddit.
"""

import requests
import sys

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit,
        or 0 if the subreddit is invalid.
    """
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Define the API endpoint URL
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        # Send an HTTP GET request to the Reddit API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)

        # Parse the JSON response and extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions
        print(f"Error: {e}")
        return 0

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)

