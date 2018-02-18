 
#### to get all yahoo finance web site data, this Git Repo works
https://github.com/lukaszbanasiak/yahoo-finance

1/ just one caveat , historial quotes for Date Range NOT working, for that use, Pandas-fin (dir)  quote.py program , it uses Google to fetch


2/ installation setps
```
$ git clone git://github.com/lukaszbanasiak/yahoo-finance.git
$ cd yahoo-finance
$ python setup.py install

$python test.py   # run after above install

test.py
-------
from yahoo_finance import Share
yahoo = Share('YHOO')
print yahoo.get_price()
```


3/ Available methods  ( every thing )
```

get_price()
get_change()
get_percent_change()
get_volume()
get_prev_close()
get_open()
get_avg_daily_volume()
get_stock_exchange()
get_market_cap()
get_book_value()



```
