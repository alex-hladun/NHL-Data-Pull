from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle
filename = '2010-11dataset'
infile = open(filename, 'rb')
df1 = pickle.load(infile)
infile.close()
print(type(df1[2].loc[3, 'openoverunder']))
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
        if hometeamWLratio >= 0.58 and row['hour'] <= 16 and hometeamGP >= 25:
            df2 = df2.append(df1[i].iloc[index, :])
overWL = []
profit = []
for index, row in df2.iterrows():
    print(type(df2.loc[index, 'openoverunder']))
print(df2.iloc[10, :])
