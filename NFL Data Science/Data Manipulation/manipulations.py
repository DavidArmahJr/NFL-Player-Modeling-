



# Filters datasets to contain specific columns
def initialFilterDF(dfPass,dfRush,dfReceive,dfOffense,dfDefense,dfPlays):
    filteredPass = dfPass[['Player', 'Team', 'Gms', 'Att','Cmp', 'Yds', 'TD', 'Int', 'Sack', 'Loss']]
    filteredRush = dfRush[['Player', 'Team', 'Gms', 'Att', 'Yds', 'TD', 'FD']]
    filteredReceive = dfReceive[['Player', 'Team', 'Gms', 'Rec', 'Yds', 'TD', 'FD', 'Tar', 'YAC']]
    filteredOffense = dfOffense[['Team','Gms', 'Tot_Pts', 'RushYds', 'PassYds', 'TotYds']]
    filteredDefense = dfDefense[['Team','Gms', 'Tot_Pts', 'RushYds', 'PassYds', 'TotYds']]
    filteredPlays = dfPlays[['Team', 'Gms', 'Plays', 'Rush', 'Pass']]
    
    return filteredPass, filteredRush, filteredReceive, filteredOffense, filteredDefense, filteredPlays

# Calculates Per game data for all datasets
def getAvgDF(passing, rushing, receiving, teamOffense, teamDefense, plays):
    passing[['Att', 
                  'Cmp', 'Yds', 'TD', 'Int', 'Sack', 'Loss']] = passing[[ 'Att', 
                                                                        'Cmp', 'Yds', 'TD', 'Int', 'Sack', 'Loss']].div(passing['Gms'].values,axis=0)
    rushing[['Att', 'Yds', 'TD', 'FD']] = rushing[['Att', 'Yds', 'TD', 'FD']] \
    .div(rushing['Gms'].values, axis=0)
    
    receiving[['Tar','Rec', 'Yds', 'YAC', 'FD', 'TD']] = receiving[['Tar','Rec', 'Yds', 'YAC', 'FD', 'TD']] \
    .div(receiving['Gms'].values, axis = 0)
    
    teamOffense[['PassYds', 'RushYds','TotYds', 'Tot_Pts']] =  teamOffense[['PassYds', 'RushYds',
                                                                            'TotYds', 'Tot_Pts']].div(teamOffense['Gms'].values, axis=0)
    
    teamDefense[['PassYds', 'RushYds','TotYds', 'Tot_Pts']] =  teamDefense[['PassYds', 'RushYds',
                                                                            'TotYds', 'Tot_Pts']].div(teamDefense['Gms'].values, axis=0)
    
    plays[['Rush', 'Pass']] = plays[['Rush', 'Pass']].div(plays['Plays'].values, axis=0)
    
    plays[['Plays']] = plays[['Plays']].div(plays['Gms'].values, axis=0)
    
    
    
    return passing, rushing, receiving, teamOffense, teamDefense, plays

# Calculates Team average across the league
def leagAvgDF(avgO, avgD, avgP):
    return avgO[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']].mean(), \
            avgD[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']].mean(), avgP[['Plays', 'Rush', 'Pass']].mean()

# Calculates Difference of Teams to average team
def avgLeagDiffDF(avgO, leagO, avgD, leagD, avgP, leagP):
    avgO[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']] = avgO[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']] - leagO
    avgD[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']] = avgD[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']] - leagD
    avgP[['Plays', 'Rush', 'Pass']] = avgP[['Plays', 'Rush', 'Pass']] - leagP
    return avgO, avgD, avgP

# Calculates comparison of team vs league 
def avgLeagRatioDF(avgO, leagO, avgD, leagD, avgP, leagP):
    avgO[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']] = avgO[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']].div(leagO)
    avgD[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']] = avgD[['Tot_Pts', 'RushYds', 'PassYds', 'TotYds']].div(leagD)
    avgP[['Plays', 'Rush', 'Pass']] = avgP[['Plays', 'Rush', 'Pass']].div(leagP)
    return avgO, avgD, avgP

# Renames Column names 
def renamePlayerCols(passing, rushing, receiving):
    passing_cols = ['Player', 'Team', 'Gms', 'Passing_Att', 'Passing_Cmp', 'Passing_Yds', 'Passing_TD', 'Passing_Int',
                    'Sack','SackYds_Loss']
    rushing_cols = ['Player', 'Team', 'Gms', 'Rushing_Att', 'Rushing_Yds', \
                        'Rushing_TD', 'Rushing_FD']
    receiving_cols = ['Player', 'Team', 'Gms', 'Receiving_Rec', 'Receiving_Yds', 'Receiving_TD', 'Receiving_FD',
                       'Receiving_Tar','Receiving_YAC']

    passing.columns = passing_cols
    rushing.columns = rushing_cols
    receiving.columns = receiving_cols

# Combines Dataframes into bigger data containing similar data
def combinePlayerDF(filteredPass,filteredRush,filteredReceive,avgPass,avgRush,avgReceive):
    fullPlayerDF = filteredPass.set_index('Player') \
                .combine_first(filteredRush.set_index('Player')) \
                .combine_first(filteredReceive.set_index('Player'))

    fullPlayerAvgsDF = avgPass.set_index('Player') \
                .combine_first(avgRush.set_index('Player')) \
                .combine_first(avgReceive.set_index('Player'))
    
   
    
    columnOrder = ['Team', 'Gms', 'Passing_Att','Passing_Cmp', 'Passing_Yds', 'Passing_TD', 
           'Passing_Int','Sack', 'SackYds_Loss','Rushing_Att', 'Rushing_Yds', 
           'Rushing_TD', 'Rushing_FD', 'Receiving_Tar', 'Receiving_Rec',
            'Receiving_Yds','Receiving_TD','Receiving_FD','Receiving_YAC'   ]

    fullPlayerDF = fullPlayerDF[columnOrder].fillna(0)
    fullPlayerAvgsDF = fullPlayerAvgsDF[columnOrder].fillna(0)
    
    return fullPlayerDF[columnOrder], fullPlayerAvgsDF[columnOrder]
