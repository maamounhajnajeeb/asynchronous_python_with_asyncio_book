import inspect, asyncio


# 1
# async def f():
#     return 123

# print(type(f))

# print(inspect.iscoroutinefunction(f))


# 2
# def g():
#     yield 123

# print(type(g))

# gen = g()
# print(type(gen))

# print(inspect.isgenerator(gen))


# 3
# async def f():
#     return 123

# coro = f()
# print(type(coro))

# print(inspect.iscoroutine(coro))


# 4
# async def f():
#     return 123

# coro = f()
# try:
#     coro.send(None)
# except StopIteration as e:
#     print("the answer was:", e.value)


# 5 # new await keyword
# async def f():
#     await asyncio.sleep(1.0)
#     return 123

# async def main():
#     result = await f()
#     return result


# 6
# async def f():
#     try:
#         while True:
#             await asyncio.sleep(0)
#     except asyncio.CancelledError:
#         print("I was cancelled!")
#     else:
#         return 111

# coro = f()
# coro.send(None)
# coro.send(None)
# print(coro.throw(asyncio.CancelledError))


# 7
# async def f():
#     try:
#         while True:
#             await asyncio.sleep(0)
#     except asyncio.CancelledError:
#         print("Nope!")
#         while True:
#             await asyncio.sleep(0)
#     else:
#         return 111

# coro = f()
# coro.send(None)
# coro.throw(asyncio.CancelledError)

# coro.send(None)


# 8
async def f():
    await asyncio.sleep(0)
    return 111

loop = asyncio.get_event_loop()
coro = f()
print(loop.run_until_complete(coro))
