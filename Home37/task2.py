import asyncio
import time


async def download_data():
    await asyncio.sleep(3)
    print('Data was downloaded')


async def main():
    task1 = asyncio.create_task(download_data())
    task2 = asyncio.create_task(download_data())

    start_time = time.time()

    await task1
    await task2

    end_time = time.time()

    print(f'time: {end_time - start_time}')


asyncio.run(main())
