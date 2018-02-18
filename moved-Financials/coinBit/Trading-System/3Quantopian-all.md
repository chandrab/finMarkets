#### Every thing what Quantopian offers

[FAQ Page](https://www.quantopian.com/faq#get-started) Is Quantopian free?
- Yes! Quantopian's platform and data, including price, volume, and corporate fundamentals data for all **8000+ US equities and futures from 2002** to present is free for everyone to use
- We currently provide minute-level price, volume, and fundamental data of all US stocks from January 2002 through the previous trading day for backtesting. The previous day's data is uploaded every night. We also have [price and volume data for 72 US futures](https://www.quantopian.com/help#available-futures), going as far back as January 2002.

- Minute-level bar data consists of the high, low, open, close, and volume for each minute that a stock or futures contract is traded.
- **Fundamental data from Morningstar** is available, free of charge, for over 5,000 companies. This data set includes over 600 metrics for use in Quantopian's backtester, as a point-in-time database.

What **libraries does Quantopian support?**
- Only specific, whitelisted Python modules can be imported. If you need a module that isn't on this list, please let us know.
- below is the **list of libraries** . They support good ones such as **Pandas, talib, numpy, zipline, scipy, sklearn, statsmodels**
- bisect cmath collections copy cvxopt datetime functools heapq itertools math numpy operator pandas pytz Queue random re scipy sklearn statsmodels time talib zipline zlib

- If your heart is set on using your own development environment, take a look at Zipline. **Zipline is our backtester, and we have open sourced the code**. If you want, **you can connect Zipline to a data source ( your own Data soruce)** and use your own development environment.

### [Quantopian overview](https://www.quantopian.com/help) -- provide summary of all FEATURES, see below

####  1. Pipeline
- Many algorithms depend on calculations that follow a specific pattern:
- Every day, for some set of data sources, fetch the last N days’ worth of data for a large number of assets and apply a reduction function to produce a single value per asset.
- This kind of calculation is called **a cross-sectional trailing-window computation.**
- eaxmple : We then specify that we want to filter down each day to just stocks with a 10-day average price of $5.00 or less.
```
from quantopian.algorithm import attach_pipeline, pipeline_output
from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import SimpleMovingAverage

def initialize(context):

    # Create and attach an empty Pipeline.
    pipe = Pipeline()
    pipe = attach_pipeline(pipe, name='my_pipeline')

    # Construct Factors.
    sma_10 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=10)
    sma_30 = SimpleMovingAverage(inputs=[USEquityPricing.close], window_length=30)

    # Construct a Filter.
    prices_under_5 = (sma_10 < 5)

    # Register outputs.
    pipe.add(sma_10, 'sma_10')
    pipe.add(sma_30, 'sma_30')

    # Remove rows for which the Filter returns False.
    pipe.set_screen(prices_under_5)

def before_trading_start(context, data):
    # Access results using the name passed to `attach_pipeline`.
    results = pipeline_output('my_pipeline')
    print results.head(5)

    # Store pipeline results for use by the rest of the algorithm.
    context.pipeline_results = results
```
above program output is as follows
```
index	             sma_10	   sma_30
Equity(21 [AAME])	2.012222	1.964269
Equity(37 [ABCW])	1.226000	1.131233
Equity(58 [SERV])	2.283000	2.309255
Equity(117 [AEY])	3.150200	3.333067
Equity(225 [AHPI])	4.286000	4.228846
```

#### 2. Custom Factors
-  quantopian.pipeline.CustomFactor and implement a compute method whose signature is:
```
def compute(self, today, assets, out, *inputs):
```
```
class MyFactor(CustomFactor):
    def compute(self, today, asset_ids, out, values):
       out[:] = do_something_with_values(values)

def initialize(context):
    p = attach_pipeline(Pipeline(), 'my_pipeline')
    my_factor = MyFactor(inputs=[USEquityPricing.close], window_length=5)
    p.add(my_factor, 'my_factor')
```
####  Default Inputs
- If values are **not passed for window_length or inputs**, the CustomFactor constructor will try to **fall back to class-level attributes with the same names**. This means that we can implement a VWAP-like CustomFactor by defining an inputs list as a class level attribute.
```
import numpy as np

class PriceRange(CustomFactor):
    """
    Computes the difference between the highest high and the lowest
    low of each over an arbitrary input range.
    """
    inputs = [USEquityPricing.high, USEquityPricing.low]

    def compute(self, today, assets, out, highs, lows):
        out[:] = np.nanmax(highs, axis=0) - np.nanmin(lows, axis=0)


# We'll automatically use high and low as inputs because we declared them as
# defaults for the class.
price_range_10 = PriceRange(window_length=10)
```

#### Masking Factors
-  When passed a mask, a CustomFactor will only compute values over stocks for which the Filter returns True. All other stocks for which the Filter returned False will be filled with missing values.
- Suppose we want to compute a factor over only the top 500 stocks by dollar volume. We can define a CustomFactor and Filter as follows:
```
from quantopian.algorithm import attach_pipeline
from quantopian.pipeline import CustomFactor, Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.factors import AverageDollarVolume

def do_something_expensive(some_input):
    # Not actually expensive. This is just an example.
    return 42

class MyFactor(CustomFactor):
    inputs = [USEquityPricing.close]
    window_length = 252

    def compute(self, today, assets, out, close):
        out[:] = do_something_expensive(close)

def initialize(context):
    pipeline = attach_pipeline(Pipeline(), 'my_pipeline')

    dollar_volume = AverageDollarVolume(window_length=30)
    high_dollar_volume = dollar_volume.top(500)

    # Pass our filter to our custom factor via the mask parameter.
    my_factor = MyFactor(mask=high_dollar_volume)
    pipeline.add(my_factor, 'my_factor')
```
#### For LOOP example
```
def initialize(context):
    # AA, AAPL, ALK
    context.securities = [sid(2), sid(24), sid(300)] 

def handle_data(context, data):
    # You can pass a string variable into record().
    # Here we record the price of all the securities in our list.
    for stock in context.securities:
      price = data.current(stock, 'price')
      record(stock, price)

    # You can also pass in a variable with a string value.
    # This records the high and low values for AAPL.
    fields = ['high', 'low']
    for field in fields:
      record(field, data.current(sid(24),field))
   
```   
