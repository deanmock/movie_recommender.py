#Movie Recommender script

from bs4 import BeautifulSoup
import requests
import re
import random

#Python class for declaring movie attributes. 
class ExtractMovies(object):      
    def __init__(self, title, year,  star, ratings ):
        self.position = position
        self.title = title
        self.year = year
        self.star = star
        self.ratings = ratings
        
#function to make ratings to two decimal places
def first2(s):
    return s[:4]

url = 'https://www.imdb.com/chart/top/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.select('td.titleColumn')
links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
years = soup.select('span.secondaryInfo')
#Temoporary array to store class instances
_temp_ = []
