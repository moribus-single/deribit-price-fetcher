from datetime import timedelta

from fastapi import FastAPI

from database.db_utils import *

app = FastAPI()


@app.get("/get_ticker_prices/")
async def get_ticker_prices(ticker: str):
    conn = await create_db_pool()
    return await select_index_data_by_ticker(conn, ticker)


@app.get("/get_last_price/")
async def get_last_price(ticker: str):
    conn = await create_db_pool()
    result = await select_index_last_data_by_ticker(conn, ticker)
    return result[0]['price']


@app.get("/get_price_by_date/")
async def get_price_by_date(ticker: str, date: str):
    # converting date to start timestamp and end timestamp
    start_timestamp = datetime.strptime(date, '%Y-%m-%d')
    end_timestamp = datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)

    conn = await create_db_pool()
    result = await select_index_price_by_date(conn, ticker, start_timestamp.timestamp(), end_timestamp.timestamp())
    return [item['price'] for item in result]



