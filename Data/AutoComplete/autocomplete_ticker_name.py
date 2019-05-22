import fix_yahoo_finance as TickerData

import sys
import requests
import json

# print("Beginning script for autocomplete")

stocks = requests.get("http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(sys.argv[1])).json()['ResultSet']['Result'] # getting data and sorting through dictoinary

data = [] #the final data values to put in json

for stock in stocks:
    data.append(TickerData.Ticker(stock["symbol"]).info) # adding quote of the current stock

with open('/Users/ozanmirza/desktop/Stock-Predictor-Python/Data/AutoComplete/autocomplete.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, sort_keys=True) # saving the json and formatting it

# print("Successfully autocompleted data for {}".format(sys.argv[1]))
