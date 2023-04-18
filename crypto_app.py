import yfinance as yf
from matplotlib import pyplot as plt
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg


def get_crypto_data(symbol):
    crypto = yf.Ticker(symbol)
    data = crypto.history(period='1d')
    price = data['Close'][0]
    return data, price

class CryptoButtons(GridLayout):
    def __init__(self, **kwargs):
        super(CryptoButtons, self).__init__(**kwargs)
        self.cols = 3
        self.add_widget(Button(text='(BTC) Bitcoin', on_press=lambda x: self.show_crypto('BTC-USD')))

    def show_crypto(self, symbol):
        self.parent.display_crypto(symbol)

class CryptoDisplay(GridLayout):
    def __init__(self, **kwargs):
        super(CryptoDisplay, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Symbol'))
        self.add_widget(Label(text='Price'))
        self.symbol_label = Label(text='')
        self.price_label = Label(text='')
        self.add_widget(self.symbol_label)
        self.add_widget(self.price_label)

    def update_display(self, symbol):
        data, price = get_crypto_data(symbol)
        self.symbol_label.text = symbol
        self.price_label.text = str(price)
        self.parent.graph.update_graph(data)

class CryptoCalculator(GridLayout):
    def __init__(self, **kwargs):
        super(CryptoCalculator, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Amount of Crypto'))
        self.amount_input = TextInput(multiline=False)
        self.add_widget(self.amount_input)
        self.add_widget(Label(text='Total Value'))
        self.total_label = Label(text='')
        self.add_widget(self.total_label)
        self.calculate_button = Button(text='Calculate', on_press=self.calculate)
        self.add_widget(self.calculate_button)

    def calculate(self, instance):
        amount = float(self.amount_input.text)
        price = float(self.parent.display.price_label.text)
        total = amount * price
        self.total_label.text = str(total)

class CryptoGraph(FigureCanvasKivyAgg):
    def __init__(self, **kwargs):
        super(CryptoGraph, self).__init__(plt.figure(**kwargs))
        self.ax = self.figure.subplots()

    def update_graph(self, data):
        data['Close'].plot(ax=self.ax)
        self.draw()

class CryptoGrid(GridLayout):
    def __init__(self, **kwargs):
        super(CryptoGrid, self).__init__(**kwargs)
        self.cols = 1
        self.buttons = CryptoButtons()
        self.display = CryptoDisplay()
        self.calculator = CryptoCalculator()
        self.graph = CryptoGraph(figsize=(5, 3), dpi=100)
        self.add_widget(self.buttons)
        self.add_widget(self.display)
        self.add_widget(self.calculator)
        self.add_widget(self.graph)

    def display_crypto(self, symbol):
        self.display.update_display(symbol)
        self.calculator.amount_input.text = ''
        self.calculator.total_label.text = ''

class CryptoApp(App):
    def build(self):
        return CryptoGrid()

if __name__ == '__main__':
    CryptoApp().run()