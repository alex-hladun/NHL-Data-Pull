import pandas as pd


def NHLoddsmerger(df1, Excelfilepath):

    dfx = pd.read_excel(Excelfilepath)
    dfx['Date'] = dfx['Date'].apply(str)
    n = 0
    for i in range(len(df1)):
        for index, row in df1[i].iterrows():
            for index2, row2 in dfx.iterrows():
                if row['hometeam'] == row2['Team'] and row['gamedate'] == row2['Date']:
                    n = n + 1
                    print(n)
                    df1[i].loc[index, 'homeopenodds'] = row2['Open']
                    df1[i].loc[index, 'homecloseodds'] = row2['Close']
                    df1[i].loc[index, 'awayopenodds'] = dfx.loc[index2 - 1, 'Open']
                    df1[i].loc[index,
                               'awaycloseodds'] = dfx.loc[index2 - 1, 'Close']
                    df1[i].loc[index, 'homespreadgoals'] = row2['PuckLineGoals']
                    df1[i].loc[index, 'awayspreadgoals'] = dfx.loc[index2 -
                                                                   1, 'PuckLineGoals']
                    df1[i].loc[index, 'homespreadodds'] = row2['PuckLineOdds']
                    df1[i].loc[index, 'awayspreadodds'] = dfx.loc[index2 -
                                                                  1, 'PuckLineOdds']
                    df1[i].loc[index, 'openoverunder'] = row2['OpenOUGoals']
                    df1[i].loc[index,
                               'openoverodds'] = dfx.loc[index2 - 1, 'OpenOUOdds']
                    df1[i].loc[index, 'openunderodds'] = row2['OpenOUOdds']
                    df1[i].loc[index, 'closeoverunder'] = row2['CloseOUGoals']
                    df1[i].loc[index, 'closeoverodds'] = dfx.loc[index2 -
                                                                 1, 'CloseOUOdds']
                    df1[i].loc[index, 'closeunderodds'] = row2['CloseOUOdds']
                    break
    return df1
