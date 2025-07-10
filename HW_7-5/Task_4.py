import asyncio


async def countdown(n: int):
    for i in range(n, 0, -1):
        print(i)
        await asyncio.sleep(1)
    print('Kara!')



async def main():
    await countdown(3)



if __name__ == '__main__':
    asyncio.run(main())



