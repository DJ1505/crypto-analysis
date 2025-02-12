Cryptocurrency Market Analysis Tool
📌 Overview
This project fetches live cryptocurrency data from the CoinGecko API, analyzes key metrics, and updates an Excel sheet every 5 minutes with real-time data.

🛠 Features
✔ Fetches live data for the top 50 cryptocurrencies
✔ Performs basic analysis (top 5 by market cap, average price, highest/lowest 24-hour change)
✔ Saves and updates data in an Excel sheet every 5 minutes
✔ Provides an analysis report summarizing key insights

📂 Project Structure
bash
Copy
Edit
📦 crypto-analysis  
│── 📂 data/                    # Stores generated Excel files  
│── 📂 scripts/                 # Python scripts for fetching & analysis  
│── ├── fetch_data.py           # Fetch live cryptocurrency data  
│── ├── analysis.py             # Perform analysis on fetched data  
│── ├── save_to_excel.py        # Save and update data in an Excel sheet  
│── ├── main.py                 # Run the entire pipeline  
│── 📜 requirements.txt         # List of required Python libraries  
│── 📜 README.md                # Project documentation  
│── 📜 Crypto_Analysis_Report.pdf # Final analysis report  
⚙ Installation & Setup
1️⃣ Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/crypto-analysis.git
cd crypto-analysis
2️⃣ Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows
3️⃣ Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Run the project:

bash
Copy
Edit
python main.py
📊 Data Analysis Insights
🔹 Top 5 Cryptocurrencies by Market Cap:

Bitcoin (BTC): $1,899,357,740,390.00
  Ethereum (ETH): $313,766,083,118.00
  Tether (USDT): $141,920,247,982.00
  XRP (XRP): $138,601,547,608.00
  Solana (SOL): $94,833,776,614.00


📁 Live Excel Data
The real-time Excel sheet updates every 5 minutes.
📌 Download link:  https://1drv.ms/x/c/e89fb6e6d0532474/EUHiDd78KeVBi2lU6ojw1ncB2C_jIZxdB9d5N8J6C3-f3g


📜 API Reference
CoinGecko API: https://www.coingecko.com/en/api
🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

📩 Contact
🔹 Author: Dhananjay Kumar Tyagi
🔹 Email: dhananjaykumartyagi@gmail.com
🔹 GitHub: https://github.com/DJ1505
