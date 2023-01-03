import point2D as p2d
import random

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 15
taux_evap = 0.25
alpha = 0.5
beta = 1.5

class ant:
    state : list[p2d.point2D]
    alpha : float
    beta : float

    def __init__(self, ville : p2d.point2D, alpha : float, beta : float) -> None:
        self.state = [ville]
        self.alpha = alpha
        self.beta = beta

    def cal_fitness(self):
        return p2d.cal_distance(self.state)

    def reset_it(self, ville: p2d.point2D):
        self.state = [ville]

    def add_cp(self, ville: p2d.point2D):
        self.state.append(ville)

    def get_state(self) -> p2d.point2D:
        return self.state.copy()

    def __calc_proba(self, pheromones : list[list[float]], instance : list[p2d.point2D]):
        proba = [0 for _ in range(len(instance))]
        sum = 0
        for elem in instance:
            sum += pheromones[self.state[-1].id][elem.id]**self.alpha * self.state[-1].dist(elem)**self.beta

        for elem in instance:
            proba[elem.id] = pheromones[self.state[-1].id][elem.id]**self.alpha * self.state[-1].dist(elem)**self.beta / sum

        return proba
            
    def select_next_town(self, pheromones: list[list[float]], instance : list[p2d.point2D]):
        temp_ins = instance.copy()
        for elem in temp_ins:
            if elem in self.state:
                temp_ins.remove(elem)
        
        p = self.__calc_proba(pheromones, temp_ins)
        r = random.random()
        i = 0
        sum = 0
        while(sum + p[i] < r):
            i += 1
            sum += p[i]
        self.add_cp(temp_ins[i])

def actualize_pheromones(population : list[ant], pheromones : list[list[float]], tx_evap : float):
    for i in len(pheromones):
        for j in len(pheromones[i]):
            pheromones[i][j] = (1-tx_evap)*pheromones[i][j]
    
    for elem in population:
        f = elem.cal_fitness()
        s = elem.get_state()
        for i in range(len(s)):
            j = i+1
            if j == len(s):
                j = 0
            
            pheromones[i][j] += 5/f
            pheromones[j][i] += 5/f

    return pheromones

instance = p2d.generate_instance(NOMBRE_DE_VILLES)
population = []
for elem in instance:
    population.append(ant(elem, alpha, beta))