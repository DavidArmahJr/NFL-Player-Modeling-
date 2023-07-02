import requests
from bs4 import BeautifulSoup
import pandas as pd
import html5lib


# Test the Section 1 Method with various cases
def testConfigure(url):
    examDF = configure(url)
    assert examDF is not None

# Good Link Test
testConfigure('https://www.footballdb.com/statistics/nfl/player-stats/passing/2022/regular-season?sort=passrate&limit=all')
#rushing)
# Bad Link Test
testConfigure('https://www.footbaldb.com/statistics/nfl/player-stats/passing/2022/regular-season?sort=passrate&limit=all')
   
