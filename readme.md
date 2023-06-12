# Deribit Price Fetcher


This is a project that fetches the prices of **ETH** and **BTC** from **Deribit API** and provides a small backend using 
**FastApi** and **PostgreSQL** for analyzing the retrieved data.

---

## Requirements

- Python 3.9
- PostgreSQL database
- FastApi

---

## Installation

1. Clone the repository <br>
`
    git clone git@github.com:moribus-single/deribit-price-fetcher.git
` 
2. Navigate to the project directory<br>
`
    cd deribit-price-fetcher
`
3. Install the dependencies using pip:<br>
`
    pip install -r requirements.txt
`
4. Setup PostgreSQL database and configure connection in `.env` according `.env.example` 
5. Start the client and fetch the data <br>
`
    python client.py
`
6. After fetching some data start backend server <br>
`
    uvicorn api:app --reload
`

---

## API endpoints

**/get_ticker_prices/** - получить все данные для конкретного тикера <br>
**/get_last_price/** - получить последнюю цену для конкретного тикера <br>
**/get_price_by_date/** - получить цену для конкретного тикера по дате. Формат даты ***YEAR-MONTH-DAY*** <br>
