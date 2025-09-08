import json

def analyze_crypto_data():
    """
    Reads crypto_data.json and performs a simple analysis:
    1. Finds the top 5 coins by market cap
    2. Calculates average price
    3. Identifies biggest gainer and loser in 24h
    """

    # Try to load the data file
    try:
        with open("crypto_data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Error: crypto_data.json not found. Please run fetch_data.py first.")
        return

    # Find the top 5 coins by market cap
    sorted_by_market_cap = sorted(data, key=lambda coin: coin["market_cap"], reverse=True)
    top_5_market_cap = sorted_by_market_cap[:5]

    # Calculate average price of all coins
    total_price = 0
    for coin in data:
        total_price += coin["current_price"]

    average_price = total_price / len(data)

    # Find the coin with the biggest gain in 24h
    biggest_gain = data[0]
    for coin in data:
        if coin["price_change_percentage_24h"] > biggest_gain["price_change_percentage_24h"]:
            biggest_gain = coin

    # Find the coin with the biggest loss in 24h
    biggest_loss = data[0]
    for coin in data:
        if coin["price_change_percentage_24h"] < biggest_loss["price_change_percentage_24h"]:
            biggest_loss = coin

    # Print the results
    print("\nTop 5 Coins by Market Cap:")
    for coin in top_5_market_cap:
        formatted_cap = "${:,.2f}".format(coin["market_cap"])
        print(f"{coin['name']} ({coin['symbol'].upper()}): {formatted_cap}")

    print(f"\nAverage Price (Top 50 Coins): ${average_price:.2f}")

    print("\nBiggest 24h Changes:")
    print(f"Gainer: {biggest_gain['name']} ({biggest_gain['symbol'].upper()}) "
          f"up {biggest_gain['price_change_percentage_24h']:.2f}%")
    print(f"Loser: {biggest_loss['name']} ({biggest_loss['symbol'].upper()}) "
          f"down {biggest_loss['price_change_percentage_24h']:.2f}%")

if __name__ == "__main__":
    analyze_crypto_data()
