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
import pprint
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


raw_titles = soup.findAll(class_="ipc-title__text")
raw_details = soup.findAll(class_="sc-c7e5f54-8 hgjcbi cli-title-metadata-item")
#raw_ratings = soup.findAll(class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")
#THIS IS WORKING. Just need to make it not so ugly. Less lines, same function. 

#Note about below: using quotation marks 3 times on either side of a block of code makes it dormant
# I don't think I'll need below function but I'm keeping it around for reference at the moment
"""
def get_titles(soup): 
    raw_titles = soup.findAll(class_="ipc-title__text")
    raw_titles = raw_titles[2:252]
    titles = []
    for title in raw_titles:
        titles.append(title.text)
     # printing here to validate it works   
    print(titles)
    return titles
    """

#DRY - this function is the same as above but im hoping it will replace it by being able to be used with
# more than just the titles. I want this to be a text cleaning function for ratings, titles, years, etc
#works for title, years, ratings, time. Not for link. Might need to build separate function for links
def get_text(raw):
    text = []
    for i in raw:
        text.append(i.text)
     # printing here to validate it works   
    print(text)
    return text

#make titles list
#Works
titles = get_text(raw_titles)
titles = titles[2:252]

#make years list
#works
raw_years = get_text(raw_details)
years = []
for year in raw_years:
    if re.match("^[12][0-9]{3}$", year):
        years.append(year)

    
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