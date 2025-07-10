import asyncio, random


async def fetch_data(index: str):
    await asyncio.sleep(random.randint(1, 5))
    print(f'Данные {index} получены')



async def main():
    tasks = [fetch_data(f'Kara x{i}') for i in range(1, 6)]
    await asyncio.gather(*tasks)



if __name__ == '__main__':
    asyncio.run(main())