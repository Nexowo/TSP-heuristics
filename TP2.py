import random
import numpy as np
from matplotlib import pyplot as plt
from math import sqrt

class point2D:
    x : float
    y : float
    id : int

    def __init__(self, id : int, x : float, y : float):
        self.id = id
        self.x = x
        self.y = y

    def dist(self, point : object):
        if isinstance(point, point2D):
            return sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

def add_point_to_plot(point : point2D):
    plt.plot(point.x, point.y, marker = "o", markersize = 5, markerfacecolor="green")

def print_solution(solution : list[point2D]):
    for i in range(len(solution)) :
        if i != len(solution)-1:
            plt.plot([solution[i].x, solution[i+1].x], [solution[i].y, solution[i+1].y], color = "blue")
        else:
            plt.plot([solution[i].x, solution[0].x], [solution[i].y, solution[0].y], color = "blue")

def cal_distance(solution : list[point2D]):
    tot_dist = 0
    for i in range(len(solution)) :
        if i != len(solution)-1:
            tot_dist+=solution[i].dist(solution[i+1])
        else:
            tot_dist+=solution[i].dist(solution[0])

    return tot_dist

def solution_id(solution : list[point2D]):
    id = []
    for ville in solution:
        id.append(ville.id)
    return id

def voisinage(solution : list[point2D]):
    new_solution = solution.copy()
    a = random.randint(0,len(new_solution)-1)
    b = random.randint(0,len(new_solution)-1)

    while a == b:
        b = random.randint(0,len(new_solution)-1)
    
    temp = new_solution[a]
    new_solution[a] = new_solution[b]
    new_solution[b] = temp

    return new_solution

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 15
T = 1000
facteur = 0.99

villes  = []
for i in range(NOMBRE_DE_VILLES):
    x, y = random.random()*1000, random.random()*1000
    villes.append(point2D(i, x, y))
    add_point_to_plot(villes[-1])

### Initialisation du premier individu
solution = villes.copy() 
random.shuffle(solution)
cout0 = cal_distance(solution)
###

min_sol=solution
cout_min_sol=cout0

for i in range(100):
    print('la ',i,'solution = ',solution_id(solution),' distance totale= ',cout0,' température actuelle =',T)
    T=T*facteur
    for j in range(50):
        nouv_sol=voisinage(solution)
        cout1=cal_distance(nouv_sol)
         # print('la ',j,'ème recherche de voisinage de',solution,'donne la solution=' ,nouv_sol,' distance totale= ',cout1) 
        if cout1<cout0:
            cout0=cout1
            solution=nouv_sol
            if cout1<cout_min_sol:
                cout_min_sol=cout1
                min_sol=solution.copy()
        else:
            x=np.random.uniform()
            if x<np.exp((cout0-cout1)/T):
                cout0=cout1
                solution=nouv_sol

print('voici la solution retenue ',solution_id(min_sol),' et son coût ', cal_distance(min_sol))

print_solution(min_sol)
plt.show()
