import os
from urllib.request import urlopen

url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'

local_path = os.path.join('data', 'GOOG.csv')
with urlopen(url) as image, open(local_path, 'wb') as f:
    f.write(image.read())
