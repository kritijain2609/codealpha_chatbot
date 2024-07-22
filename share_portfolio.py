import requests
import pandas as pd
from prettytable import PrettyTable

API_KEY = 'CO6IH4QDIDUQDZ5L'
BASE_URL = 'https://www.alphavantage.co/query'

portfolio = {}

def get_stock_price(symbol):
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': '1min',
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()
    
    try:
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        last_price = data['Time Series (1min)'][last_refreshed]['4. close']
        return float(last_price)
    except KeyError:
        return None

def add_stock(symbol, shares):
    price = get_stock_price(symbol)
    if price:
        portfolio[symbol] = {
            'shares': shares,
            'price': price
        }
        print(f"Added {shares} shares of {symbol} at ${price:.2f} each.")
    else:
        print(f"Failed to fetch price for {symbol}.")

def remove_stock(symbol):
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"{symbol} not found in portfolio.")

def display_portfolio():
    table = PrettyTable()
    table.field_names = ["Symbol", "Shares", "Current Price", "Total Value"]
    total_value = 0

    for symbol, details in portfolio.items():
        current_price = get_stock_price(symbol)
        if current_price:
            total_value_stock = current_price * details['shares']
            total_value += total_value_stock
            table.add_row([symbol, details['shares'], f"${current_price:.2f}", f"${total_value_stock:.2f}"])

    print(table)
    print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == '3':
            display_portfolio()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
