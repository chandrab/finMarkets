

An analysis on price targets: [blog post](http://blog.ayoungprogrammer.com/2017/05/stocks-with-outperform-ratings-beats-market.html/) , [github coe](https://github.com/ayoungprogrammer/price-targets) <br>

Scrapy [vs. BeautifulSoup  compared](https://blog.michaelyin.info/2017/08/10/scrapy-tutorial-1-scrapy-vs-beautiful-soup/) - in the above Scrapy was used .

_________
[corrlelations](https://stackoverflow.com/questions/19428029/how-to-get-correlation-of-two-vectors-in-python)
```
from scipy.stats.stats import pearsonr   
a = [1,4,6]
b = [1,2,3]   
print pearsonr(a,b)
This gives

(0.99339926779878274, 0.073186395040328034)
You can also use numpy.corrcoef:

import numpy
print numpy.corrcoef(a,b)
This gives:

[[ 1.          0.99339927]
 [ 0.99339927  1.        ]]
print pearsonr(a,b)
```

[Pandas Seaborn correlation](https://stackoverflow.com/questions/29432629/correlation-matrix-using-pandas)
```
You can observe the relation between features either by drawing a heat map from seaborn or scatter matrix from pandas.

Scatter Matrix:

pd.scatter_matrix(dataframe, alpha = 0.3, figsize = (14,8), diagonal = 'kde');
If you want to visualize each feature's skewness as well - use seaborn pairplots.

sns.pairplot(dataframe)
Sns Heatmap:

import seaborn as sns

f, ax = pl.subplots(figsize=(10, 8))
corr = dataframe.corr()
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
            square=True, ax=ax)
The output will be a correlation map of the features. i.e. see the below example.

```
__________________________________
#### Pandas [Tutorial](https://www.dataquest.io/blog/pandas-python-tutorial/)
```
frame = pd.DataFrame(
    [
        [1,2],
        ["Boris Yeltsin", "Mikhail Gorbachev"]
    ],
    index=["row1", "row2"],
    columns=["column1", "column2"]
)


        column1	         column2
row1	  1	               2
row2 	  Boris Yeltsin	   Mikhail Gorbachev

```
Demystifying Pandas 
[Using iloc, loc, to select rows and columns in DataFrames](
https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/) <br>

[Indexing and Selecting Data¶](http://pandas.pydata.org/pandas-docs/stable/indexing.html#deprecate_ix) -- Official Pandas Docs <br>
[10 minute Pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)
```
In [14]: df.head()
Out[14]: 
                   A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-05 -0.424972  0.567020  0.276232 -1.087401

Display the index, columns, and the underlying numpy data
----------------------------------------------------
In [16]: df.index
Out[16]: 
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

In [17]: df.columns
Out[17]: Index(['A', 'B', 'C', 'D'], dtype='object')

In [18]: df.values
Out[18]: 
array([[ 0.4691, -0.2829, -1.5091, -1.1356],
       [ 1.2121, -0.1732,  0.1192, -1.0442],
       [-0.8618, -2.1046, -0.4949,  1.0718],
       [ 0.7216, -0.7068, -1.0396,  0.2719],
       [-0.425 ,  0.567 ,  0.2762, -1.0874],
       [-0.6737,  0.1136, -1.4784,  0.525 ]])
       
       

In [22]: df.sort_values(by='B')
Out[22]: 
                   A         B         C         D
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804
2013-01-04  0.721555 -0.706771 -1.039575  0.271860
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-06 -0.673690  0.113648 -1.478427  0.524988
2013-01-05 -0.424972  0.567020  0.276232 -1.087401


Selecting a single column, which yields a Series, equivalent to df.A

In [23]: df['A']
Out[23]: 
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849
2013-01-04    0.721555

Selecting a single column, which yields a Series, equivalent to df.A

In [23]: df['A']
Out[23]: 
2013-01-01    0.469112
2013-01-02    1.212112
2013-01-03   -0.861849

In [24]: df[0:3]   # slice ROWS

             A         B         C         D
2013-01-01  0.469112 -0.282863 -1.509059 -1.135632
2013-01-02  1.212112 -0.173215  0.119209 -1.044236
2013-01-03 -0.861849 -2.104569 -0.494929  1.071804


df.loc[dates[0]]

Selecting on a multi-axis by label
In [27]: df.loc[:,['A','B']]

Showing label slicing, both endpoints are included
In [28]: df.loc['20130102':'20130104',['A','B']]

Reduction in the dimensions of the returned object
In [29]: df.loc['20130102',['A','B']]

```
