#### Finance Site Product Specification : PRD for the Product

```

0/ find a nice UX/UI on Github  to show Stock Data 

0/ use Python FLASK backend for simplicity , DB may be SQL that is Filebased ..

 Since lot of the data extraction below need custom HTML data extraction , do not worry about Github Lib. Do own Python BS Lib extract
1/ Extract yahoo fiance Data
 - use Github stock data extract programs ( pyton or other ) : get  Tickers, 
 - use Python Beautifulsoup Lib to extract  Analysts 1 year Price Targets ( min, avg, high ) from HTML URL data extradtion 
 - get EPS (TTM) , once you get you can PE (TTM) for any day -->  PE (TTM) =  Price / EPS (TTM )
 
2/ Extract data from Zacks 
 - use Python BS Lib to extract from HTML source, the following
 - Zacks Rank , VGM , VGM overall A - G grade ( Value , Growth, Momentum )
 - Forward PE , EPS current Year, EPS previous Year,  PEG Ratio
 
3/ Extract from FinViz
 - same HTML page data extract using Python BS Lib
 - SMA 20/50/200 , Price change % Month, Q, Half Year, YTD
 - all kinds of PE ratios
 - Analyst Price Targets for 6+  moths  with Dates and Upgrade/downgrade
 
 4/ If possible Extract VectorVest Data ( after saving as file with Windows automated Scripts )
  - See VectorVest video for what to extract 
  - Value, Saftely, Timing 
 ```
 
Trading Thesises 
```
 1.  High Volatile stocks on Earnings day ( see detailed in other post )
 
 2.  Analyse a Stock ( owned by somebody )
   -- Dispaly the following
     - FinViz chart image ( get image URL , do not need image download , it will show image - 
     - Yahoo Analyst 1 Yr Price Target ( min, avg, high ) , show % Premium/discount of 'current price' to ' avg. 1 Yr target price'
      - show other comparable comapnies ( like GOOG, APPLE, FB  when showing PYPL, NFLX )  % premium/discount of abvoe
     - PE Forward , PEG ratio , 

```
 
 
