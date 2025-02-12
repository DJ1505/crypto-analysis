import json
import pandas as pd
import os

def save_to_excel():
   # Try to load our crypto data from JSON
   try:
       with open("crypto_data.json", "r") as f:
           data = json.load(f)
   except FileNotFoundError:
       print("Error: crypto_data.json not found - run fetch_data.py first!")
       return

   # Format the data for Excel
   excel_data = []
   for coin in data:
       excel_data.append({
           "Name": coin["name"],
           "Symbol": coin["symbol"].upper(),
           "Current Price (USD)": coin["current_price"],
           "Market Cap (USD)": coin["market_cap"],
           "24h Trading Volume": coin["total_volume"],
           "24h Price Change (%)": coin["price_change_percentage_24h"]
       })

   # Create DataFrame and set output path
   df = pd.DataFrame(excel_data)
   excel_path = os.path.join(os.getcwd(), "crypto_data.xlsx")

   # Save to Excel file
   try:
       df.to_excel(excel_path, index=False, engine="openpyxl")
       print(f"Successfully saved to: {excel_path}")
   except Exception as e:
       print(f"Failed to save Excel file: {e}")

if __name__ == "__main__":
   save_to_excel()