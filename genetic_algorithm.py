import random
from matplotlib import pyplot as plt
import point2D as p2d

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 5

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
    for _ in range(nb_individus):
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
    child_1 = []
    child_2 = []
    for j in range(i):
        child_1.append(indiv1[j])
        child_2.append(indiv2[j])
    for j in range(i, len(indiv1)):
        child_1.append(indiv2[j])
        child_2.append(indiv1[j])

    return child_1, child_2

def mutation(indiv : list[p2d.point2D]):

    i = random.randint(0, len(indiv)-1)
    j = random.randint(0, len(indiv)-1)

    temp = indiv[i]
    indiv[i] = indiv[j]
    indiv[j] = temp

    return indiv

def find_best_indiv(population:list[list[p2d.point2D]]):
    best_indiv = population[0]
    for i in range(1, len(population)):
        if cal_fitness(best_indiv) < cal_fitness(population[i]):
            best_indiv = population[i]
    return best_indiv

def validate(elem : list[p2d.point2D], list_not_sorted : list[p2d.point2D]):
    nb_it = [0 for _ in range(len(elem))]
    for element in elem:
        nb_it[element.id]+=1
    
    for i in range(len(nb_it)):
        if nb_it[i] == 0:
            elem.append(list_not_sorted[i])
        if nb_it[i] == 2:
            elem.remove(list_not_sorted[i])

    return elem

solution = []
instance = p2d.generate_instance(NOMBRE_DE_VILLES)

for _ in range(nb_individus):
    solution.append(instance.copy())
    random.shuffle(solution[-1])

best_indiv = find_best_indiv(solution)

for i in range(nb_generations):
    #select = selection(solution, nb_individus)
    print("Generation {}".format(i))
    for j in range(len(solution)):
        print(p2d.solution_id(solution[j]))
    new_s = []
    random.shuffle(solution)
    for j in range(0,int(0.8*len(solution)), 2):
        child_1, child_2 = croisement(solution[j],solution[j+1])
        child_1 = validate(child_1, instance)
        child_2 = validate(child_2, instance)
        new_s.append(child_1)
        new_s.append(child_2)

    for j in range(int (0.2*len(solution))):
        new_s.append(mutation(solution[-j-1]))

    solution = new_s

    x = find_best_indiv(solution)
    if cal_fitness(x) < cal_fitness(best_indiv):
        best_indiv = x.copy()

p2d.print_solution(best_indiv)
plt.show()