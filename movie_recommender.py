#Movie Recommender script
# https://medium.com/analytics-vidhya/web-scraping-with-python-and-object-oriented-programming-14638a231f14
# This program looks like it needs to be fixed. No longer seems to work.

#STEP 1: we are importing the libraries we need. Beautiful Soup is a python webscraping library.
# (Webscraping is basically using a program to copy the html of a webpage and then taking what you want
# from it)
#Requests is a library that allows us to request an HTML page
#BeautifulSOup is a library that allows us to format an html page once we have requested it
#(Formatting meaning we can clean up the 'raw text' from the HTML response)
#Re is a regular expressions library that we may not actually need...tbd
#random is a library that allows us to use a random method
from bs4 import BeautifulSoup
import pprint
import requests
import re
import random

"""
#WE WILL COME BACK TO THIS ONCE WE HAVE PARSED THE WEB PAGE
#STEP 2: make Python class for declaring movie attributes. 
class ExtractMovies(object):      
    def __init__(self, title, year,  star, ratings ):
        self.position = position
        self.title = title
        self.year = year
        self.star = star
        self.ratings = ratings

print(ExtractMovies)
"""
        
#function to make ratings to two decimal places
#Not sure if we will actually need this
def first2(s):
    return s[:4]

#STEP 3: Get the web page in its raw, untamed text format
#getting the web page specified below, passing it the mozilla user agent so it doesn't block us from
# accessing the page, and then storing the page in a 'response' variable

# If you wanna see what this looks like, open the python interpretor and run this:
"""
session = requests.Session()
response = session.get('https://www.imdb.com/chart/top/', headers={'User-Agent': 'Mozilla/5.0'})
print(response.text)
"""

##to see what it looks like after you parse the html with Beautiful Soup, run this:
"""
soup = BeautifulSoup(response.text, 'html.parser')
print(soup)
"""

#Grabbing web page, parsing it with BS, and storing it in soup variable
session = requests.Session()
response = session.get('https://www.imdb.com/chart/top/', headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(response.text, 'html.parser')

#I inspected the html and narrowed it down to the classes that contain the text we are after
raw_titles = soup.findAll(class_="ipc-title__text")
raw_details = soup.findAll(class_="sc-c7e5f54-8 hgjcbi cli-title-metadata-item")
raw_stars = soup.findAll(class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")

#function that parses text
def get_text(raw):
    text = []
    for i in raw:
        text.append(i.text)
     # printing here for testing purposes to validate it works   
    print(text)
    return text

#running the raw titles text through the function to trim it down
titles = get_text(raw_titles)
#narrowing the titles list down to the 250 movies we are after (needed to get rid of some extra text)
titles = titles[2:252]


#extract years from the details text that contains year, rating, runtime
# then we are going to use a regular expression match to find all the text that resembles a year
years = []
for year in get_text(raw_details):
    if re.match("^[12][0-9]{3}$", year):
        years.append(year)



# ------------------------------------------------------------------------------------
# EVERYTHING BELOW HERE DOESN"T WORK

#TODO - problem. This would work except for the fact that 1 damn movie is missing its mpaa rating and its throwing
# everything else off.
#ratings list
raw_ratings = get_text(raw_details)
options = ['G', 'PG', 'PG-13', 'R', 'TV-MA', 'NR','UR', 'M', 'TV-G', 'TV-PG', 'TV-14', 'NC-17', 'X', 'GP', 'Not Rated', '18+', 'Unrated', 'Passed', 'Approved']
ratings = []
for rating in raw_ratings:
    if rating in options:
        ratings.append(rating)

#make time list
times = []
for i in raw_ratings:
    if i not in options and i not in years:
        times.append(i)
"""raw_runtimes = get_text(raw_details)
runtimes = []
for runtime in raw_runtimes:
    if re.match("m$", runtime):
        runtimes.append(runtime)
"""
[]


#print(soup.findAll(class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"))


#TODO - parse links
links = soup.findAll(class_="ipc-title-link-wrapper")



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