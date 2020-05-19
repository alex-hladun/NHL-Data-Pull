import pickle
import pandas as pd
from ArrayFunction import gamearray
from CleanTimeFunction import cleantimeanddate
from NHLOddsMergerFunction import NHLoddsmerger


def importmergeddataset(url, DSTdate, Excelfilepath, importfilename):
    df1 = gamearray(url)
    df1 = cleantimeanddate(df1, DSTdate)
    df1 = NHLoddsmerger(df1, Excelfilepath)
    outfile = open(importfilename, 'wb')
    pickle.dump(df1, outfile)
    outfile.close()


importmergeddataset("https://statsapi.web.nhl.com/api/v1/schedule?startDate=2007-09-29&endDate=2008-06-04",
                    "2008-03-09", "/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/nhlodds2007-08.xlsx",
                    "2007-08dataset")
