from problems import knapsack
from algorithms import bruteforce
import time

weight_limit = 3000

for i in range(31):
    items = knapsack.generateItems(i)
    start = time.time()
    bruteforce(items, weight_limit)
    end = time.time()

    print(f"{i}\t|\t{end-start}s")
