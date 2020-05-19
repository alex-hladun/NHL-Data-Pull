from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle
filename = '2011-12dataset'
infile = open(filename, 'rb')
df1 = pickle.load(infile)
infile.close()
print(df1[2])
df2 = pd.DataFrame()
for i in range(len(df1)):
    for index, row in df1[i].iterrows():
        if (row['homeLs'] + row['homeOTLs']) != 0:
            hometeamWLratio = row['homeWs'] / \
                (row['homeWs'] + row['homeLs'] + row['homeOTLs'])
        else:
            hometeamWLratio = 0
        if (row['awayLs'] + row['awayOTLs']) != 0:
            awayteamWLratio = row['awayWs'] / \
                (row['awayWs'] + row['awayLs'] + row['awayOTLs'])
        else:
            awayteamWLratio = 0
        hometeamGP = row['homeWs'] + row['homeLs'] + row['homeOTLs']
        if hometeamWLratio >= 0.58 and awayteamWLratio >= 0.50 and awayteamWLratio <= 0.55 and hometeamGP >= 45:
            df2 = df2.append(df1[i].iloc[index, :])
moneylineWL = []
profit = []
for index, row in df2.iterrows():
    if row['awaygoals'] > row['homegoals']:
        moneylineWL.append('W')
        if row['awaycloseodds'] > 0:
            profit.append(row['awaycloseodds']/100)
        else:
            profit.append(-100/row['awaycloseodds'])
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
path = r'/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/VisitorUnderDogEveningHome580W%.xlsx'
book = load_workbook(path)

writer = pd.ExcelWriter(path, engine='openpyxl')
writer.book = book
df2.to_excel(writer, '11-12')
writer.save()
writer.close()
