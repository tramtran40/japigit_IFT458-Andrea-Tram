import sys
from alpha_vantage.timeseries import TimeSeries

API_KEY = 'P229J3T1EBKTN8A6'

def getStockdata(symbol):
    try:
        time_series = TimeSeries(key=API_KEY, output_format='pandas')
        data , meta_data= time_series.get_intraday(symbol=symbol, interval='1min')
        return str(data.tail(1).iloc[0]['4. close'])
    except:
        return "not found"

def main():
    output_File = open('japi.out', 'w')
    while 1:
        userInput = input("Enter a Stock Symbol or QUIT to quit: ").upper()
        if userInput != "QUIT":
            stockPrice = 'The current price of {} is {}\n'.format(userInput, getStockdata(userInput))
            print(stockPrice)
            output_File.write(stockPrice)
            print("Stock Quotes retrieved successfully!")
        else:
            sys.exit("\nQuit.")
main()
