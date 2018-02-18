
class EpsSurprise:

    def __init__(self, symbol):
        self.symbol = symbol
        f.df_eps_histotry = ""  # this is Pandas Dataframe


    def populate_eps_history(self ):
	# extract zacks eps data scrap for symbol

        	# dataframe fields: date, qtr_dt , eps_est, eps , surprise_perc, after_before
        	df = util.get_zacks_eps_history(this.symbol)  # have it in Util pkg
        	self.df_eps_histotry = df
        
        	for x in df:
        		price_change = get_price_updown() 
        		# set in dataFrame

    def eps_stats(self ):
	# extract zacks eps data scrap for symbol
        pass

    def get_price_updown(self ):
	# calc next day stock price up/down % change and add field price_chg
    
        	if time = 'after close':
        		dt_from, dt_to  = dt , dt+4
        	else:
        		dt_from, dt_to  = dt-1 , dt+3  # for 'before open'

    # http://www.learndatasci.com/python-finance-part-yahoo-finance-api-pandas-matplotlib/
    	df_quotes =  get_stock_quotes(this.symbol, dt_from, dt_to)
    
    	# index df  by date 
    price_change =  ( close[1] - close[0]) / close[0] ) * 100
    
    return price_change 

