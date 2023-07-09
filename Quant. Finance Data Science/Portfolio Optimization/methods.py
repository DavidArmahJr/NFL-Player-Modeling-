import pandas as pd
import numpy as np
import yfinance as yf
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import missingno as msno
%matplotlib inline
# Choose stocks to add in Portfolio
def createPortfolio(tickerList):
    Pr = pd.DataFrame()
    end = date.today()
    start = end - date.timedelta(5 * 365)
    for ticker in tickerList:
        tmp_close = yf.download(ticker,
                           start=start,
                           end=end,
                           progress=False)['Adj Close']
        Pr = pd.concat([Pr, tmp_close], axis=1)
    Pr.columns = tickerList
# Daily Log returns of Portolio
def buildTimeSeries(Pr):
    re = np.log(Pr/Pr.shift(1)).dropna(how='any')
    return re


# the objective function is to minimize the portfolio risk
def objective(re,weights):
    weights = np.array(weights)
    return weights.dot(re.cov()).dot(weights.T)
# The constraints
    cons = (# The weights must sum up to one.
        {"type":"eq", "fun": lambda x: np.sum(x)-1}, 
        # This constraints says that the inequalities (ineq) must be non-negative.
        # The expected daily return of our portfolio and we want to be at greater than 0.003
        {"type": "ineq", "fun": lambda x: np.sum(re.mean()*x)-0.003})
# Every stock can get any weight from 0 to 1
    bounds = tuple((0,1) for x in range(re.shape[1]))
# Initialize the weights with an even split
# In out case each coin will have (1/# of coins) % at the beginning
    guess = [1./re.shape[1] for x in range(re.shape[1])]
    optimized_results = minimize(objective, guess, method = "SLSQP", bounds=bounds, constraints=cons)
    return optimized_results # The optimum weights
# Expected Portfolio Returns
def exp_return(opt_res, time_ser):
    return np.sum(re.mean()*optimized_results.x)
# Random allocation experiment to calculate correct portfolio distributions
def rand_exp(re):
    weights = np.array(np.random.random(re.shape[1]))
    print('Random Weights:')
    print(weights)

    print('Rebalance')
    weights1 = weights/np.sum(weights)
    print(weights1)

    # expected return
    print('Expected Portfolio Return')
    exp_ret = np.sum((re.mean()*weights1)*365) #
    print(exp_ret)

    # expected volatility
    print('Expected Volatility')
    exp_vol = np.sqrt(np.dot(weights1.T,np.dot(re.cov()*365, weights1)))
    print(exp_vol)

    # Sharpe Ratio
    print('Sharpe Ratio')
    SR = exp_ret/exp_vol
    print(SR)
    
    return weights, weights1, exp_ret, exp_vol, SR
# monte carlo simulation of random portfolio allocations
def randn_exp(re, num_ports):
    all_weights = np.zeros((num_ports, len(re.columns)))
    ret_arr = np.zeros(num_ports)
    vol_arr = np.zeros(num_ports)
    sharpe_arr = np.zeros(num_ports)

    for ind in range(num_ports): 
        # weights 
        weights = np.array(np.random.random(re.shape[1])) 
        weights = weights/np.sum(weights)  
    
        # save the weights
        all_weights[ind,:] = weights

        # expected return 
        ret_arr[ind] = np.sum((re.mean()*365*weights))

        # expected volatility 
        vol_arr[ind] = np.sqrt(np.dot(weights.T,np.dot(re.cov()*365, weights)))

        # Sharpe Ratio 
        sharpe_arr[ind] = ret_arr[ind]/vol_arr[ind]
    return all_weights, ret_arr, vol_arr, sharpe_arr
    
    
