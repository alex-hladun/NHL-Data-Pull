from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle
infile = open('2007-20dataset', 'rb')
df1 = pickle.load(infile)
infile.close()
print(df1[0][5])
print(df1[0][1].loc[0, "gamedate"])
dfx = pd.read_excel(
    '/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/WeekendDates.xlsx')
dfx = dfx.applymap(str)
n = 0
dfweekend = list()
isempty = []
year = df1[0]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[0:80, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[1]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[98:184, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[2]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[202:288, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[3]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[306:391, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[4]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[410:497, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[5]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[516:603, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[6]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[623:705, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[7]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[724:810, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[8]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[828:914, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[9]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[932:1018, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[10]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[1037:1123, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[11]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[1140:1227, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
year = df1[12]
for date in range(len(year)):
    isempty = year[date].empty
    if (isempty == False) and ((year[date].loc[0, "gamedate"] in dfx.iloc[1245:1300, 1].values.tolist()) or year[date].loc[0, "hour"] <= 16):
        n = n + 1
        print(n)
        dfweekend.append(year[date])
    else:
        n = n + 1
        print(n)
print(dfweekend)
outfile = open("2007-20datasetwknd", 'wb')
pickle.dump(dfweekend, outfile)
outfile.close()
