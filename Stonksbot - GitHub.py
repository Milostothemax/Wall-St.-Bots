import requests
import random
from bs4 import BeautifulSoup
import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler(API, SECRET API)
auth.set_access_token(ACCESS TOKEN, SECRET TOKEN)

#Scrape BBC for Headline text
url = 'https://www.bbc.co.uk/news'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')

tags = soup.find_all(class_='gs-c-promo-heading__title')
#print(headlines)
headlines = list()

for i in tags:
    if i.string is not None:
        if ':' not in i.string:
            if '?' not in i.string:
                headlines.append(i.string)

#Phrases for rising and falling
phrases = [
    'rises',
    'threatens to spiral out of control',
    'decreases',
    'squeezing',
    #Add more phrases as required
]
# Create API object
api = tweepy.API(auth)

api.update_status(f'Stock market {random.choice(phrases)} as {random.choice(headlines)} #wstbot #stonks')


