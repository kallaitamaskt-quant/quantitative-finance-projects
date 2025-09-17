import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def get_stock_data(ticker, start_date, end_date):
    print(f"Downloading data for {ticker} from {start_date} to {end_date}...")
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        print(f"Error: No data found for ticker '{ticker}'. Please check the symbol.")
        return None
    print("Data download complete.")
    return data

if __name__ == "__main__":
    # parameters
    ticker_symbol = "TSLA"
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    # grab data
    stock_data = get_stock_data(ticker_symbol, start_date, end_date)

    if stock_data is not None:
        # calculate metrics
        stock_data["Daily Returns"] = stock_data["Close"].pct_change()
        stock_data["SMA50"] = stock_data["Close"].rolling(window=50).mean() # simple moving average over 50 days (short term)
        stock_data["SMA200"] = stock_data["Close"].rolling(window=200).mean() # simple moving average over 200 days (long term)

        print("\n--- Last 5 rows of data with calculated metrics: ---")
        print(stock_data.tail())

        # plot
        plt.figure(figsize=(12,6))
        plt.plot(stock_data["Close"], label="Close Price")
        plt.plot(stock_data["SMA50"], label="50-Day SMA")
        plt.plot(stock_data["SMA200"], label="200-Day SMA")
        plt.legend() # to show labels
        plt.show() # to open the chart window