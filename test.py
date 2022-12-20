import genetic_algorithm as ga
import random
import point2D as p2d

NOMBRE_DE_VILLES = 15
nb_individus = 10

instance = p2d.generate_instance(NOMBRE_DE_VILLES)
solution = []

for _ in range(nb_individus):
    solution.append(instance.copy())
    random.shuffle(solution[-1])
    print("{} : {}".format(p2d.solution_id(solution[-1]), ga.cal_fitness(solution[-1])))

best_indiv = ga.find_best_indiv(solution)
print("best_indiv = {} : {}".format(p2d.solution_id(best_indiv), ga.cal_fitness(best_indiv)))