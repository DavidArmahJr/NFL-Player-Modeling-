#Necessary Imports
import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib
import unittest
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
import xgboost
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from xgboost import XGBRegressor
pd.options.display.float_format ='{:.2f}'.format


#passing table URL
passing_stats = 'https://www.footballdb.com/statistics/nfl/player-stats/passing/2022/regular-season?sort=passrate&limit=all'
#rushing table URL
rushing_stats = 'https://www.footballdb.com/statistics/nfl/player-stats/rushing/2022/regular-season?sort=rushyds&limit=all'
#receiving table URL
receiving_stats = 'https://www.footballdb.com/statistics/nfl/player-stats/receiving/2022/regular-season?sort=recnum&limit=all'
#team offense URL
offensive_stats = 'https://www.footballdb.com/stats/teamstat.html?lg=NFL&yr=2022&type=reg&cat=T&group=O&conf='
#team defense URL
defensive_stats = 'https://www.footballdb.com/stats/teamstat.html?lg=NFL&yr=2022&type=reg&cat=T&group=D&conf='
#play selection data URL for year 2022 Testing
plays_stats = 'https://www.footballdb.com/stats/play-selection.html' 

# Collect and clean Datasets

# Player data
dfPass = configure(passing_stats)
cleanPlayerName(dfPass)
cleanPlayerData(dfPass)
dfRush = configure(rushing_stats)
cleanPlayerName(dfRush)
cleanPlayerData(dfRush)
dfReceive = configure(receiving_stats)
cleanPlayerName(dfReceive)
cleanPlayerData(dfReceive)

# Team data
dfOffense = configure(offensive_stats)
cleanTeamName(dfOffense)
cleanTeamData(dfOffense)
dfDefense = configure(defensive_stats)
cleanTeamName(dfDefense)
cleanTeamData(dfDefense)
dfPlays = configure(plays_stats)
cleanTeamName(dfPlays)
cleanTeamData(dfPlays)



avgPass, avgRush, avgReceive, \
avgTeamO, avgTeamD, avgTeamPlays = getAvgDF(filteredPass.copy(), filteredRush.copy(), filteredReceive.copy(), \
                                                                        filteredOffense.copy(), filteredDefense.copy(), filteredPlays.copy())
leagO, leagD, leagP = leagAvgDF(avgTeamO.copy(), avgTeamD.copy(), avgTeamPlays.copy())

avgDiffTeamO,avgDiffTeamD, avgDiffTeamP = avgLeagDiffDF(avgTeamO.copy(),leagO.copy(), \
                                                      avgTeamD.copy(), leagD.copy(), avgTeamPlays.copy(), leagP.copy())
avgRatioTeamO,avgRatioTeamD, avgRatioTeamP = avgLeagRatioDF(avgTeamO.copy(),leagO.copy(),\
                                                          avgTeamD.copy(), leagD.copy(), avgTeamPlays.copy(), leagP.copy())

renamePlayerCols(filteredPass, filteredRush, filteredReceive)
renamePlayerCols(avgPass, avgRush, avgReceive)

fullPlayerDF, fullPlayerAvgsDF = combinePlayerDF(filteredPass,filteredRush,filteredReceive,avgPass,avgRush,avgReceive)


