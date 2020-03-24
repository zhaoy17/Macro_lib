'''
This module provides functionality for easy access of macroeconomic data from 
the Federal Reserve Bank of St. Louis API
'''
from urllib import request
from urllib import error
from urllib import paese

class DataQuery:
    '''
    __api_key__: the unique api_key for our application; this is needed for pulling GET Request
    __HTTP__: Path to the source on Web Server
    '''
    def __init__(self):
        self.__api_key__ = "4f96326c4128a0f9e5a951bd674b6b61"
        self.__HTTP__ = "https://api.stlouisfed.org/fred/"

    '''
    this method should return the url for GET request given the parameters
    to server and source directory

    Example:
    INPUT: _parse_request(self, {category_id: 125}, category) should return an url address: 
    RETURN: https://api.stlouisfed.org/fred/category?category_id=125&api_key=abcdefghijklmnopqrstuvwxyz123456&file_type=json
    '''
    def _parse_request(self, dict, directory):
        pass

    