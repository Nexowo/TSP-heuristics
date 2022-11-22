import random
from matplotlib import pyplot as plt
import point2D as p2d

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 15

#paramètres de l'algorithme génétique
nb_generations = 100 # nombre de générations
nb_individus = 10 # nombre d'individu par génération

def cal_fitness(solution : list[p2d.point2D]):
    return p2d.cal_distance(solution) #Pas de différence entre la fitness et la distance totale parcourue dans ce problème

def selection(population : list[list[p2d.point2D]], nb_individus):
    sum_dist = 0

    for elem in population:
        sum_dist+=cal_fitness(elem)

    selection = []
    while (len(selection) < nb_individus):
        rd = random.random()
        probability = cal_fitness(population[0])/sum_dist
        i = 0
        while(rd > probability):
            i+=1
            probability+= cal_fitness(population[i])/sum_dist

        selection.append(population[i])


solution = []
for i in range(nb_individus):
    solution.append(p2d.generate_instance(NOMBRE_DE_VILLES))
    random.shuffle(solution[-1])