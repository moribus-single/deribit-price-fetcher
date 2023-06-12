import asyncpg
import os

from string import Template
from dotenv_vault import load_dotenv
from datetime import datetime

from .dataclass import Index

load_dotenv()


async def create_db_pool():
    return await asyncpg.create_pool(
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )


async def create_index_table(conn):
    query = "CREATE TABLE IF NOT EXISTS index (" \
            "id SERIAL PRIMARY KEY, " \
            "name VARCHAR(10) NOT NULL, " \
            "price FLOAT NOT NULL, " \
            "time FLOAT NOT NULL" \
            ")"

    await conn.execute(query)


async def insert_index_data(conn, data: Index):
    query = Template("INSERT INTO index (name, price, time) VALUES ('$name', $price, $time)")

    await conn.execute(
        query.substitute(name=data.name, price=data.price, time=data.time)
    )


async def select_index_data_by_ticker(conn, ticker):
    query = Template("SELECT id, name, price, \"time\" FROM index WHERE name='$ticker'")
    return await conn.fetch(query.substitute(ticker=ticker))


async def select_index_last_data_by_ticker(conn, ticker):
    query = Template("SELECT price FROM index WHERE name='$ticker' ORDER BY \"time\" DESC")
    return await conn.fetch(query.substitute(ticker=ticker))


async def select_index_price_by_date(conn, ticker, start_timestamp, end_timestamp):
    query = Template("SELECT price FROM index WHERE "
                     "name = '$ticker' AND \"time\" >= $start_timestamp AND \"time\" < $end_timestamp")
    return await conn.fetch(
        query.substitute(
            ticker=ticker,
            start_timestamp=start_timestamp,
            end_timestamp=end_timestamp
        )
    )


async def drop_database(conn, db_name):
    query = Template("DROP DATABASE $db_name")
    conn.execute(
        query.substitute(db_name=db_name)
    )
