'''
Provides functionality which allows easy access to the macroeconomic data through 
the Federal Reserve Bank of St. Louis API
'''
from urllib import request
from urllib import error
from urllib import parse
import numpy as np
import pandas as pd

class DataQuery:
    '''
    __API_KEY__: the unique api_key for our application; this is needed for pulling GET Request
    __HTTP__:    Path to the source on Web Server
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
            'Regional Data' : 3008 ,
            'Academic Data' : 33060
        }

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
        params = parse.urlencode(params)
        url = f"{self.__HTTP__}{directory}?{params}"
        return url


    