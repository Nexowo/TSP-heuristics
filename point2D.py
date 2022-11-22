from math import sqrt
from matplotlib import pyplot as plt
import random

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


def generate_instance(nb_ville):
    villes  = []
    for i in range(nb_ville):
        x, y = random.random()*1000, random.random()*1000
        villes.append(point2D(i, x, y))
        add_point_to_plot(villes[-1])

    return villes