import asyncio
from threading import Thread


async def work(i):
    while True:
        print("I'm task: {}".format(i))
        await asyncio.sleep(1)


async def lead(loop):
    i = 0
    while True:
        asyncio.run_coroutine_threadsafe(work(i), loop)
        await asyncio.sleep(1)
        i += 1


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
