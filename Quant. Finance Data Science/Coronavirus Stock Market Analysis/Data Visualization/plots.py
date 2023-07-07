

#Plots log return and closing price for a specific stock
def plots(stock):
  # SPY Index
  stock['log return'] = np.log(stock["Adj Close"]/ stock["Adj Close"].shift(1))
  # Line Plot
  fig = plt.figure()

  plt.subplot(2, 2, 1)
  plt.title("Closing price ")
  stock['Adj Close'].plot(style='k.', figsize=(10, 5))
  plt.subplot(2, 2, 2)
  plt.title("Log Return")
  stock['log return'].plot(figsize=(10, 5))
  
  #Histogram
  plt.subplot(2, 2, 3)
  plt.title("Closing Price")
  stock['Adj Close'].hist(figsize=(10, 5))
  plt.subplot(2, 2, 4)
  plt.title("Log Return")
  spy['log return'].hist(figsize=(10, 5))
  
  fig.suptitle('S&P 500 Index')
  
  plt.tight_layout()
  
  plt.show()
