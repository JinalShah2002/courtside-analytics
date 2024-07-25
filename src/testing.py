"""

@author: Jinal Shah

This file is meant for testing
and messing around with functions.

"""
import requests
from bs4 import BeautifulSoup


# Statmuse Function
def get_statmuse_response(query):
    query_list = query.split(' ')
    url = f"https://www.statmuse.com/nba/ask/{'-'.join(query_list)}"
    return requests.get(url).content

# Test the function
resp = get_statmuse_response('timberwolves points per game without anthony edwards')
soup = BeautifulSoup(resp, 'html.parser')

# with open('testing.txt', 'w') as f:
#     f.write(soup.prettify())

for content in soup.find_all('meta'):
    if content.get('name') == 'description':
        print(content.get('content'))