#Movie Recommender script
# https://medium.com/analytics-vidhya/web-scraping-with-python-and-object-oriented-programming-14638a231f14
# This program looks like it needs to be fixed. No longer seems to work.

#STEP 1: we are importing the libraries we need. Beautiful Soup is a python webscraping library.
# (Webscraping is basically using a program to copy the html of a webpage)
#Requests is a library that allows us to request an HTML page
#BeautifulSOup is a library that allows us to format an html page once we have requested it
#(Formatting meaning we can clean up the 'raw text' from the HTML response)
#Re is a regular expressions library that we may not actually need...tbd
#random is a library that allows us to use a random method
from bs4 import BeautifulSoup
import requests
import re
import random

#STEP 2: make Python class for declaring movie attributes. 
class ExtractMovies(object):      
    def __init__(self, title, year,  star, ratings ):
        self.position = position
        self.title = title
        self.year = year
        self.star = star
        self.ratings = ratings

print(ExtractMovies)
        
#function to make ratings to two decimal places
#Not sure if we will actually need this
def first2(s):
    return s[:4]

#STEP 3: Get the web page in its raw, untamed text format


#getting the web page specified below, passing it the mozilla user agent so it doesn't block us from
# accessing the page, and then storing the page in a 'response' variable

# If you wanna see what this looks like, open the python interpretor and run this:
### session = requests.Session()
## response = session.get('https://www.imdb.com/chart/top/', headers={'User-Agent': 'Mozilla/5.0'})
## print(response.text)

##to see what it looks like after you parse the html with Beautiful Soup, run this:
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

session = requests.Session()
response = session.get('https://www.imdb.com/chart/top/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'html.parser')

##The below code seems to be outdated/broken. I'm going to rewrite it so that it actually works. 

##TODO: Parse movies, links, ratings, year from soup variable

movies = soup.findAll(class_="ipc-title__text")
#Needs parsing
#TODO: Tame this text via a function


links = soup.findAll(class_="ipc-title-link-wrapper")
years = soup.findAll(class_="sc-c7e5f54-8 hgjcbi cli-title-metadata-item")
ratings = soup.findAll(class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
#print(soup.findAll(class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"))


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