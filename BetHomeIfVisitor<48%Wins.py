from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle

filename = '2007-20dataset'
infile = open(filename, 'rb')
df1 = pickle.load(infile)
infile.close()
print(type(df1[12][84].loc[1, 'year']))
df2 = pd.DataFrame()
weekenddate = ""
for year in range(len(df1)):
    for date in range(len(df1[year])):
        for index, row in df1[year][date].iterrows():
            if (row['homeLs'] + row['homeOTLs']) != 0:
                hometeamWpercent = row['homeWs'] / \
                    (row['homeWs'] + row['homeLs'] + row['homeOTLs'])
            else:
                hometeamptpercent = 0
            if (row['awayLs'] + row['awayOTLs']) != 0:
                awayteamWpercent = row['awayWs'] / \
                    (row['awayWs'] + row['awayLs'] + row['awayOTLs'])
            else:
                awayteamWpercent = 0
            hometeamGP = row['homeWs'] + row['homeLs'] + row['homeOTLs']
            awayteamGP = row['awayWs'] + row['awayLs'] + row['awayOTLs']
            if (awayteamWpercent <= 0.48 and hometeamGP >= 15) and (row['hour'] <= 16 or weekenddate == row["gamedate"]):
                weekenddate = row["gamedate"]
                df2 = df2.append(df1[year][date].iloc[index, :])
moneylineWL = []
profit = []
for index, row in df2.iterrows():
    if row['homegoals'] > row['awaygoals']:
        moneylineWL.append('W')
        if row['homecloseodds'] > 0:
            profit.append(row['homecloseodds']/100)
        else:
            profit.append(-100/row['homecloseodds'])
    else:
        moneylineWL.append('L')
        profit.append(-1)
df2['moneylineWL'] = moneylineWL
df2['profit'] = profit
df2 = df2[['year', 'gamedate', 'gametype', 'hour', 'mins', 'hometeam', 'homegoals', 'homeWs', 'homeLs',
           'homeOTLs', 'awayteam', 'awaygoals', 'awayWs', 'awayLs', 'awayOTLs',
           'homeopenodds', 'homecloseodds', 'awayopenodds', 'awaycloseodds', 'homespreadgoals',
           'awayspreadgoals', 'homespreadodds', 'awayspreadodds', 'openoverunder',
           'openoverodds', 'openunderodds', 'closeoverunder', 'closeoverodds', 'closeunderodds',
           'moneylineWL', 'profit']]

print(df2)
sum = df2['profit'].sum()
print(sum)
path = r'/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/BetHomeIfAfternoonVisitor<48%Wins.xlsx'
book = load_workbook(path)

writer = pd.ExcelWriter(path, engine='openpyxl')
writer.book = book
df2.to_excel(writer, '07-20 Results')
writer.save()
writer.close()
