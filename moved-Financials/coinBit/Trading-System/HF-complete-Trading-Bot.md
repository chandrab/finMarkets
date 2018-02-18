
1/ https://github.com/gcarq/freqtrade
- Simple High Frequency Trading Bot for crypto currencies
- Simple High frequency trading bot for crypto currencies designed to support multi exchanges and be controlled via Telegram.
- 

**2/ Features** : uses TA-Lib https://github.com/mrjbq7/ta-lib
```
 Based on Python 3.6+: For botting on any operating system - Windows, macOS and Linux
 Persistence: Persistence is achieved through sqlite
 Dry-run: Run the bot without playing money.
 Backtesting: Run a simulation of your buy/sell strategy.
 Strategy Optimization: Optimize your buy/sell strategy parameters with Hyperopts.
 Whitelist crypto-currencies: Select which crypto-currency you want to trade.
 Blacklist crypto-currencies: Select which crypto-currency you want to avoid.
 Manageable via Telegram: Manage the bot with Telegram
 Display profit/loss in fiat: Display your profit/loss in 33 fiat.
 Daily summary of profit/loss: Provide a daily summary of your profit/loss.
 Performance status report: Provide a performance status of your current trades.
 
 ----Exchange supported----
 Bittrex
 Binance
 Others
 ```
 
 
**3/ Requirements**
```
Min hardware required
To run this bot we recommend you a cloud instance with a minimum of:

Minimal (advised) system requirements: 2GB RAM, 1GB disk space, 2vCPU
Software requirements
Python 3.6.x
pip
git
TA-Lib
virtualenv (Recommended)
Docker (Recommended)
```

**4/ user Forum :** [Slack Channel](https://highfrequencybot.slack.com/join/shared_invite/enQtMjQ5NTM0OTYzMzY3LWMxYzE3M2MxNDdjMGM3ZTYwNzFjMGIwZGRjNTc3ZGU3MGE3NzdmZGMwNmU3NDM5ZTNmM2Y3NjRiNzk4NmM4OGE)


**5/ Back Testing command**
```
Backtesting also uses the config specified via -c/--config.

usage: freqtrade backtesting [-h] [-l] [-i INT] [--realistic-simulation]
                             [-r]

optional arguments:
  -h, --help            show this help message and exit
  -l, --live            using live data
  -i INT, --ticker-interval INT
                        specify ticker interval in minutes (default: 5)
  --realistic-simulation
                        uses max_open_trades from config to simulate real
                        world limitations
  -r, --refresh-pairs-cached
                        refresh the pairs files in tests/testdata with 
                        the latest data from Bittrex. Use it if you want
                        to run your backtesting with up-to-date data.
 ```
