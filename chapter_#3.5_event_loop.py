import asyncio

# 1
loop = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()
print(loop is loop2)


# 2
async def f():
    for i in range():
        asyncio.create_task()