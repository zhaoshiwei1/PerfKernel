import aiohttp
import asyncio
#
#
# async def main():
#     async with aiohttp.request('GET', 'http://www.baidu.com') as resp:
#         json = await resp.text()
#         print(json)
#
# loop = asyncio.new_event_loop()
# loop.run_until_complete(main())


# async def main():
#     tasks = []
#     [tasks.append(fetch('http://127.0.0.1:8080/calculate?a=1&b={}'.format(i))) for i in range(10)]
#     await asyncio.wait(tasks)
#
#
# async def fetch(url):
#     async with aiohttp.request('GET', url) as resp:
#         json = await resp.text()
#         print(json)
#
# loop = asyncio.new_event_loop()
# loop.run_until_complete(main())

async def fetch(url, session):
    async with session.get(url) as resp:
        result = await resp.text()
        print(result)


async def rate_control(sem, url, session):
    async with sem:
        await fetch(url, session)


async def main(concurrency):
    sem = asyncio.Semaphore(concurrency)
    async with aiohttp.ClientSession() as session:
        tasks = []
        [tasks.append(rate_control(sem, 'http://127.0.0.1:8080/calculate?a=1&b={}'.format(i), session)) for i in range(10)]
        await asyncio.wait(tasks)

loop = asyncio.new_event_loop()
loop.run_until_complete(main(concurrency=2))
