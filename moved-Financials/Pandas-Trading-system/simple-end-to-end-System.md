#### Simple End-to-End  Trading System Python/Pandas code

0. This end-to-end Trading system has 3 parts: I) simple Portifolio Buy/Sell management II) Pandas TA Lib III) Deep Learning/RL part

***II . for technical indicator calculations use this 'Pandas TA Lib'***
+ Sample [Test program calling Pandas TA LIb](https://github.com/femtotrader/pandas_talib/blob/master/samples/main.py)
+ Actual [indicators code in Pandas ](https://github.com/femtotrader/pandas_talib/blob/master/pandas_talib/__init__.py) . This is very elegant code, each TA function return the Data frame with TA Column as  added COLUMN
+  Technical Indicators group of 11: [These 11 shows one of BUY, SELL, NEUTRAL signal ](https://www.investing.com/currencies/btc-usd-technical). Find how they determine Buy,Sell, Neutral based on TA Indicator values, that is what is the Cut of to say BUY vs. Sell for each indicator . asr: I should get this on internet ...

***III .Deep Learning/RL part***
 + Applying TA Indicators and give it as Classification/Regression problem to Tensor flow code ( see DL-M-AI dir TF code next day UP, DOWN or FLAT day program . Also saved/forked in our Kagale account )
 + using 'Reinforment Learning' RL part, where RL agent makes decision when to BUY and SELL based on Indicators etc.. ( see DL-ML-AI dir Reinforcement base game program )
 + As shown in RL game program, it is easy to have one variable . what happens when you have different variables in each box of the Game. Tie those each values to each of Technical Indicator . asr: talk to Kaggle people and others ..
 + 
 + we may use above 11 Technical indicators final resutlt that is BUY, SELL, Neutral +1oga, -1, 0 as 11 different Features to Tensor flow program in addition to orginal 11 indicators , so total 22 features
 + see how prediction accuracy cahnges with fist 11 then with  Buy/sell/Neutral added total 22 .

 
 ***I . Pandas based simple end to end system***
+ 1/ An Introduction to [Stock Market Data Analysis with Python](https://github.com/datascience-course/2016-datascience-labs/blob/master/lab6-time-series/lab6-time-series.ipynb
)

+ 1.2 same explained in these two blog posts, part 1:  https://ntguardian.wordpress.com/2016/09/19/introduction-stock-market-data-python-1/
 part 2: https://ntguardian.wordpress.com/2016/09/26/introduction-stock-market-data-python-2/
 
 + 2/ Analyzing [Stock Risk](https://nextjournal.com/hisham/stock-market) - has some correlatoin code 
 
 +  We will refer to the sign of this difference as the regime; that is, if the fast moving average is above the slow moving average, this is a bullish regime (the bulls rule), and a bearish regime (the bears rule) holds when the fast moving average is below the slow moving average. I identify regimes with the following code.
In [28]:
+ asr : Nice  PANDAS and NUMPY interchange here, works well to gether . 
 ```
# np.where() is a vectorized if-else function, where a condition is checked for each component of a vector, 
and the first argument passed is used when the condition holds, and the other passed if it does not
apple["Regime"] = np.where(apple['20d-50d'] > 0, 1, 0)

# We have 1's for bullish regimes and 0's for everything else. Below I replace bearish regimes's values with -1, and 
to maintain the rest of the vector, the second argument is apple["Regime"]
apple["Regime"] = np.where(apple['20d-50d'] < 0, -1, apple["Regime"])
apple.loc['2016-01-01':'2016-08-07',"Regime"].plot(ylim = (-2,2)).axhline(y = 0, color = "black", lw = 2)
```
+ It's simple to obtain signals. Let $r_t$ indicate the regime at time $t$, and $s_t$ the signal at time $t$. Then:
$$\begin{equation*}
s_t = \text{sign}(r_t - r_{t - 1})
\end{equation*}$$
$s_t \in \{-1, 0, 1\}$, with $-1$ indicating "sell", $1$ indicating "buy", and $0$ no action. We can obtain signals like so:
In [32]:
```
# To ensure that all trades close out, I temporarily change the regime of the last row to 0
regime_orig = apple.ix[-1, "Regime"]
apple.ix[-1, "Regime"] = 0
apple["Signal"] = np.sign(apple["Regime"] - apple["Regime"].shift(1))
# Restore original regime data
apple.ix[-1, "Regime"] = regime_orig
apple.tail()
````
+ 

