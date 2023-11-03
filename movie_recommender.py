#Movie Recommender script
# https://medium.com/analytics-vidhya/web-scraping-with-python-and-object-oriented-programming-14638a231f14

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

print(ExtractMovies)
        
#function to make ratings to two decimal places
def first2(s):
    return s[:4]


headers = {'User-Agent': 'Mozilla/5.0'}
session = requests.Session()
response = session.get('https://www.imdb.com/chart/top/', headers={'User-Agent': 'Mozilla/5.0'})
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')

##TODO: The below code seems to be outdated/broken. I'm going to rewrite it so that it actually works.


movies = soup.select('h3')
#Needs major parsing
#TODO: Tame this text via a function

links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
years = soup.select('span.secondaryInfo')
#Temoporary array to store class instances
_temp_ = []

for index in range(0, len(movies)):
     movie_string = movies[index].get_text()
     movie = (' '.join(movie_string.split()).replace('.', ''))
     movie_title = movie[len(str(index))+1:-7]
     year = years[index].get_text()
     position = index+1
     movie_instances = ExtractMovies(
         movie_title, year, crew[index], first2(ratings[index]))
     print(movie_instances)
     _temp_.append(movie_instances)

random.shuffle(_temp_)
i=1
for obj in _temp_:
    print(i, "|", obj.title, '\n', obj.year,'\n', obj.star, '\n', obj.ratings, '\n')
    i=i+1
    if(i==11):
        break

#this is an example, a test