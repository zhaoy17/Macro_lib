'''
Provides functionality which allows easy access to the macroeconomic data through 
the Federal Reserve Bank of St. Louis API
'''
from macro_lib import _assist
from urllib import request
from urllib import error
from urllib import parse
import json
import numpy as np
import pandas as pd

class DataQuery:
    '''
    __API_KEY__: the unique api_key for our application; this is needed for pulling GET Request
    __HTTP__:    Path to the source on Web Server
    __current__: the most recent requested list of categories 
    __history__: a stack that allows user to go back to their previously request list of categories
    '''
    def __init__(self):
        self.__API_KEY__ = "4f96326c4128a0f9e5a951bd674b6b61"
        self.__HTTP__ = "https://api.stlouisfed.org/"
        self.__CATEGORIES__ = {
            'Money, Banking, & Finance' : 32991, 
            'Population, Employment, & Labor Markets' : 10,
            'National Accounts' : 32992,
            'Production & Business Activity' : 1,
            'Prices' : 32455,
            'International Data' : 32263,
            'US Regional Data' : 3008 ,
            'Academic Data' : 33060
        }
        self.__current__ = self.__CATEGORIES__
        self.__history__ = list()  

    '''
    this method should return the url for GET request given the parameters
    to server and source directory

    Example:
    INPUT: _parse_request(self, {category_id: 125}, category) should return an url address: 
    RETURN: https://api.stlouisfed.org/fred/category?category_id=125&api_key=abcdefghijklmnopqrstuvwxyz123456&file_type=json
    Possible directory parameter includes:
        -----------
        Categories 
        -----------
        * fred/category - Get a category.
        * fred/category/children - Get the child categories for a specified parent category.
        * fred/category/related - Get the related categories for a category.
        * fred/category/series - Get the series in a category.
        * fred/category/tags - Get the tags for a category.
        * fred/category/related_tags - Get the related tags for a category.
        -----------
        Releases 
        -----------
        * fred/releases - Get all releases of economic data.
        * fred/releases/dates - Get release dates for all releases of economic data.
        * fred/release - Get a release of economic data.
        * fred/release/dates - Get release dates for a release of economic data.
        * fred/release/series - Get the series on a release of economic data.
        * fred/release/sources - Get the sources for a release of economic data.
        * fred/release/tags - Get the tags for a release.
        * fred/release/related_tags - Get the related tags for a release.
        * fred/release/tables - Get the release tables for a given release.
        --------
        Series 
        --------
        * fred/series - Get an economic data series.
        * fred/series/categories - Get the categories for an economic data series.
        * fred/series/observations - Get the observations or data values for an economic data series.
        * fred/series/release - Get the release for an economic data series.
        * fred/series/search - Get economic data series that match keywords.
        * fred/series/search/tags - Get the tags for a series search.
        * fred/series/search/related_tags - Get the related tags for a series search.
        * fred/series/tags - Get the tags for an economic data series.
        * fred/series/updates - Get economic data series sorted by when observations were updated on the FRED® server.
        * fred/series/vintagedates - Get the dates in history when a series' data values were revised or new data values were released.
        --------
        Sources 
        --------
        * fred/sources - Get all sources of economic data.
        * fred/source - Get a source of economic data.
        * fred/source/releases - Get the releases for a source.
        --------
        Tags 
        --------
        * fred/tags - Get all tags, search for tags, or get tags by name.
        * fred/related_tags - Get the related tags for one or more tags.
        * fred/tags/series - Get the series matching tags.

    More Info At: https://research.stlouisfed.org/docs/api/fred/category.html
    '''
    def _parse_request(self, params, directory):
        params['api_key'] = self.__API_KEY__
        params['file_type'] = 'json'
        params = parse.urlencode(params)
        url = f"{self.__HTTP__}{directory}?{params}"
        return url

    '''
    return a list of category user can navigate to
    '''
    def get(self):
        return sorted(self.__current__)

    '''
    Navigate to one of the categories of data
  
    Parameters:
        * selection:  the index of the category the user choose to navigate to
        * assist:     optional parameter, if true get the argument through prompts
   
    Returns:
        * the selected category's child

    Example:
        go_to('US Regional Data') should return:
        [States, BEA Regions, BLS Regions, Federal Reserve Districts, Freddie Mac Regions]
        in sorted order
    '''
    def go_to(self, selection = None, assist = False):
        if assist:
            prompt = "Please choose from one of the following categories to navigate into:\n--------------------------------------------------------------------\n"
            categories = list(self.get())
            for category in categories:
                prompt += (category + "\n")
            selection = _assist._ask_for_one_(prompt, type(""))
            if (selection == None):
                return
        elif selection == None:
            raise ValueError("selection must be either a string or an index")
        if type(selection) == type(5):
            if selection - 1 >= len(self.get()):
                raise IndexError("Attempt to go to a non-exisiting category")
            selection = self.get()[selection - 1]
        elif type(selection) != type(""):
            raise ValueError("selection must be either a string or an index")
        if selection not in self.__current__.keys():
            raise ValueError("Attempt to go to a non-exisiting category")
        url = self._parse_request({'category id' : self.__current__[selection]}, "fred/category/children")        
        try:
            data = request.urlopen(url).read()
            data = json.loads(data)['categories']
        except:
            raise ConnectionError("HTTP Request was not successful")
        self.__history__.append(self.__current__)
        self.__current__ = dict(zip([e['name'] for e in data], [d['id'] for d in data]))
        return self.get()

    '''
    Navigate back and return the category's parent
    '''
    def go_back(self):
        if len(self.__history__) != 0:
            self.__current__ = self.__history__.pop()
        return self.get()








    