import matplotlib.pyplot as plt
import pandas as pd

%matplotlib inline

def playerPlot(df, x1, y1): 
    
    def plotlabel(xvar, yvar, label):
        ax.text(xvar+0.002, yvar, label)
        
    fig = plt.figure(figsize=(30,10))
    ax = sns.scatterplot(x = x1, y =  y1, data=df)

    # The magic starts here:
    df.apply(lambda x: plotlabel(x[x1],  x[y1], x['Player']), axis=1)

    plt.title(x1 + ' v. ' + y1)
    plt.xlabel(x1)
    plt.ylabel(y1)
    
