### steps [in running zipline](https://github.com/quantopian/zipline)

1. Just issued this commond from on home dir /users/pad.. ; it insalled all under some where probably conda ...
```
$ conda install -c Quantopian zipline
```

2. created zipline-asr dir and created file dma.py by [coping code]()
- registered with github login and got Quandl API key ( saved in dir ) and issued following command
```
$ QUANDL_API_KEY=<yourkey> zipline ingest -b quandl
$ zipline run -f dual_moving_average.py --start 2014-1-1 --end 2018-1-1 -o dma.pickle
```

3.  [Tutorial](http://www.zipline.io/beginner-tutorial.html)  and [data bundles](http://www.zipline.io/bundles.html)
