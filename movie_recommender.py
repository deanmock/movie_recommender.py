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