cities = [
    (16.47, 96.10),
    (16.47, 94.44),
    (20.09, 92.54),
    (22.39, 93.37), 
    (25.23, 97.24), 
    (22.00, 96.05), 
    (20.47, 97.02), 
    (17.20, 96.29), 
    (16.30, 97.38), 
    (14.05, 98.12), 
    (16.53, 97.38), 
    (21.52, 95.59), 
    (19.41, 97.13), 
    (20.09, 94.55), 
]




import math
import random

def calculate_distance(point1, point2):
    x2, y2 = point2
    x1, y1 = point1
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

def fitness(indivisual = []):
    sum = 0
    for index in range(len(indivisual)):
        next_index = index + 1 if index  + 1 < len(indivisual) else 0
        city_index_1 = indivisual[index]
        city_index_2 = indivisual[next_index]
        sum += calculate_distance(cities[city_index_1], cities[city_index_2])
    return sum


def select_parent(population: list):
    fitness_population = [fitness(i) for i in population]
    fitness_sum = sum(fitness_population)
    parent_1, parent_2 = random.choices(population, weights=[(1 / i) / fitness_sum for i in fitness_population],k=2)
    return parent_1, parent_2


def correct_child(child: list[int]):
    all_elements = set(range(len(child)))
    unique_elements = set(child)
    missing_elements = all_elements - unique_elements
    corrected_array = []
    for element in child:
        if element in unique_elements:
            corrected_array.append(element)
            unique_elements.remove(element)
        else:
            corrected_array.append(missing_elements.pop())
    return corrected_array


def crossover(parent_1: list[int], parent_2: list[int]):
    cross_line_1 = random.randint(0, int(len(parent_2) / 2))
    cross_line_2 = random.randint(int(len(parent_2) / 2) + 1, len(parent_2) - 1)
    child_1 = parent_1[:cross_line_1] + parent_2[cross_line_1: cross_line_2] +  parent_1[cross_line_2:]
    child_2 = parent_2[:cross_line_1] + parent_1[cross_line_1: cross_line_2] +  parent_2[cross_line_2:]
    return correct_child(child_1), correct_child(child_2)

def mutation(child: list[int]):
    line_1 = random.randrange(len(child))
    line_2 = random.randrange(len(child))
    temp = child[line_1]
    child[line_1] = child[line_2]
    child[line_2] = temp
    return correct_child(child)