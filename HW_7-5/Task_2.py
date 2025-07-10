import asyncio


async def delayed_print(text: str, delay: int):
    await asyncio.sleep(delay)
    print(text)



async def main():
    await asyncio.gather(delayed_print('Kara', 1), delayed_print('Double Kara', 5), delayed_print('Чушь', 7))



if __name__ == '__main__':
    asyncio.run(main())
