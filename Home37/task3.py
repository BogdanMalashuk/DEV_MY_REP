import asyncio
import random
import time

import requests


async def fetch_data(url):
    waiting_time = random.randint(1, 3)
    await asyncio.sleep(waiting_time)
    print(f'successfully, waiting time: {waiting_time}')


async def main():
    url1 = "https://www.youtube.com/?app=desktop&hl=ru"
    url2 = "https://www.facebook.com/?locale=ru_RU"
    url3 = "https://teachmeskills.by/"

    start_time = time.time()
    await asyncio.gather(fetch_data(url1), fetch_data(url2), fetch_data(url3))
    end_time = time.time()

    print(f'time: {end_time - start_time}')


asyncio.run(main())
