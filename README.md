# CryptoBot

CryotoBot is a Telegram bot that shows live crypto rates from YahooFinance API and draws chatrs with choosen days.The bot can handle the following buttons and commands:

- **' /start '**: displays available commands
- A specific cryptocurrency symbol: displays the current price of that cryptocurrency and adds it to a MongoDB database
- **' All Cryptos '**: displays the current prices of all cryptocurrencies in **`cryptos`** list
- **' Support '**: displays contact information for technical support
- **' Calculator '**: initiates a calculator function that allows users to input an amount and cryptocurrency to get the value in USD
- **' Graph '** : initiates a function to generate a graph of a cryptocurrency's historical prices over a specified number of days

The bot also uses a MongoDB database to store information about each cryptocurrency's price and the time of the update.Overall, this code provides a useful set of functionalities for a cryptocurrency bot on Telegram


# Installation

To use CryptoBot, you will need to install python libraries from [requirements.txt
](requirements.txt)

