import asyncio


async def make_sound(task_name: str, delay: int):
    await asyncio.sleep(delay)
    print(task_name)



async def main():
    await asyncio.gather(
        make_sound('Неимоверная чушь - 1', 1),
        make_sound('Неимоверная чушь - 2', 2),
        make_sound('Неимоверная чушь - 3', 3)
    )



if __name__ == '__main__':
    asyncio.run(main())