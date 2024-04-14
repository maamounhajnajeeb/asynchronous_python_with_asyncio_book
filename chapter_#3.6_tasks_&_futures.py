import asyncio
from contextlib import suppress
from typing import Any


# 1
# f = asyncio.Future()
# print(f.done())

# f.cancel()
# print(f.cancelled())


# 2
# async def main(f: asyncio.Future): #1
#     await asyncio.sleep(1)
#     f.set_result("I have finished!") #2

# loop = asyncio.get_event_loop()
# fut = asyncio.Future() #3
# print(fut.done()) #4

# loop.create_task(main(fut)) #5
# print(loop.run_until_complete(fut)) #6
# print(fut.done())

# print(fut.result()) #7


# 3
# async def main(f: asyncio.Future):
#     await asyncio.sleep(1)

#     try:
#         f.set_result("I have finished!") #2
#     except RuntimeError as e:
#         print(f"No longer allowed: {e}")
#         f.cancel() #3

# loop = asyncio.get_event_loop()
# fut = asyncio.Task(asyncio.sleep(1_000_000)) #1
# print(fut.done())

# loop.create_task(main(fut))

# with suppress(asyncio.CancelledError):
#     loop.run_until_complete(fut)

# print(fut.done())

# print(fut.cancelled()) #3


# 4
# async def f(): #1
#     pass

# coro = f() #2
# loop = asyncio.get_event_loop() #3

# task = loop.create_task(coro) #4
# assert isinstance(task, asyncio.Task) #5

# new_task = asyncio.ensure_future(coro) #6
# assert isinstance(new_task, asyncio.Task)

# mystery_meat = asyncio.ensure_future(task) #7
# assert mystery_meat is task #8

# 5
# def listify(x: Any):
#     """ Try hard to convert x into list """
#     if isinstance(x, (str, bytes)):
#         return [x]
    
#     try:
#         return [_ for _ in x]
#     except TypeError:
#         return [x]

