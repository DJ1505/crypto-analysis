import json

def analyze_crypto_data():
   # Load and check if our data file exists
   try:
       with open("crypto_data.json", "r") as f:
           data = json.load(f)
   except FileNotFoundError:
       print("Error: Can't find crypto_data.json - run fetch_data.py first!")
       return

   # Get top 5 coins by market cap
   top_5_market_cap = sorted(data, key=lambda x: x["market_cap"], reverse=True)[:5]

   # Calculate average price across all coins
   avg_price = sum(coin["current_price"] for coin in data) / len(data)

   # Find biggest gainers and losers in last 24h
   biggest_gain = max(data, key=lambda x: x["price_change_percentage_24h"])
   biggest_loss = min(data, key=lambda x: x["price_change_percentage_24h"])

   # Print out our analysis
   print("\nTop 5 Coins by Market Cap:")
   for coin in top_5_market_cap:
       market_cap_formatted = "${:,.2f}".format(coin['market_cap'])
       print(f"  {coin['name']} ({coin['symbol'].upper()}): {market_cap_formatted}")

   print(f"\nAverage Price (Top 50 Coins): ${avg_price:.2f}")
   
   print(f"\nBiggest 24h Changes:")
   print(f"Gainer: {biggest_gain['name']} ({biggest_gain['symbol'].upper()}) "
         f"up {biggest_gain['price_change_percentage_24h']:.2f}%")
   print(f"Loser: {biggest_loss['name']} ({biggest_loss['symbol'].upper()}) "
         f"down {biggest_loss['price_change_percentage_24h']:.2f}%")

if __name__ == "__main__":
   analyze_crypto_data()