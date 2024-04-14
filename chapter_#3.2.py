import asyncio, time


async def main():
    # asyncio.get_event_loop()
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")

# asyncio.run()
# 1] loop.run_untile_complete()
# 2] pending, gathering, canceling
# 3] loop.close()

loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_until_complete(task)
pending = asyncio.all_tasks(loop=loop)

for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
