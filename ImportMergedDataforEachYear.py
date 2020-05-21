from ImportMergedDatasetFunction import importmergeddataset
import pickle
import pandas as pd
from ArrayFunction import gamearray
from CleanTimeFunction import cleantimeanddate
from NHLOddsMergerFunction import NHLoddsmerger

# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2007-09-29&endDate=2008-06-04",
#                    "309", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2007-08.xlsx",
#                    "2007-08dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2008-10-04&endDate=2009-06-12",
#                    "308", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2008-09.xlsx",
#                    "2008-09dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2009-10-01&endDate=2010-06-09",
#                    "314", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2009-10.xlsx",
#                    "2009-10dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2010-10-07&endDate=2011-06-15",
#                    "313", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2010-11.xlsx",
#                    "2010-11dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2011-10-06&endDate=2012-06-11",
#                    "311", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2011-12.xlsx",
#                    "2011-12dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2013-01-19&endDate=2013-06-24",
#                    "310", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2012-13.xlsx",
#                    "2012-13dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2013-10-01&endDate=2014-06-13",
#                    "309", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2013-14.xlsx",
#                    "2013-14dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2014-10-08&endDate=2015-06-15",
#                    "308", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2014-15.xlsx",
#                    "2014-15dataset")
importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2015-10-07&endDate=2016-06-12",
                    "313", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2015-16.xlsx",
                    "2015-16dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2016-10-12&endDate=2017-06-11",
#                    "312", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2016-17.xlsx",
#                    "2016-17dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2017-10-04&endDate=2018-06-07",
#                    "311", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2017-18.xlsx",
#                    "2017-18dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2018-10-03&endDate=2019-06-12",
#                    "310", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2018-19.xlsx",
#                    "2018-19dataset")
# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2019-10-02&endDate=2020-03-11",
#                    "308", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2019-20.xlsx",
#                    "2019-20dataset")
