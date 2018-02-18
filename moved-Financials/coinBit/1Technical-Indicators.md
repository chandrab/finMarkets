### Various Technical Indicators 

**TODO **
 - **Item 2.2** mentioned below
 - create new github repo for  FinMarkets i) copy all from parent repo ii) delete pareent repo later ( use "git rm -r * " )
 
**1. Moving Avarge Envelop  (MA Env)**
- Tradingview.com,  yahoo finnce both have this "MA Env" is standard indicators, so it seems this is a popular indicator
- Tradingview.com has "MA Envelop" 20, 10 as default parameters, that is 20MA with 10% up/down envelop, 
- this (20,10) envelop seems represent well in case of EBAY and PAYPL stocks 
- in case of BTCUSD the envelop (30,20) that is 30MA and 20% up/down envelop shows  Chart well, so we need to adjust this base on stock Volatailty. 
- as for as volume is converned, 10d volume gives good VISUAL indication on chart( 20d ma (default) of volume does not show clear Volume Trend )

- some custom indicators on Tradingview.com , this guy [LazyBear has ton of free indicators on Trading view](https://www.tradingview.com/chart/BTCUSD/4IneGo8h-Master-Index-List-of-all-my-indicators/#c100282)
- [Range Identifier](https://www.tradingview.com/script/FnFOxVIY-Range-Identifier-LazyBear/) , tons of Indicators [on google docs](https://docs.google.com/document/d/15AGCufJZ8CIUvwFJ9W-IKns88gkWOKBCvByMEvm5MLo/edit)

**2. days since touching MA line ( 30d MA, 50d MA, 100d MA )**
- 2.1 In case of BTCUSD (tradinview symbol) , it seems BTC follow the rules like price will touch 30d MA line in 30 days, 50d MA line 50 days etc.. only in case of great bull RUN from November 12 it touched on December 22 that is 40 days instead of 30 days . On all other cases of past 1 year it touched in 30 days. 
- **2.2 Test  above hypothesis** with  Pandas/Nummypy/Zipline (need to bring own data) or with Kaggle (they have data) for for BTC . Find at what % it **obeyed touching 30/50/75 day line since the last touch with in those days of 30/70/75 for last 3 years**
 ```
-----------------------------------------------------------------------------------------
   TYPE   | with in % | median days | outside % | median days | outside min | outside Max
-----------------------------------------------------------------------------------------
 30 d MA  |
 
 50 d MA  |
   
 75 d MA  |
-----------------------------------------------------------------------------------------
``` 

**3. Automatically find which Envelop fit the current stock**
- for Ebay, Paypal  Env(20,10) worked  20 d MA,  10%  upper/lower envelop fit 95% of  Price points
- for  BTCuSD  Env(30,20)  fitted 
- so automatically find which one
- basically code tries each envelop and see 90% is staying inside the envelop
  for ma  in range(15, 40, 5 )   # 15 to 40 with increments of 5
      band1 =   ma +  ma /2 
      band2 =   ma =  ma /2 
      ma_val 

