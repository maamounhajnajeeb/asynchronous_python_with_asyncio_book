import asyncio

# 1
# class A:
#     def __aiter__(self):
#         self.x = 0
#         return self
    
#     def __anext__(self):
#         if self.x > 2:
#             raise StopIteration
#         else:
#             self.x += 1
#             return self.x

# a = A()
# for i in a:
#     print(i)


# 2
# from aioredis import create_redis

# async def main():
#     redis = await create_redis(('localhost', 6379))
#     keys = ['Americas', 'Africa', 'Europe', 'Asia']

#     async for value in OneAtTime(redis, keys):
#         await do_something_with(value)

# class OneAtTime:
#     def __init__(self, redis, keys) -> None:
#         self.redis, self.keys =  redis, keys
    
#     def __aiter__(self):
#         self.ikeys = iter(self.keys)
#         return self
    
#     async def __anext__(self):
#         try:
#             k = next(self.ikeys)
#         except StopIteration:
#             raise StopAsyncIteration
        
#         value = await redis.get(k)
#         return value

# asyncio.run(main())


# 3
# from aioredis import create_redis

# async def main(): #1
#     redis = await create_redis(('localhost', 6379))
#     keys = ['Americas', 'Africa', 'Europe', 'Asia']

#     async for value in one_at_time(redis, keys): #2
#         await do_something_with(value)

# async def one_at_time(redis, keys): #3
#     for key in keys:
#         value = await redis.get(key) #4
#         yield value #5

# asyncio.run(main())


# 4
# async def doubler(n):
#     for i in range(n):
#         yield i, i * 2
#         await asyncio.sleep(0.1)

# async def main():
#     result = [x async for x in doubler(3)]
#     print(result)

#     result = {x: y async for x, y in doubler(3)}
#     print(result)

#     result = {x async for x in doubler(3)}
#     print(result)

# asyncio.run(main())


# 5
# async def f(x):
#     await asyncio.sleep(0.1)

#     return x + 100

# async def factory(n):
#     for x in range(n):
#         await asyncio.sleep(0.1)
#         yield f, x

# async def main():
#     result = [await f(x) async for f, x in factory(3)]
#     print(result)

# asyncio.run(main())


# 6
# async def f(delay):
#     await asyncio.sleep(delay)

# loop = asyncio.get_event_loop()
# t1 = loop.create_task(f(1))
# t2 = loop.create_task(f(2))
# loop.run_until_complete(t1)
# loop.close()


# 7
async def echo(reader: asyncio.StreamReader, writer: asyncio.StreamWriter): #1
    print("new connection")

    try:
        while data := await reader.readline(): #2
            writer.write(data.upper()) #3
            await writer.drain()
        
        print("leaving connection")
    
    except asyncio.CancelledError: #4
        print("Connection dropped!")

async def main(host='127.0.0.1', port=8888):
    server = await asyncio.start_server(echo, host, port) #5

    async with server:
        await server.serve_forever()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Bye!")
