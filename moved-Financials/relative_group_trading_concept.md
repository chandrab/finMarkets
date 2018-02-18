#### Relative Group Trading Concept ( similar to Pair Trading ) 
Here is [Paypal](https://finance.yahoo.com/quote/PYPL/?p=PYPL)
```
Yahoo finance analyst avg. Target price ( one year Target price ) of all followed analysts for a given stock ( 20 to 40 analysts depending on the Comapnay)
 - This Target price has 3 values 
    Low target price ( lowest of all analysts )
    Avagarge Target price
    High Target price
    
 - Now you have a 'Currnt price' of a Stock, that is Today's stock price
 - if the current Stock price is below 'avg. Target price'  stock is trading in Discount to Target Price
 - current Stock Price > avg. Target price --> Stock price is in Premium to Target Price
 
 Here is some DATA
 
 Company  currnet Price   Target Price   difference
 --------  -------------  -------------- -----------
 PAPL       $58               $55        -10% ( potential upside if positive or downside if negative )
 GOOG       $955              $1042
 AAPL       $149              $159
 AMZN       $1000             $1120
 
 all Last 3 stocks are trading +10 discount to avg. Target price, where as Paypal -10% Premium to avg. target price 
 
 so if you do a Pair Trade of  " PYPL Short/ (GOOG + AMZN+ AAPL) Long " there is a 20% differential which can be corrected.

```
