from math import sqrt
from matplotlib import pyplot as plt
import random
import pandas as pd

class point2D:
    x : float
    y : float
    id : int

    def __init__(self, id : int, x : float, y : float):
        self.id = id
        self.x = x
        self.y = y

    def dist(self, point : "point2D"):
        return sqrt((point.x - self.x)**2 + (point.y - self.y)**2)

    def __eq__(self, __o: "point2D") -> bool:
        return __o.id == self.id and __o.x == self.x and __o.y == self.y

def add_point_to_plot(point : point2D):
    plt.plot(point.x, point.y, marker = "o", markersize = 5, markerfacecolor="green")

def print_solution(solution : list[point2D]):
    for i in range(len(solution)) :
        if i != len(solution)-1:
            plt.plot([solution[i].x, solution[i+1].x], [solution[i].y, solution[i+1].y], color = "blue")
        else:
            plt.plot([solution[i].x, solution[0].x], [solution[i].y, solution[0].y], color = "blue")
    plt.show()

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


def generate_instance(nb_ville):
    villes  = []
    for i in range(nb_ville):
        x, y = random.random()*1000, random.random()*1000
        villes.append(point2D(i, x, y))
        add_point_to_plot(villes[-1])

    return villes

def generate_csv(nb_ville, name_csv):
    villes = []
    for i in range(nb_ville):
        villes.append([i, random.random()*1000, random.random()*1000])
    
    df = pd.DataFrame(villes)
    df.to_csv(name_csv)

def import_csv(name_csv):
    df = pd.read_csv(name_csv, sep=',')
    villes = []
    print(df)
    for i in range(len(df)):
        villes.append(point2D(i, df.iat[i,1], df.iat[i,2]))
        add_point_to_plot(villes[-1])
    return villes