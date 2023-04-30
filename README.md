# CryptoBot

CryptoBot is a Telegram bot that shows live crypto rates from YahooFinance API and draws charts with choosen days.The bot can handle the following buttons and commands:

- **' /start '**: displays available commands and buttons
- A specific cryptocurrency symbol: displays the current price of that cryptocurrency and adds it to a MongoDB database
- **' All Cryptos '**: displays the current prices of all cryptocurrencies in **`cryptos`** list
- **' Support '**: displays contact information for technical support
- **' Calculator '**: initiates a calculator function that allows users to input an amount and cryptocurrency to get the value in USD
- **' Graph '** : initiates a function to generate a graph of a cryptocurrency's historical prices over a specified number of days

The bot also uses a MongoDB database to store information about each cryptocurrency's price and the time of the update


# Installation

To use CryptoBot, you will need to install python libraries from [requirements.txt
](requirements.txt) using this command in terminal:

```bash
pip install -r requirements.txt
```
or

```bash
pip install pyTelegramBotAPI
pip install yfinance==0.2.14
pip install mplfinance
pip install bytesbufio
pip install pymongo
```

After you need to import all libraries and connect to your Mongodb database

```python
import telebot
from datetime import datetime, timedelta
import mplfinance as mpf
from io import BytesIO
import yfinance as yf
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("Your_mongodb_client_uri", server_api=ServerApi('1'))
```


# How to use

After cloning the repository and installing the required libraries, you can use CryptoBot by running the bot.py file:
```Bash
python bot.py
```

Overall, this code provides a useful set of functionalities for a cryptocurrency bot on Telegram
