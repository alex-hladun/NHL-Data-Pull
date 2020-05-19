import numpy as np
import pandas as pd
import requests


def gamearray(url):
    # takes NHL schedule from NHL API, imports it as a dictionary, and returns a clean list of dataframes
    # (each item in the list is a date) containing relevant info from each game
    r = requests.get(url)
    schedule_data = r.json()
    dates = schedule_data['dates']
    df1 = []
    cols = ['year', 'gamedate', 'gametype', 'time', 'hometeam', 'homegoals', 'homeWs', 'homeLs',
            'homeOTLs', 'awayteam', 'awaygoals', 'awayWs', 'awayLs', 'awayOTLs',
            'homeopenodds', 'homecloseodds', 'awayopenodds', 'awaycloseodds', 'homespreadgoals',
            'awayspreadgoals', 'homespreadodds', 'awayspreadodds', 'openoverunder',
            'openoverodds', 'openunderodds', 'closeoverunder', 'closeoverodds', 'closeunderodds'
            ]
    for date in dates:
        temp = []
        temp2 = []
        for game in date['games']:
            if game['gameType'] == 'R' or game['gameType'] == 'P':
                gamedatetemp = date['date']
                year = gamedatetemp[0:4]
                time = game['gameDate'][10:20]
                gametype = game['gameType']
                hometeam = game['teams']['home']['team']['name']
                homegoals = game['teams']['home']['score']
                hometeamrecord = game['teams']['home']['leagueRecord']
                homeWs = hometeamrecord['wins']
                homeLs = hometeamrecord['losses']
                awayteam = game['teams']['away']['team']['name']
                awaygoals = game['teams']['away']['score']
                awayteamrecord = game['teams']['away']['leagueRecord']
                awayWs = awayteamrecord['wins']
                awayLs = awayteamrecord['losses']
                if 'ot' in awayteamrecord:
                    awayOTLs = awayteamrecord['ot']
                else:
                    awayOTLs = 0
                if 'ot' in hometeamrecord:
                    homeOTLs = hometeamrecord['ot']
                else:
                    homeOTLs = 0
                gamedate = str(
                    int(gamedatetemp[5:7])) + gamedatetemp[8:10]
                homeopenodds = []
                homecloseodds = []
                awayopenodds = []
                awaycloseodds = []
                homespreadgoals = []
                awayspreadgoals = []
                homespreadodds = []
                awayspreadodds = []
                openoverunder = []
                openoverodds = []
                openunderodds = []
                closeoverunder = []
                closeoverodds = []
                closeunderodds = []
                temp.append([year, gamedate, gametype, time, hometeam, homegoals, homeWs, homeLs, homeOTLs,
                             awayteam, awaygoals, awayWs, awayLs, awayOTLs, homeopenodds,
                             homecloseodds, awayopenodds, awaycloseodds, homespreadgoals, awayspreadgoals,
                             homespreadodds, awayspreadodds, openoverunder, openoverodds, openunderodds,
                             closeoverunder, closeoverodds, closeunderodds])
        temp2 = pd.DataFrame(temp, columns=cols)
        df1.append(temp2)
    return df1
