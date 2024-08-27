import asyncio
import random


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял шар №{ball}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    names = ["Андрей", "Александр", "Максим", "Олег", "Егор", "Степан", "Владислав", "Вячеслав", "Боб"]
    tasks = []
    for task in range(3):
        task_ = asyncio.create_task(start_strongman(names[random.randint(0, len(names) - 1)], random.random()))
        tasks.append(task_)
    for task in tasks:
        await task


if __name__ == '__main__':
    asyncio.run(start_tournament())
