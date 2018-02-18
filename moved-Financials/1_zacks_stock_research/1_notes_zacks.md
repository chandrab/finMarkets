####  All Zacks Research related : scraping etc..

#### Coding Part : Big Theams, what to Extract from each of : Zacks, Finviz, yahoo Finance, Pandas
```
0/ Stock Symbol list: 
  - get this CSV file and [parse with Pandas into Dataframe](http://www.nasdaq.com/screening/company-list.aspx)
  - filelds are : IPO year, Market cap, Industry , sector 
  - based on IPO year, from get 1/1/YYY to 12/31/YYYY , using Pandas python take first 10 rows, gives IPO DATE

0.2/ Human Wisdom Collooraton
  - Widsdom colloboration is very important in the STOCK Analysis
  - include smart people like  'Subbu' comment on 8/4/17 on FIT https://finance.yahoo.com/quote/FIT/community?p=FIT ( show our website & ask for colloboration )
  - include Subbarami reddy , another widsom ..
  
1/ Zacks :
  - There is no Github repo for Zacks, so we need to do Python , BS Lib coding.
  - next Qtr Reporting DATE , EPS estimates, surprises % in the past
  - industry comparision : next 5 Yr growth Company, Indusry ( also past 5 years)
  - For historial prices, it seems we have simple working Pandas code
  - for IPO date: from EPS historical Last Record, we get 1 st Qtr date, use it minus 4 months DATE with Pandas to get FIRST Trading Date

2/ Finviz: 
  - get Analyst upgrade/downgrade DATE and target prices
  - Charts jpgeg, extract image URL and display it , no storage
 
3/ Yahoo finance
  - use that yahoo-finance Pyton Lib : all API methods to get all Data, for historical data use Pandas
  - for 1 Yr Target price LOW, AVG, HIGH : find JOSN url which down loades and extract THOSE .
  
4/ How IPO priced moved over 1 yr
  Thesis : every stock with touch IPO base price with in a year
  - get ALL Nasdaq stock symbols 
  - for each Symbol find IPO Date using Zacks EPS page
  - based on First EPS date , do minus 4 months with Pandas query to get first TRADE DATE .
  - then Run the THESIS, how long it TOOK to touch IPO file for : FB, FIT, GPRO , SNAP , RDFN , ALIBABA, ATlasian , Twillo etc..
  
5/ We need to find Correlations for Earning shootup/down
  - Get [Options quotes using Pandas](http://pandas-datareader.readthedocs.io/en/latest/remote_data.html#yahoo-finance-quotes), we can use this to get prices for next 1 Week  LONG/SHORT of SAME Strike 
  - case in point , on 8/3/17 FIT reported good resulted stock up +15% , on 8/4/17  GPRO reported with Stock up +20%
  - so we need to find is there any correlation in the past 4 quarters, with Earning for Fit, GPro ..
  - 
  - on 7/31/17 Morgan stanly has Postitive init for Both  FIT and GPRO ( news from Finviz ) --> we need to send  Alerts to Phones when News comes out
```
______________________________________________________________________________________________________________

1/ Earling Data : Quarterly upto 10 years, [with DATES (before/after close), EPS estimate/actual/suprise](https://www.zacks.com/stock/research/GPRO/earnings-announcements) <br>
1.2/ EPS Estimate [Revisions from Analysts](https://www.zacks.com/stock/research/GPRO/earnings-announcements) <br>
1.3/ [12 Mon EPS Vs. Stock Price](https://www.zacks.com/stock/chart/GPRO/eps) for GPRO , for [Adobe](https://www.zacks.com/stock/chart/adbe/eps) - If you can gestimate (based on EPS forecasts) EPS 2 to 3 Quarters ahaed, you catch big gains as seen in Adobe case .

2/ [Income Statements](https://www.zacks.com/stock/quote/GPRO/income-statement) <br>
2.2/ [Balance Sheet](https://www.zacks.com/stock/quote/GPRO/balance-sheet) <br>
2.3/ [industry comparision](https://www.zacks.com/stock/research/EBAY/industry-comparison) - see Growth Rates for EBAY : next 5 years 8.80 Vs.	18.50	<br>


