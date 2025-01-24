import asyncio

async def task():
  print('task is running')
  await asyncio.sleep(1)
  print('task is finished')
  

async def task2():
  print('task2 is running')
  await asyncio.sleep(1)
  print('task2 is finished')
  

async def main():
  await asyncio.gather(task(), task2())
  
asyncio.run(main())


async def fetch_data(i):
  print(f'fetching data {i}')
  await asyncio.sleep(i)
  print(f'data fetched {i}')
  return {'data': f'some data {i}'}

async def main1():
  tasks = [asyncio.create_task(fetch_data(i)) for i in range(3)]
  results = await asyncio.gather(*tasks)
  print(f'results: {results}')

asyncio.run(main1())

