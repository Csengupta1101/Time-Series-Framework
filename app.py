import os
import yfinance as yf
import pandas as pd

def fetch_stock_data_and_save_to_excel(ticker, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Fetch the stock data using yfinance
    start_date = pd.Timestamp.today() - pd.DateOffset(years=5)
    end_date = pd.Timestamp.today()
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    # Save the stock data to an Excel file
    output_file = os.path.join(output_folder, f"{ticker}_stock_data.xlsx")
    stock_data.to_excel(output_file)

if __name__ == "__main__":
    ticker_symbol = "EXIDEIND.NS"  # Ticker symbol for Tata Power on the NSE
    data_folder = "data"
    fetch_stock_data_and_save_to_excel(ticker_symbol, data_folder)
