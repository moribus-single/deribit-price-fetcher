import asyncio
from aiohttp import ClientSession
import json
import time

from database.db_utils import *
from constants import Constants


async def get_index_price(ticker):
    url = Constants.DeribitApi.GET_PRICE_ENDPOINT
    params = {
        'index_name': f'{ticker}_usd'
    }

    async with ClientSession() as session:
        async with session.get(url=url, params=params) as response:
            data = await response.text()
            json_data = json.loads(data)

            return json_data['result']['index_price']


async def main():
    btc = 'btc'
    eth = 'eth'

    # connect to the database
    conn = await create_db_pool()

    # create table if it's not exist
    await create_index_table(conn)

    while True:
        # gather results
        results = await asyncio.gather(
            get_index_price(btc),
            get_index_price(eth)
        )

        # create Index objects
        btc_index = Index(id=None, name=btc, price=results[0], time=time.time())
        eth_index = Index(id=None, name=eth, price=results[1], time=time.time())

        # insert index data
        await insert_index_data(conn, btc_index)
        await insert_index_data(conn, eth_index)

        print(f"BTC: {results[0]}")
        print(f"ETH: {results[1]}")

        await asyncio.sleep(Constants.ClientParameters.TIME_SLEEP)


if __name__ == "__main__":
    asyncio.run(main())
