def MLR_PG(X,Y, PlayerPerGame):
    X_train, X_test, y_train, y_test = train_test_split(PlayerPerGame[X].to_numpy(), 
                                                        PlayerPerGame[Y])
    #Create Linear model
    MLR = LinearRegression()
    MLR.fit(X_train, y_train.values)
    
    
    def modelPerformance(mlr, X_train, y_train):
        y_pred_train = mlr.predict(X_train)
        return r2_score(y_train, y_pred_train)
    
    #print(modelPerformance(MLR, X_train, y_train))

    
    
    prediction = MLR.predict(PlayerPerGame[X].values)
    #print("Mean squared error of Linear Regression: %.2f" % mean_squared_error(y_test, prediction))
    return prediction

def run_MLR(playerAvg):
    mullinearReg = pd.DataFrame()
    
    mullinearReg.index = playerAvg.index
    
    mullinearReg['MLR_Passing_Att']= MLR_PG(['Passing_Cmp', 'Passing_Yds', 'Passing_TD', \
                                             'Passing_Int','Sack', 'SackYds_Loss'], 'Passing_Att', playerAvg)
                                  
    mullinearReg['MLR_Passing_Cmp'] = MLR_PG(['Passing_Att', 'Passing_Yds', 'Passing_TD', \
                                              'Passing_Int','Sack', 'SackYds_Loss'], 'Passing_Cmp', playerAvg)
                                  
    mullinearReg['MLR_Passing_Yds']= MLR_PG(['Passing_Att', 'Passing_Cmp', \
                                             'Passing_TD', 'Passing_Int','Sack', 'SackYds_Loss'], 'Passing_Yds', playerAvg)
                                  
    mullinearReg['MLR_Passing_TD']=  MLR_PG(['Passing_Att', 'Passing_Cmp', 'Passing_Yds', \
                                          'Passing_Int','Sack', 'SackYds_Loss'], 'Passing_TD', playerAvg)
    
    mullinearReg['MLR_Passing_Int']= MLR_PG(['Passing_Att','Passing_Cmp', 'Passing_Yds', \
                                             'Passing_TD','Sack', 'SackYds_Loss'], 'Passing_Int', playerAvg)
                                  
    mullinearReg['MLR_Rushing_Att']= MLR_PG(['Rushing_Yds','Rushing_FD'], 'Rushing_Att', playerAvg)
                                  
    mullinearReg['MLR_Rushing_Yds']= MLR_PG(['Rushing_Att', 'Rushing_FD'], 'Rushing_Yds',playerAvg)
                                  
    mullinearReg['MLR_Rushing_TD']=  MLR_PG(['Rushing_Att', 'Rushing_Yds','Rushing_FD'], 'Rushing_TD',playerAvg)
                                  
    mullinearReg['MLR_Receiving_Tar']= MLR_PG(['Receiving_Rec', 'Receiving_Yds'], 'Receiving_Tar', playerAvg)
    
    mullinearReg['MLR_Receiving_Rec']= MLR_PG(['Receiving_Tar', 'Receiving_Yds', 'Receiving_YAC'], 'Receiving_Rec', playerAvg)
                                  
    mullinearReg['MLR_Receiving_Yds']=  MLR_PG(['Receiving_Rec', 'Receiving_Tar', \
                                                'Receiving_FD'], 'Receiving_Yds', playerAvg)
                                  
    mullinearReg['MLR_Receiving_TD']= MLR_PG(['Receiving_Yds','Receiving_FD'], 'Receiving_TD', playerAvg)

    return pd.concat([playerAvg, mullinearReg], axis=1)





def monteCarlo_mulLinearReg(df):
    list1 = []
    for i in range(0,100):
        mullinearRegTable = run_MLR(df)
        list1.append(mullinearRegTable)
    result = pd.concat(list1)
    return result.groupby(level=0).mean()

