from ImportMergedDatasetFunction import importmergeddataset
import pickle
import pandas as pd
from ArrayFunction import gamearray
from CleanTimeFunction import cleantimeanddate
from NHLOddsMergerFunction import NHLoddsmerger

# importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2007-09-29&endDate=2008-06-04",
#                    "309", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2007-08.xlsx",
#                    "2007-08dataset")
importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2008-10-04&endDate=2009-06-12",
                    "308", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2008-09.xlsx",
                    "2008-09dataset")
# could copy and paste this function for every schedule range,associated Excel file, DST date for that year
# and changing output file name, or just use the pickle files that I've already done this with
# (eg. 2007-08dataset, 2008-09dataset, 2007-20dataset etc)
