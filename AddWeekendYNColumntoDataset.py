from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle
infile = open('2007-20dataset', 'rb')
df1 = pickle.load(infile)
infile.close()
dfx = pd.read_excel(
    '/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/WeekendDates.xlsx')
n = 0
weekenddateYN = []
for year in range(1):
    for date in range(5):
        weekenddateYNlist = []
        for index, row in df1[year][date].iterrows():
            for index2, row2 in dfx.iterrows():
                n = n + 1
                print(n)
                if row['year'] == row2['Year'] and row['gamedate'] == row2['Date']:
                    weekenddateYN = 'Y'
                    break
                else:
                    weekenddateYN = 'N'
            weekenddateYNlist.append(weekenddateYN)
        print(weekenddateYNlist)
        print(df1[0][0])
        df1[year][date].insert(2, "wknddate", weekenddateYNlist, True)
        print(df1[year][date])
