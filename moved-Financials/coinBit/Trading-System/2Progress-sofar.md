### Progress made with Trading Bot

#### TODO : 
  - first simple try on Quantopian
  - then goto zipline, Quandl, quantopian ( has onsite forum) and ask what is best way before investing much time

####  Zipline with  LIVE Trading
- contributors and reviewers [needed for Zipline-Live](https://www.quantopian.com/posts/contributors-and-reviewers-needed-for-zipline-live)
- On premise [live trading with zipline](http://www.zipline-live.io/tutorial)
- It seems this Zipline-Live is working with REAL Trading Account with IB, soon this Github repo will be more developed with more features.
- **sr: we can use Quantoinan for NOW and in few months Zipline-Live will be more Ready**

#### 0/ Quontopian - all Web based Client , DATA is Free
  - see this video, may be we need this [simple instaed of installing etc..](https://www.quantopian.com/tutorials/algorithmic-trading-sentdex#lesson2) 
  - we can test our SMA25, SMA50 with EBAY how many days it takes to come back ..
  - may be Quontoipan may have Bitcoin DATA, check ....

#### 1.2/ Zipline
 - see if we can get EOD data with Yahoo finance lib on github , then Run zipline python 
 - see good Stragegy example : 
 - AS [stated below](https://github.com/quantopian/zipline) , seems Quandl and Zipline allmost together ....
 - [Clean example with TagLib](https://github.com/quantopian/zipline/blob/master/zipline/examples/dual_ema_talib.py)
 - [latest example of 2018 ](https://github.com/quantopian/zipline/blob/master/zipline/examples/momentum_pipeline.py)
 - [profit Target example](https://github.com/enigmampc/catalyst/blob/master/catalyst/examples/rsi_profit_target.py)
 ```
 You can then run this algorithm using the Zipline CLI; you'll need a Quandl API key to ingest the default data bundle. 
 Once you have your key, run the following from the command line:

$ QUANDL_API_KEY=<yourkey> zipline ingest -b quandl
$ zipline run -f dual_moving_average.py --start 2014-1-1 --end 2018-1-1 -o dma.pickle
This will download asset pricing data data from quandl, and stream it through the algorithm over the specified time range. Then, the resulting performance DataFrame is saved in dma.pickle, which you can load an analyze from within Python.
```

#### 1.3/ [using Quandl with Python](https://github.com/quandl/quandl-python/blob/master/FOR_DEVELOPERS.md) 
- see if we can get simple EOD data Free 
- [see if EOD data is Free](https://www.quandl.com/tools/api)


#### 2/ [quantRocket](https://www.quantrocket.com/#product-roadmap) : 
- They promise Paid service to connect to Algo trading in Q1 of 2018 ( see bottom of the page). If they Deliver it can be used for $20/month
 - [note book](https://www.quantrocket.com/docs/#research-notebooks)

#### 3/ Interactive Brokers Python Client

- IB Official client software :  [client](http://interactivebrokers.github.io/#) [general info](https://interactivebrokers.github.io/tws-api/#gsc.tab=0)

- IbPy - [Interactive Brokers Python API](https://github.com/blampe/IbPy/blob/master/demo/api_coverage.py)
------------------

#### 4/ Catalyst install & run --- ONLY use for CRYPTO, for Stocks zipline/quandl/quntopian seems better 
 - asr: this is good for  Crypto Pairs, since the compay Enigma tested it will pairs on crypto exchanges ..
 - [profit Target example](https://github.com/enigmampc/catalyst/blob/master/catalyst/examples/rsi_profit_target.py)
- we already have Conda installed
- this [command got all neeed code](https://enigmampc.github.io/catalyst/install.html)  
  + $conda env create -f python2.7-environment.yml ; $source activate catalyst 
- Errors [disappeard with this command](https://enigmampc.github.io/catalyst/install.html#macos-virtualenv-conda-matplotlib)
- 
- In order to run the code above, you have to ingest the needed data first:
    + $catalyst ingest-exchange -x bitfinex -f minute -i ltc_usd ( where are the files it got the DATA download ?? not in current dir)
- ran algo sample file with this command
    + $catalyst run -f dual_moving_average.py -x bitfinex -s 2017-9-22 -e 2017-9-23 --capital-base 1000 --base-currency usd --data-frequency minute -o out.pickle
    
- It printed 2 trades, but hanged probably in matplotlib, no output files written in current dir 
 +  Beginning with release 9.73, InteractiveBrokers is **now officially supporting a new Python API client (Python 3 only)**. 
 +  This should make this repo superfluous except for Python 2. ( if we want to use above CATALYST which is python2 , we can use this Python2 Lib to connect to IB)

    
