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

    return selection

def croisement(indiv1 : list[p2d.point2D], indiv2 : list[p2d.point2D]):
    i = random.randint(0, len(indiv1))
    child_1 = [0 for _ in range(len(indiv1))]
    child_2 = [0 for _ in range(len(indiv1))]
    child_1[0:i] = indiv1[0:i]
    child_2[0:i] = indiv2[0:i]
    if i != len(child_1):
        child_1[i+1:-1] = indiv2[i+1:-1]
        child_2[i+1:-1] = indiv1[i+1:-1]
    return child_1, child_2

def mutation(indiv : list[p2d.point2D]):
    i = random.randint(0, len(indiv))
    j = random.randint(i, len(indiv))

    middle = indiv[i:j]
    middle.reverse()
    indiv[i:j] = middle

    return indiv

def find_best_indiv(population:list[list[p2d.point2D]]):
    best_indiv = population[0]
    for i in range(1, len(population)):
        if cal_fitness(best_indiv) < cal_fitness(population[i]):
            best_indiv = population[i]
    return best_indiv

solution = []

for _ in range(nb_individus):
    solution.append(p2d.generate_instance(NOMBRE_DE_VILLES))
    random.shuffle(solution[-1])

best_indiv = find_best_indiv(solution)

for i in range(nb_generations):
    select = selection(solution, nb_individus)
    for j in range(int(0.8*len(select))):
        select[j], select[j+1] = croisement(select[j],select[j+1])
        j+=1

    for j in range(int (0.2*len(select))):
        select[-j-1] = mutation(select[-j-1])

    solution = select
    x = find_best_indiv(solution)
    if cal_fitness(x) < cal_fitness(best_indiv):
        best_indiv = x

p2d.print_solution(solution)
plt.show()