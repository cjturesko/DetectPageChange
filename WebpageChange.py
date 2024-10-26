import hashlib
import requests
import random
import time

# URL to be checked
url = "https://krebsonsecurity.com/"

# Time between checks in seconds
sleeptime = 60

def get_hash():
    # Random integer to select user agent to avoid detection
    randomint = random.randint(0, 7)

    # User agents
    user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.6; rv:110.0) Gecko/20100101 Firefox/110.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36 Edg/117.0.2045.43',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_6_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:117.0) Gecko/20100101 Firefox/117.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
    ]

    headers = {'User-Agent': user_agents[randomint]}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

    # Calculate hash of the page content
    return hashlib.sha224(response.content).hexdigest()

current_hash = get_hash()  # Get the current hash, which is what the website is now

while True:  # Run indefinitely
    if get_hash() == current_hash:  # If nothing has changed
        print('Not Changed')
    else:  # If something has changed
        print('Changed')
        break
    time.sleep(sleeptime)
