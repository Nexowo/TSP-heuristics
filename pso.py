import point2D as p2d
import random as rd

NOMBRE_DE_VILLE = 15
nb_particle = 10
nb_it = 100
gbest = []
omega = .5

class particle:
    state : list[p2d.point2D]
    pbest : list[p2d.point2D]
    __speed : list[list[p2d.point2D]]
    omega : float

    def __init__(self, s :list[p2d.point2D], omega : float):
        self.state = [*s]
        self.pbest = [*s]
        self.__speed = []
        self.omega = omega

    def fitness(self):
        return p2d.cal_distance(self.state)

    def dist(self, state : list[p2d.point2D]):
        temp = [*self.state]
        dist = []
        while temp != state:
            i = 0
            while temp[i] == state[i]:
                i+=1
            j = temp.index(state[i])

            invert = temp[i:j]
            invert.reverse()
            temp[i:j] = invert
            dist.append([temp[j], temp[i]])
        return dist

    def cal_speed(self):
        new_speed = []
        for elem in self.__speed:
            r = rd.random()
            if r < self.omega:
                new_speed.append(elem)
            
        d_pbest = self.dist(self.pbest)
        d_gbest = self.dist(gbest)

        a = rd.gauss(.5,1)
        b = rd.gauss(.5,1)

        for elem in d_pbest:
            r = rd.random()
            if a > r:
                new_speed.append(elem)

        for elem in d_gbest:
            r = rd.random()
            if b > r:
                new_speed.append(elem)

        self.__speed = new_speed

    def new_pos(self):
        for elem in self.__speed:
            x = elem[0]
            y = elem[1]

            i,j = self.state.index(x), self.state.index(y)

            temp = self.state[min(i,j):max(i,j)]
            temp.reverse()
            self.state[min(i,j):max(i,j)] = temp
        if self.fitness() < p2d.cal_distance(self.pbest):
            self.pbest = [*self.state]

instance = p2d.generate_instance(NOMBRE_DE_VILLE)
particles : list[particle]= []
for _ in range(nb_particle):
    state = [*instance]
    rd.shuffle(state)
    particles.append(particle(state, omega))

for i in range(nb_particle):
    if i == 0:
        gbest = [*particles[i].state]
    else:
        if particles[i].fitness() < p2d.cal_distance(gbest):
            gbest = [*particles[i].state]

for j in range(nb_it):
    print(f"{j}e iteration")
    for i in range(nb_particle):
        particles[i].cal_speed()
        particles[i].new_pos()

    for i in range(nb_particle):
        if particles[i].fitness() < p2d.cal_distance(gbest):
            gbest = [*particles[i].state]

print("Le meilleur infividu trouvé est {} avec une fitness de {}".format(p2d.solution_id(gbest), p2d.cal_distance(gbest)))
p2d.print_solution(gbest)