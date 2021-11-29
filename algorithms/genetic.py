from random import choices, randint, randrange, random
from typing import List, Optional, Callable, Tuple

Genome = List[int]
Population = List[Genome]
PopulateFunc = Callable[[], Population]
FitnessFunc = Callable[[Genome], int]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
PrinterFunc = Callable[[Population, int, FitnessFunc], None]


def generateGenome(length: int) -> Genome:
    return choices([0, 1], k=length)


def generatePopulation(size: int, genome_length: int) -> Population:
    return [generateGenome(genome_length) for _ in range(size)]


def singlePointCrossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Length of Genome A and Genome B have to be same length.")

    length = len(a)
    if length < 2:
        return a, b

    p = randint(1, length - 1)
    return a[0:p] + b[p:], b[0:p] + a[p:]


def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome))
        genome[index] = genome[index] if random() > probability else abs(genome[index] - 1)
    return genome


def populationFitness(population: Population, fitness_func: FitnessFunc) -> int:
    return sum([fitness_func(genome) for genome in population])


# def selectionPair(population: Population, fitness_func: FitnessFunc) -> Population:
#     weights = List[int]
#     return choices(
#         population=population,
#         weights=[fitness_func(gene) for gene in population],
#         k=2
#     )

def selectionPair(population: Population, fitnessFunc: FitnessFunc) -> Population:
    weights = []
    weightsGZ = False
    for gene in population:
      fitness = fitnessFunc(gene)
      weights.append(fitness)
      if fitness > 0:
        weightsGZ = True

    if weightsGZ == False:
        return choices(population=population, k=2)
        # raise RuntimeError("Useless poplation with no skills. Start again.")
    return choices(population=population, weights=weights, k=2)

def sortPopulation(population: Population, fitnessFunc: FitnessFunc) -> Population:
    return sorted(population, key=fitnessFunc, reverse=True)


def genomeToString(genome: Genome) -> str:
    return "".join(map(str, genome))


def printStats(population: Population, generation_id: int, fitness_func: FitnessFunc):
    print("Generation %02d\n" % generation_id)
    print("Population: [%s]" % ", ".join([genomeToString(gene) for gene in population]))
    print("Avg. Fitness: %f" % (populationFitness(population, fitness_func) / len(population)))
    sorted_population = sortPopulation(population, fitness_func)
    print(
        "Best: %s (%f)" % (genomeToString(sorted_population[0]), fitness_func(sorted_population[0])))
    print("Worst: %s (%f)" % (genomeToString(sorted_population[-1]),
                              fitness_func(sorted_population[-1])))
    print("")

    return sorted_population[0]


def runEvolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        fitness_limit: int,
        selection_func: SelectionFunc = selectionPair,
        crossover_func: CrossoverFunc = singlePointCrossover,
        mutation_func: MutationFunc = mutation,
        generation_limit: int = 100,
        printer: Optional[PrinterFunc] = None) \
        -> Tuple[Population, int]:
    population = populate_func()

    for i in range(generation_limit):
        population = sorted(population, key=lambda genome: fitness_func(genome), reverse=True)

        if printer is not None:
            printer(population, i, fitness_func)

        if fitness_func(population[0]) >= fitness_limit:
            break

        next_generation = population[0:2]

        for j in range(int(len(population) / 2) - 1):
            parents = selection_func(population, fitness_func)
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]

        population = next_generation

    return population, i
