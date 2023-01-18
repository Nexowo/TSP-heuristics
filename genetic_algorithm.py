import random
import point2D as p2d
from time import time

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 15

#paramètres de l'algorithme génétique
nb_generations = 1000 # nombre de générations
nb_individus = 10 # nombre d'individu par génération

def cal_fitness(solution : list[p2d.point2D]):
    return p2d.cal_distance(solution) #Pas de différence entre la fitness et la distance totale parcourue dans ce problème

def selection(population : list[list[p2d.point2D]]):
    sum_dist = 0

    for elem in population:
        sum_dist+=cal_fitness(elem)

    
    rd = random.random()
    probability = (1/cal_fitness(population[0]))/(1/sum_dist)
    i = 0
    while(rd > probability):
        i+=1
        probability+= (1/cal_fitness(population[i]))/(1/sum_dist)


    return population[i]

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

    temp = indiv[min(i,j):max(i,j)]
    temp.reverse()
    indiv[min(i,j):max(i,j)] = temp

    return indiv

def find_best_indiv(population:list[list[p2d.point2D]]):
    best_indiv = population[0]
    for i in range(1, len(population)):
        if cal_fitness(best_indiv) > cal_fitness(population[i]):
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

def sort(population: list[list[p2d.point2D]]):
    sorted_pop = []
    while population != []:
        best_indiv = find_best_indiv(population)
        population.remove(best_indiv)
        sorted_pop.append(best_indiv)
    return sorted_pop


solution = []
# instance = p2d.generate_instance(NOMBRE_DE_VILLES)
instance = p2d.import_csv("3.csv")

for _ in range(nb_individus):
    solution.append([*instance])
    random.shuffle(solution[-1])

best_indiv = find_best_indiv(solution)

starting_time = time()

for i in range(nb_generations):
    #select = selection(solution, nb_individus)
    print("Generation {}".format(i))
    for j in range(len(solution)):
        print(p2d.solution_id(solution[j]))
    new_s = []
    #random.shuffle(solution)
    solution = sort(solution)
    for j in range(0,int(0.6*len(solution)), 2):
        child_1, child_2 = croisement(selection(solution),selection(solution))
        child_1 = validate(child_1, instance)
        child_2 = validate(child_2, instance)
        new_s.append(child_1)
        new_s.append(child_2)

    for j in range(int (0.2*len(solution))):
        new_s.append(mutation(solution[random.randint(0,len(solution)-1)]))

    j = 0
    while len(new_s) < len(solution):
        new_s.append(solution[j])
        j+=1

    solution = new_s

    x = find_best_indiv(solution)
    if cal_fitness(x) < cal_fitness(best_indiv):
        best_indiv = [*x]

print (f"Le meilleur individu est {p2d.solution_id(best_indiv)}, fitness = {cal_fitness(best_indiv)}, ex-time = {time()-starting_time}")

p2d.print_solution(best_indiv)