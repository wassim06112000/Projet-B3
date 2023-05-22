import pandas_datareader
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import yfinance as yf
from pandas.plotting import scatter_matrix

start = datetime.datetime(1986,1,1)
end = datetime.datetime.now()
print (end)
print(start)
pepsi = yf.download('PEP', start=start, end=end)
Coca = yf.download('KO', start=start, end=end)


pepsi['returns'] = pepsi['Close'].pct_change(1)
Coca['returns'] = Coca['Close'].pct_change(1)

pepsi['returns'].hist(bins= 100, label = 'Pepsi', figsize = (10,8), alpha = 0.9 )
Coca['returns'].hist(bins= 100, label = 'Coca', alpha = 0.6  )
plt.legend()
plt.show()
