# import finsymbols
import pandas
import numpy
import requests
import finsymbols
# import csv

def get_company():
    """
    - Receive the content of finsymbols get_sp500_symbols, which gets them from wikipedia
    https://stackoverflow.com/questions/13769278/are-there-any-free-apis-for-retrieving-the-sp-500s-component-symbols

    Parameters
    ----------

    Returns
    -------
    - s&p 500 symbols and descriptive data

    """
    data = pandas.json_normalize(finsymbols.get_sp500_symbols())
    return(data['symbol'], data)

def get_values(symbols):
    """
    - gets two years of history for symbols
    - parse the json into a pandas dataframe
    
    Parameters
    - "symbols"... a series of s&p500 symbols
    ----------

    Returns
    - "data"... a df of two years of history
    -------
    """
    for i in numpy.arange(0, len(symbols), 1):
        ticker = symbols[i]
        url = "https://mboum-finance.p.rapidapi.com/op/option"
        querystring = {"expiration":"1705622400","symbol":"AAPL"}
        headers = {
	        "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)        
