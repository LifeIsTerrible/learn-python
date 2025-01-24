import aiohttp
import asyncio
import sys

sys.stdout.reconfigure(encoding='utf-8')

async def fetch(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      return await response.json()
  
async def main():
  urls = ['https://api.github.com', 'https://api.github.com/events', 'https://api.github.com/repos/aio-libs/aiohttp']
  tasks = [fetch(url) for url in urls]
  results = await asyncio.gather(*tasks)
  print(f'results: {results}')
  
asyncio.run(main())

