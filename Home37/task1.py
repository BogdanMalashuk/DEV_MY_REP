import asyncio
import time


async def download_data():
    await asyncio.sleep(3)
    print('Data was downloaded')


async def main():
    start_time = time.time()

    await download_data()
    await download_data()

    end_time = time.time()

    print(f'time: {end_time - start_time}')


asyncio.run(main())
