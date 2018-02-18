### Various Price Discovery Models

**0. Take aways & tools used:**
 - In support/resistance findig ml.py , HighCharts.com chart was used it worked, it is clean chart and have range ( D, Months etc..)
 - Let us try to use same Highcharts in our site too
 - also check the other Flask based Python for other web site building .

**1. Zacks Rank :** see separate file for this

**1. Facebook Prophet :**
 - Prediction Data [Stock Prices with Prophet](http://intelligentonlinetools.com/blog/2017/12/26/prediction-data-stock-price-prophet-report/)
 - shinyapp web page - [check various stocks prediciton](https://mydata.shinyapps.io/ShinyProphetV2/) ( confidence range) . Tried with Ebay,paypal  When Outside Range good for short/long with Options . Try for Crude oil CL data how it looks 
 - Stock market forecasting [with prophet](http://pythondata.com/stock-market-forecasting-with-prophet/) -- see confidence Bands in the post
 - sr: may be we can use PROPHET to fina SEASONLITY in CRUDE OIL CL,  BTC  prices on weekends, specific months JAN, FEB etc...
 - [Prohphet youtube](https://www.youtube.com/watch?v=95-HMzxsghY)
 
**2. Deep Learning LSTM , Keras :** 
- Machine Learning [Stock Prediction with LSTM and Keras](http://intelligentonlinetools.com/blog/2018/01/19/machine-learning-stock-prediction-lstm-keras/)
- [complete code page](http://intelligentonlinetools.com/blog/2018/01/20/machine-learning-stock-prediction-lstm-keras-python-source-code/)
- LSTM with 5, 60 and 1000 neurons.  more nuerons better accuracy
- The final LSTM was running with testing MSE 0.015 and accuracy 98.1%. This was obtained by changing number of neurons in LSTM.
- [LSTM video](https://www.youtube.com/watch?v=2np77NOdnwk)

**3. finding dynamic Support/Resistance level using Math MeanShift Stats models :** 
- sr: It worked when we tried, on a csv file data 
- [github](https://github.com/jonromero/forex_algotrading) - see ml.py file
- [ML in forex with SUP RES levels](http://jon.io/machine-beats-human-using-machine-learning-in-forex.html)
