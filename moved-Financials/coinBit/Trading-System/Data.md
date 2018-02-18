### Data soruces 


1/ Just click download button on this page, you get [zip file with 4 data files](https://www.kaggle.com/mczielinski/bitcoin-historical-data)
- bitstamp file has data from 2012 on wards, one min data, coinbase data from 2014 Dec
- all 1 min data, so compact to 1 hour using same Kaggle program ( see )
- first try with Kagggle on site itself, then do same on our local MAC using PANDAS etc..
- I did unzip on local MAC, it showed 4 files,  head on bitstamp file showed 1 min data 

Bitstamp file head show this, see Kaggle how to convert timestamp
```
Timestamp,Open,High,Low,Close,Volume_(BTC),Volume_(Currency),Weighted_Price
1325317920,4.39,4.39,4.39,4.39,0.45558087,2.0000000193,4.39
1325317980,4.39,4.39,4.39,4.39,0.45558087,2.0000000193,4.39
1325318040,4.39,4.39,4.39,4.39,0.45558087,2.0000000193,4.39
1325318100,4.39,4.39,4.39,4.39,0.45558087,2.0000000193,4.39
1325318160,4.39,4.39,4.39,4.39,0.45558087,2.0000000193,4.39
1325318220,4.39,4.39,4.39,4.39,0.45558087,2.0000000193,4.39
```

2/ gives 7d, 2h, 1h percentage chagnes easily with just one call https://github.com/mondeja/pymarketcap/wiki
 - see other coinmarketcap repos (forked) if reqd.
