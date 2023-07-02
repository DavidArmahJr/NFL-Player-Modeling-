import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib

# Retrieves Table from url (footballdb.com)
def configureFootballDB(url):
    
    
    ## Create header to access Webpage
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    
    try:
        #Retrieve Webpage Table
        data = requests.get(url, headers=hdr)
        soup = BeautifulSoup(data.text, 'html.parser')
        table = soup.find_all('table')
        df = pd.read_html(str(table))[0]

        if (df.empty):
          print("No table found from " + url)
        else:
          print('Successfully retrieved table from ' + url)
        return df
    except Exception as error:
        #Throw Error
        print('Unsuccesful Retrieval: Error trying to retrieve table from given Url', error)
        
