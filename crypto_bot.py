import telebot
import yfinance as yf
from datetime import datetime

# Initialize the Telegram bot with your API token
bot = telebot.TeleBot('TOKEN_HERE')

# Define a list of cryptocurrencies to fetch rates for
cryptos = ['BTC', 'ETH', 'DOGE', 'LTC', 'XRP']

# Define a function to fetch the crypto rate from the Yahoo Finance API
def get_crypto_rate(crypto):
    ticker = yf.Ticker(f'{crypto}-USD')
    rate = ticker.info['regularMarketPrice']
    return rate

# Define a function to handle the "/start" command
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Send a message to the user with the available cryptocurrencies to choose from
    bot.send_message(message.chat.id, f'Choose cryptocurrencies:\n{", ".join(cryptos)}')

# Define a function to handle the user's message
@bot.message_handler(func=lambda message: message.text.upper() in cryptos)
def handle_message(message):
    # Fetch the rate for the chosen cryptocurrency and send it to the user
    crypto = message.text.upper()
    rate = get_crypto_rate(crypto)
    message_text = f'{crypto}: ${rate:.2f}\nLast updated: {datetime.now()}'
    bot.send_message(message.chat.id, message_text)

# Start the Telegram bot
bot.polling()


