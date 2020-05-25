from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle

fullTeamList = ['Calgary Flames', 'Phoenix Coyotes', 'Edmonton Oilers', 'Arizona Coyotes', 'Colorado Avalanche', 'Vegas Golden Knights', 'Anaheim Ducks', 'Vancouver Canucks', 'San Jose Sharks', 'Los Angeles Kings', 'Carolina Hurricanes', 'Pittsburgh Penguins', 'Tampa Bay Lightning', 'Detroit Red Wings', 'Columbus Blue Jackets', 'Washington Capitals', 'Buffalo Sabres', 'Florida Panthers', 'Toronto Maple Leafs', 'Montréal Canadiens', 'New Jersey Devils', 'Boston Bruins', 'Philadelphia Flyers', 'New York Rangers', 'New York Islanders', 'Ottawa Senators', 'Atlanta Thrashers', 'St. Louis Blues', 'Chicago Blackhawks', 'Minnesota Wild', 'Winnipeg Jets', 'Nashville Predators', 'Dallas Stars']

def openfile(filename):
    infile = open(filename, 'rb')
    df1 = pickle.load(infile)
    infile.close()

    teamStreak = {}
    for team in fullTeamList:
        teamStreak[team] = 0

    for date in range(len(df1)):
        homeTeamStreak =[]
        awayTeamStreak = []
        # print(date)
        # print(year)
        for index, row in df1[date].iterrows():
            # Assign pre-game win/lose streaks for each game 
            homeTeamStreak.append(teamStreak[row['hometeam']])
            awayTeamStreak.append(teamStreak[row['awayteam']])

            # Home team win condition
            if (row['homegoals']>row['awaygoals']):
                # checks current streak for home team 
                if (teamStreak[row['hometeam']] >= 0):
                    teamStreak[row['hometeam']] += 1
                else: 
                    teamStreak[row['hometeam']] = 1

                # checks current streak for away team 
                if (teamStreak[row['awayteam']] <= 0):
                    teamStreak[row['awayteam']] -= 1
                else: 
                    teamStreak[row['awayteam']] = -1

            # Home team lose condition 
            if (row['homegoals'] < row['awaygoals']):
                # checks current streak for home team 
                if (teamStreak[row['hometeam']] <= 0):
                    teamStreak[row['hometeam']] -= 1
                else: 
                    teamStreak[row['hometeam']] = -1

                # checks current streak for away team 
                if (teamStreak[row['awayteam']] >= 0):
                    teamStreak[row['awayteam']] += 1
                else:
                    teamStreak[row['awayteam']] = 1

        df1[date]['homeTeamStreak'] = homeTeamStreak
        df1[date]['awayTeamStreak'] = awayTeamStreak
    return df1


df07 = openfile('2007-08dataset')
df08 = openfile('2008-09dataset')
df09 = openfile('2009-10dataset')
df10 = openfile('2010-11dataset')
df11 = openfile('2011-12dataset')
df12 = openfile('2012-13dataset')
df13 = openfile('2013-14dataset')
df14 = openfile('2014-15dataset')
df15 = openfile('2015-16dataset')
df16 = openfile('2016-17dataset')
df17 = openfile('2017-18dataset')
df18 = openfile('2018-19dataset')
df19 = openfile('2019-20dataset')
df_allyears = [df07, df08, df09, df10, df11, df12, df13, df14, df15,
               df16, df17, df18, df19]
outfile = open("2007-20datasetV2", 'wb')
pickle.dump(df_allyears, outfile)
outfile.close()
