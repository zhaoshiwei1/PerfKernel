import asyncio
from threading import Thread
import aiohttp


async def fetch(url):
    while True:
        async with aiohttp.request('GET', url) as resp:
            json = await resp.text()
            print(json)


async def lead(loop):
    i = 0
    while True:
        asyncio.run_coroutine_threadsafe(fetch('http://127.0.0.1:8080/calculate?a=1&b={}'.format(i)), loop)
        i += 1
        await asyncio.sleep(1)


async def welcome():
    while True:
        print("Welcome to slave factory!")
        await asyncio.sleep(1)


def front(loop):
    asyncio.run_coroutine_threadsafe(welcome(), loop)
    loop.run_forever()


front_loop = asyncio.new_event_loop()
front_thread = Thread(target=front, args=(front_loop, ))
front_thread.start()

slave_loop = asyncio.new_event_loop()
slave_loop.run_until_complete(lead(slave_loop))
