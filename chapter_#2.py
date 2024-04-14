import threading
from queue import Queue
from typing import Callable

class Cutlery:
    def __init__(self, knives=0, forks=0) -> None:
        self.knives, self.forks = knives, forks
    
    def __repr__(self) -> str:
        return f"knives: {self.knives}, forks: {self.forks}"
    
    def give(self, to: 'Cutlery', knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)
    
    def change(self, knives, forks):
        # while self.lock:
        self.knives += knives
        self.forks += forks

kitchen = Cutlery(knives=100, forks=100)

class ThreadBot(threading.Thread):
    def __init__(self) -> None:
        super().__init__(target=self.manage_table)
        self.cutlery = Cutlery(knives=0, forks=0) 
        self.tasks = Queue()
    
    def manage_table(self):
        while True:
            task = self.tasks.get()
            if task == "prepare table":
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            elif task == "clear table":
                self.cutlery.give(to=self.cutlery, knives=4, forks=4)
            elif task == "shutdown":
                return

bots = [ThreadBot() for i in range(10)]

import sys
for bot in bots:
    for i in range(int(sys.argv[1])):
        bot.tasks.put("prepare table")
        bot.tasks.put("clear table")
    bot.tasks.put("shutdown")

print("Kitchen inventory before service:", kitchen)

for bot in bots:
    bot.start()

for bot in bots:
    bot.join()

print("Kitchen inventory after service:", kitchen)
