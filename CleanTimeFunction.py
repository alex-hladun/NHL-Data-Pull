def cleantimeanddate(df1, DSTdate):
    # takes list of arrays from gamearray function, and cleans up time and
    # date data (makes easier to read, and converts Zulu time to local time)
    # date must be in format "522" for May 22 or "1012" for October 12, etc

    Pacific1 = ["Vegas Golden Knights", "Anaheim Ducks",
                "Vancouver Canucks", "San Jose Sharks", "Los Angeles Kings"]
    Pacific2 = ["Vegas Golden Knights", "Anaheim Ducks", "Vancouver Canucks", "San Jose Sharks",
                "Los Angeles Kings", "Arizona Coyotes", "Phoenix Coyotes"]
    Mountain1 = ["Calgary Flames", "Colorado Avalanche",
                 "Arizona Coyotes", "Phoenix Coyotes", "Edmonton Oilers"]

    Mountain2 = ["Calgary Flames", "Colorado Avalanche", "Edmonton Oilers"]

    Central = ["St. Louis Blues", "Chicago Blackhawks", "Minnesota Wild",
               "Winnipeg Jets", "Nashville Predators", "Dallas Stars"]

    Eastern = ["Carolina Hurricanes", "Pittsburgh Penguins", "Tampa Bay Lightning", "Detroit Red Wings",
               "Columbus Blue Jackets", "Washington Capitals", "Buffalo Sabres", "Florida Panthers", "Toronto Maple Leafs",
               "Montréal Canadiens", "New Jersey Devils", "Boston Bruins", "Philadelphia Flyers", "New York Rangers",
               "New York Islanders", "Ottawa Senators", "Atlanta Thrashers"]

    DST = False
    for i in range(len(df1)):
        temphour = []
        tempmins = []
        for index, row in df1[i].iterrows():
            time = row['time']
            hour = int(time[1:3])
            mins = time[4:6]
            # find zulu times that carryover to next day
            if hour <= 6 and hour >= 0:
                hour = hour + 24
            if row['gamedate'] == DSTdate:
                DST = True
            if DST == False and row['hometeam'] in Pacific1:
                hour = hour - 8
            elif (DST == False and row['hometeam'] in Mountain1) or (DST == True and row['hometeam'] in Pacific2):
                hour = hour - 7
            elif (DST == False and row['hometeam'] in Central) or (DST == True and row['hometeam'] in Mountain2):
                hour = hour - 6
            elif (DST == False and row['hometeam'] in Eastern) or (DST == True and row['hometeam'] in Central):
                hour = hour - 5
            elif DST == True and row['hometeam'] in Eastern:
                hour = hour - 4
            temphour.append(hour)
            tempmins.append(mins)
        df1[i]['hour'] = temphour
        df1[i]['mins'] = tempmins
        # reorganize columns
        df1[i] = df1[i][['year', 'gamedate', 'gametype', 'time', 'hour', 'mins', 'hometeam', 'homegoals', 'homeWs', 'homeLs',
                         'homeOTLs', 'awayteam', 'awaygoals', 'awayWs', 'awayLs', 'awayOTLs',
                         'homeopenodds', 'homecloseodds', 'awayopenodds', 'awaycloseodds', 'homespreadgoals',
                         'awayspreadgoals', 'homespreadodds', 'awayspreadodds', 'openoverunder',
                         'openoverodds', 'openunderodds', 'closeoverunder', 'closeoverodds', 'closeunderodds'
                         ]]
        del df1[i]['time']
    return df1
