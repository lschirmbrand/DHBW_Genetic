from functools import partial
from problems import knapsack
from algorithms import bruteforce, genetic
from helper.analyze import timer

# Change these parameters to change the algorithm parameters
AMOUNT_ITEMS = 30
SIZE_POPULATION = 40
GENERATION_LIMIT = 100
WEIGHT_LIMIT = 300


items = knapsack.generateItems(AMOUNT_ITEMS)
items = knapsack.moreItems

weight_limit = WEIGHT_LIMIT

print("\nWeight Limit: %dkg" % weight_limit)
print("Amount of Items: %d" % len(items))
print("\nBruteforce")
print("-----------------")

with timer():
	result = bruteforce(items, weight_limit)

knapsack.print_stats(result[1])

print("\nGenetic Algorithm")
print("-----------------")

with timer():
	population, generations = genetic.runEvolution(
		populate_func=partial(genetic.generatePopulation, size=SIZE_POPULATION, genome_length=len(items)),
		fitness_func=partial(knapsack.fitness, items=items, weight_limit=weight_limit),
		fitness_limit=result[0],
		generation_limit=GENERATION_LIMIT
	)

sack = knapsack.fromGenome(population[0], items)
knapsack.print_stats(sack)
