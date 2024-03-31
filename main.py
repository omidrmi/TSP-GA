import random
from matplotlib import pyplot as plt
import data
import rand

POPULATION_SIZE = 100
population = rand.randomPopulation(len(data.cities), POPULATION_SIZE)

unsuccessful_try = 0
best_fitness = 0
iteration = 0
while True:
    iteration += 1
    for _ in range(int(POPULATION_SIZE /2)):
        child_1, child_2 = data.crossover(*data.select_parent(population))
        if 40 < random.randint(0, 99) < 45:
            child_1 = data.mutation(child_1)
            child_2 = data.mutation(child_2)
        population.append(child_1)
        population.append(child_2)
        population.sort(key=lambda x: data.fitness(x))
        population = population[0: POPULATION_SIZE]
    current_fitness = data.fitness(population[0])
    if best_fitness == current_fitness:
        unsuccessful_try += 1
    else:
        unsuccessful_try = 0
        
    if unsuccessful_try >= 30:
        break
    best_fitness = current_fitness
    print("Best Fitness: {}".format(best_fitness))
        
print("Best Fitness: {} in {} iteration".format(best_fitness, iteration))