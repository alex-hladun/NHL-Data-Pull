from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle
print(15)
print(14)
infile = open('2007-20dataset', 'rb')
df1 = pickle.load(infile)
infile.close()
print(df1)
dfx = pd.read_excel(
    '/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/WeekendDates.xlsx')
print(dfx)
#n = 0
#weekenddateYNlist = []
#weekenddateYN = []
# for year in range(len(df1)):
#    for date in range(len(df1[year])):
#        for index, row in df1[year][date].iterrows():
#            for index2, row2 in dfx.iterrows():
#                n = n + 1
#                print(n)
#                if row['year'] == row2['Year'] and row['gamedate'] == row2['Date']:
#                    weekenddateYN = 'Y'
# break
#                else:
#                    weekenddateYN = 'N'
#            weekenddateYNlist.append(weekenddateYN)
#        df1[year][date]['wknddate'] = weekenddateYNlist
#        df1[year][date] = df1[year][date][['year', 'gamedate', 'wknddate' 'gametype', 'time', 'hour', 'mins', 'hometeam', 'homegoals', 'homeWs', 'homeLs',
#                                           'homeOTLs', 'awayteam', 'awaygoals', 'awayWs', 'awayLs', 'awayOTLs',
#                                           'homeopenodds', 'homecloseodds', 'awayopenodds', 'awaycloseodds', 'homespreadgoals',
#                                           'awayspreadgoals', 'homespreadodds', 'awayspreadodds', 'openoverunder',
#                                           'openoverodds', 'openunderodds', 'closeoverunder', 'closeoverodds', 'closeunderodds'
#                                           ]]
#        print(df1[year][date])
