import pandas as pd
import numpy as np
import datetime
import yfinance as yf

# stocks - List of stocks
# startD - start date
# endD- end date to look at stock
def getStocks(stocks,startD, endD):
    stockVals = []
    for i in stocks:
        currStock = yf.download(i, start=startD, end=endD)
        stockVals.append(currStock['Adj Close'])
        
    df = pd.DataFrame(stockVals)
    df.index = stocks
    
    return df.transpose()
    
  
