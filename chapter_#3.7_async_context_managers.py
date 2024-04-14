# class Connection:
#     def __init__(self, host, port) -> None:
#         self.host, self.port = host, port
    
#     async def __aenter__(self):
#         self.conn = await get_conn(self.host, self.port)
#         return conn
    
#     async def __aexit__(self, exc_type, exc, tb):
#         await self.conn.close()

# async with Connection('localhost', 9001) as conn:
#     pass


# 2
# from contextlib import contextmanager

# @contextmanager #1
# def web_page(url):
#     data = download_webpage(url) #2
#     yield data
#     update_states(url) #3

# with web_page("google.com") as data: #4
#     process(data) #5


# 3
# from contextlib import asynccontextmanager

# @asynccontextmanager 
# async def web_page(url): 
#     data = await download_webpage(url) 
#     yield data 
#     await update_stats(url)

# async with web_page('google.com') as data: 
#      process(data)


# 4
# import asyncio
# from contextlib import asynccontextmanager

# @asynccontextmanager
# async def web_page(url):
#     loop = asyncio.get_event_loop()
#     data = await loop.run_in_executor(
#         None, download_webpage, url)
#     yield data

#     await loop.run_in_executor(None, update_stats, url)

# async with web_page("google.com") as data:
#     process(data)