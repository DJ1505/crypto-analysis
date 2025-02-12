import requests
import json

def fetch_crypto_data():
    # CoinGecko API endpoint for top 50 coins by market cap
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }

    # Grabing  data from CoinGecko
    response = requests.get(url, params=params)
    
    # If we get a good response, save it
    if response.status_code == 200:
        crypto_data = response.json()
        
        # Dump it into a JSON file
        with open("crypto_data.json", "w") as f:
            json.dump(crypto_data, f, indent=4)
        
        print("[SUCCESS] Data saved to crypto_data.json")
    else:
        print(f"[ERROR] API call failed with status code: {response.status_code}")

# Only run this if we're running the file directly
if __name__ == "__main__":
     fetch_crypto_data()