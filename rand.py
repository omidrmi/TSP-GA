import random


def randomIndivisual(gen_count = 10):
    return random.sample(range(gen_count), gen_count)


def randomPopulation(gen_count = 10, populationCount = 100):
    return [randomIndivisual(gen_count) for i in range(populationCount)]