import point2D as p2d
import random
from copy import copy
from time import time

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 15
taux_evap = 0.95
alpha = 2
beta = 2
n_gen = 100

class ant:
    state : list[p2d.point2D]
    alpha : float
    beta : float

    def __init__(self, ville : p2d.point2D, alpha : float, beta : float) -> None:
        self.state = [ville]
        self.alpha = alpha
        self.beta = beta

    def __copy__(self):
        new_ant = ant(self.state[0], self.alpha, self.beta)
        new_ant.state = [*self.state]
        return new_ant

    def cal_fitness(self):
        return p2d.cal_distance(self.state)

    def reset_it(self, ville: p2d.point2D):
        self.state = [ville]

    def add_cp(self, ville: p2d.point2D):
        self.state.append(ville)

    def get_state(self) -> p2d.point2D:
        return [*self.state]

    def __calc_proba(self, pheromones : list[list[float]], instance : list[p2d.point2D]):
        proba = [0 for _ in range(len(instance))]
        sum = 0
        for elem in instance:
            sum += pheromones[self.state[-1].id][elem.id]**self.alpha * (1/(self.state[-1].dist(elem)**self.beta))

        for i in range(len(instance)):
            proba[i] = (pheromones[self.state[-1].id][instance[i].id]**self.alpha * (1/(self.state[-1].dist(instance[i])**self.beta))) / sum

        return proba
            
    def select_next_town(self, pheromones: list[list[float]], instance : list[p2d.point2D]):
        temp_ins = [*instance]

        for elem2 in self.state:
            for elem in temp_ins:
                if elem == elem2:
                    temp_ins.remove(elem)
        
        p = self.__calc_proba(pheromones, temp_ins)
        r = random.random()
        i = 0
        sum = 0
        while(sum + p[i] < r):
            sum += p[i]
            i += 1
        self.add_cp(temp_ins[i])

def actualize_pheromones(population : list[ant], pheromones : list[list[float]], tx_evap : float):
    for i in range(len(pheromones)):
        for j in range(len(pheromones[i])):
            pheromones[i][j] = tx_evap*pheromones[i][j]
    
    for elem in population:
        f = elem.cal_fitness()
        s = elem.get_state()
        for i in range(len(s)):
            j = i+1
            if j == len(s):
                j = 0
            
            pheromones[i][j] += 1000/f
            pheromones[j][i] += 1000/f

    return pheromones

def select_best(population : list[ant]):
    best = population[0]
    for elem in population[1:]:
        if elem.cal_fitness() < best.cal_fitness():
            best = elem
    return best

#instance = p2d.generate_instance(NOMBRE_DE_VILLES)
instance = p2d.import_csv("3.csv")
population : list[ant] = []
global_best : ant
for elem in instance:
    population.append(ant(elem, alpha, beta))

pheromones = [[2 for _ in range(len(instance))] for _ in range(len(instance))]

starting_time = time()

for i in range(n_gen):
    for _ in range(len(instance)-1):
        for elem in population:
            elem.select_next_town(pheromones, instance)
    
    pheromones = actualize_pheromones(population,pheromones,taux_evap)
    best_indiv = select_best(population)
    if(i == 0):
        global_best = copy(best_indiv)
    else:
        if global_best.cal_fitness() > best_indiv.cal_fitness():
            global_best = copy(best_indiv)

    print(f"Génération {i}")
    for j in range(len(population)):
        print(f"Fourmi {j} = {p2d.solution_id(population[j].get_state())}, fitness = {population[j].cal_fitness()}")
    
    for j in range(len(instance)):
        population[j].reset_it(instance[j])

print("Le meilleur individu trouvé est {} avec une fitness de {}, en {} secondes".format(p2d.solution_id(global_best.get_state()), global_best.cal_fitness(), time()-starting_time))
p2d.print_solution(global_best.get_state())