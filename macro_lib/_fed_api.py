'''
A simple interface which enables easy access to the macroeconomic data through 
the Federal Reserve Bank of St. Louis API
'''
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
    __current__: the most recent requested data 
    __history__: a stack that allows user to go back to their previously request data
    '''
    def __init__(self):
        self.__API_KEY__ = "4f96326c4128a0f9e5a951bd674b6b61"
        self.__HTTP__ = "https://api.stlouisfed.org/"
        self.__current__ = None
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
    get the last requested data
    '''
    def _get(self):
        if (self.__current__ == 'None'):
            raise ValueError("You have not requested any data")
        return self.__current__

    '''
    Navigate back and return the category's parent
    '''
    def _go_back(self):
        if len(self.__history__) != 0:
            self.__current__ = self.__history__.pop()
        return self.get()

    '''
    Get the observation or data values for an economic data series and convert them
    into a pandas dataframe
  
    Parameters:
        * id:  the series_id, which can be found in the FED's site
   
    Returns:
        * the entire obervation
    '''
    def _fetch_all(self, id):
        if type(id) != type(""):
            raise ValueError("id must be a string")
        url = self._parse_request({'series_id' : id}, "fred/series/observations")        
        try:
            data = request.urlopen(url).read()
        except:
            raise ConnectionError("HTTP Request was not successful")
        data = json.loads(data)['observations']
        if data == {}:
            raise ValueError("id is invalid")
        if (self.__current__ != None):
            self.__history__.append(self.__current__)
        df = pd.DataFrame(dict(zip([d['date'] for d in data], [v['value'] for v in data])))
        self.__history__.append(self.__current__)
        self.__current__ = df
        return __current__

    '''
    Get the observation or data values for an economic data series from a given
    starting date to a given ending date and convert them into a pandas dataframe
  
    Parameters:
        * id: the series_id, which can be found in the FED's site
        * obs_start: the start date of the time series in the format YYYY-MM-DD
        * obs_end: the end date of the time series in the format YYYY-MM-DD
   
    Returns:
        * observations from a certain start date to an end date
    '''
    def _fetch_by_date(self, id, obs_start, obs_end):
        if (type(id) != type ("") or type(obs_start) != type("") or type(obs_end) != type("")):
            raise ValueError("id must be a string")
        url = self._parse_request({'series_id' : id, 'observation_start': obs_start, 'observation_end' : obs_end})
        try:
            data = request.urlopen(url).read()
        except:
            raise ConnectionError("HTTP Request was not successful")
        if data == {}:
            raise ValueError("the query returns nothing")
        data = json.loads(data)['observations']
        if (self.__current__ != None):
            self.__history__.append(self.__current__)
        if (len(data['date'] == 1)):
            df = data['value']
        else:
            df = pd.DataFrame(dict(zip([d['date'] for d in data], [v['value'] for v in data])))
        self.__current__ = df
        return __current__

