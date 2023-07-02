def LR_PG(X,Y, PlayerPerGame):
    X_train, X_test, y_train, y_test = train_test_split(PlayerPerGame[X], 
                                                        PlayerPerGame[Y])
    #Create Linear model
    LR = LinearRegression()
    LR.fit(X_train.values.reshape(-1,1), y_train.values)
    
    
    def modelPerformance(lr, X_train, y_train):
        y_pred_train = lr.predict(X_train.values.reshape(-1,1))
        return r2_score(y_train, y_pred_train)
    
    #print(modelPerformance(LR, X_train, y_train))

    
    
    prediction = LR.predict(X_test.values.reshape(-1,1))
    #print("Mean squared error of Linear Regression: %.2f" % mean_squared_error(y_test, prediction))
    return LR
    
def LR_Predict(LR, value):
    x= LR.predict(np.array([[value]]))[0]
    return x
    
def run_LR(playerAvg):
    linearReg = pd.DataFrame()
    
    linearReg.index = playerAvg.index
    
    linearReg['LR_Passing_Att']= [LR_Predict( \
        LR_PG('Passing_Cmp', 'Passing_Att', playerAvg), i)for i in playerAvg['Passing_Cmp']]
                                  
    linearReg['LR_Passing_Cmp'] = [LR_Predict( \
        LR_PG('Passing_Att', 'Passing_Cmp', playerAvg), i)for i in playerAvg['Passing_Att']]  
                                  
    linearReg['LR_Passing_Yds']= [LR_Predict( \
        LR_PG('Passing_Cmp', 'Passing_Yds', playerAvg), i)for i in playerAvg['Passing_Cmp']]
                                  
    linearReg['LR_Passing_TD']= [LR_Predict( \
        LR_PG('Passing_Yds', 'Passing_TD', playerAvg), i)for i in playerAvg['Passing_Yds']]
    
    linearReg['LR_Passing_Int']= [LR_Predict( \
        LR_PG('Passing_Att', 'Passing_Int', playerAvg), i)for i in playerAvg['Passing_Att']]
                                  
                                  
    linearReg['LR_Rushing_Att']= [LR_Predict(
        LR_PG('Rushing_Yds', 'Rushing_Att', playerAvg), i)for i in playerAvg['Rushing_Yds']]
                                  
    linearReg['LR_Rushing_Yds']= [LR_Predict(
        LR_PG(['Rushing_Att'], 'Rushing_Yds',playerAvg), i)for i in playerAvg['Rushing_Att']]
                                  
    linearReg['LR_Rushing_TD']= [LR_Predict(
        LR_PG('Rushing_FD', 'Rushing_TD',playerAvg), i)for i in playerAvg['Rushing_FD']]
                                  
    linearReg['LR_Receiving_Tar']= [LR_Predict(
        LR_PG('Receiving_Rec', 'Receiving_Tar', playerAvg), i)for i in playerAvg['Receiving_Rec']]
    
    linearReg['LR_Receiving_Rec']= [LR_Predict(
        LR_PG('Receiving_Tar', 'Receiving_Rec', playerAvg), i)for i in playerAvg['Receiving_Tar']]
                                  
    linearReg['LR_Receiving_Yds']= [LR_Predict(
        LR_PG('Receiving_Rec', 'Receiving_Yds', playerAvg), i)for i in playerAvg['Receiving_Rec']]
                                  
    linearReg['LR_Receiving_TD']= [LR_Predict(
        LR_PG('Receiving_FD', 'Receiving_TD', playerAvg), i)for i in playerAvg['Receiving_FD']]

    return pd.concat([playerAvg, linearReg], axis=1)





def monteCarlo_LinearReg(df):
    list1 = []
    for i in range(0,100):
        linearRegTable = run_LR(fullPlayerAvgsDF)
        list1.append(linearRegTable)
    result = pd.concat(list1)
    return result.groupby(level=0).mean()
