from pandas import ExcelWriter
from openpyxl import load_workbook
import pandas as pd
import numpy as np
import pickle
filename = '2007-20dataset'
infile = open(filename, 'rb')
df1 = pickle.load(infile)
infile.close()
df2 = pd.DataFrame()

fullTeamList = ['Calgary Flames', 'Phoenix Coyotes', 'Edmonton Oilers', 'Arizona Coyotes', 'Colorado Avalanche', 'Vegas Golden Knights', 'Anaheim Ducks', 'Vancouver Canucks', 'San Jose Sharks', 'Los Angeles Kings', 'Carolina Hurricanes', 'Pittsburgh Penguins', 'Tampa Bay Lightning', 'Detroit Red Wings', 'Columbus Blue Jackets', 'Washington Capitals', 'Buffalo Sabres', 'Florida Panthers', 'Toronto Maple Leafs', 'Montréal Canadiens', 'New Jersey Devils', 'Boston Bruins', 'Philadelphia Flyers', 'New York Rangers', 'New York Islanders', 'Ottawa Senators', 'Atlanta Thrashers', 'St. Louis Blues', 'Chicago Blackhawks', 'Minnesota Wild', 'Winnipeg Jets', 'Nashville Predators', 'Dallas Stars']

# Creates a dictionary with each team, and their current streak
teamStreak = {}
for team in fullTeamList:
    teamStreak[team] = 0

for year in range(len(df1)):
    homeTeamStreak =[]
    awayTeamStreak = []
    for date in range(len(df1[year])):
        print(date)
        print(year)
        for index, row in df1[year][date].iterrows():
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

    print(teamStreak)

        #     print(df1[year][date]['hometeam'])
            # if (row['homeLs'] + row['homeOTLs']) != 0:
            #     hometeamWpercent = row['homeWs'] / \
            #         (row['homeWs'] + row['homeLs'] + row['homeOTLs'])
            # else:
            #     hometeamptpercent = 0
            # if (row['awayLs'] + row['awayOTLs']) != 0:
            #     awayteamWpercent = row['awayWs'] / \
            #         (row['awayWs'] + row['awayLs'] + row['awayOTLs'])
            # else:
            #     awayteamWpercent = 0
            # hometeamGP = row['homeWs'] + row['homeLs'] + row['homeOTLs']
            # awayteamGP = row['awayWs'] + row['awayLs'] + row['awayOTLs']
            # if (awayteamWpercent <= 0.48 and hometeamGP >= 15) and (row['hour'] <= 16 or weekenddate == row["gamedate"]):
            #     weekenddate = row["gamedate"]
            # Adds the entire row to the second dataframe. 
            #     df2 = df2.append(df1[year][date].iloc[index, :])
# moneylineWL = []
# profit = []
# for index, row in df2.iterrows():
#     if row['homegoals'] > row['awaygoals']:
#         moneylineWL.append('W')
#         if row['homecloseodds'] > 0:
#             profit.append(row['homecloseodds']/100)
#         else:
#             profit.append(-100/row['homecloseodds'])
#     else:
#         moneylineWL.append('L')
#         profit.append(-1)
# df2['moneylineWL'] = moneylineWL
##Assign column to new dataframe. 
# df2['profit'] = profit
# df2 = df2[['year', 'gamedate', 'gametype', 'hour', 'mins', 'hometeam', 'homegoals', 'homeWs', 'homeLs',
#            'homeOTLs', 'awayteam', 'awaygoals', 'awayWs', 'awayLs', 'awayOTLs',
#            'homeopenodds', 'homecloseodds', 'awayopenodds', 'awaycloseodds', 'homespreadgoals',
#            'awayspreadgoals', 'homespreadodds', 'awayspreadodds', 'openoverunder',
#            'openoverodds', 'openunderodds', 'closeoverunder', 'closeoverodds', 'closeunderodds',
#            'moneylineWL', 'profit']]

# print(df2)
# sum = df2['profit'].sum()
# print(sum)
# path = r'/Users/willmadsen/Documents/Python Stuff/Sports Betting Code/BetHomeIfAfternoonVisitor<48%Wins.xlsx'
# book = load_workbook(path)

# writer = pd.ExcelWriter(path, engine='openpyxl')
# writer.book = book
# df2.to_excel(writer, '07-20 Results')
# writer.save()
# writer.close()