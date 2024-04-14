import time, asyncio

async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye")

def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} hello from a thread")

loop = asyncio.get_event_loop()
task = loop.create_task(main())

# run_in_executer() # to run things in seperate thread or process
# run_in_executer() # the executer task will begin executing only after run_until_complete()
loop.run_in_executor(None, blocking)
loop.run_until_complete(task)

pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
