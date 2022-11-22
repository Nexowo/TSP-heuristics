import random
import numpy as np
from matplotlib import pyplot as plt
import point2D as p2d

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 15
T = 1000
facteur = 0.99

villes  = []
for i in range(NOMBRE_DE_VILLES):
    x, y = random.random()*1000, random.random()*1000
    villes.append(p2d.point2D(i, x, y))
    p2d.add_point_to_plot(villes[-1])

### Initialisation du premier individu
solution = villes.copy() 
random.shuffle(solution)
cout0 = p2d.cal_distance(solution)
###

min_sol=solution
cout_min_sol=cout0

for i in range(100):
    print('la ',i,'solution = ',p2d.solution_id(solution),' distance totale= ',cout0,' température actuelle =',T)
    T=T*facteur
    for j in range(50):
        nouv_sol=p2d.voisinage(solution)
        cout1=p2d.cal_distance(nouv_sol)
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

print('voici la solution retenue ',p2d.solution_id(min_sol),' et son coût ', p2d.cal_distance(min_sol))

p2d.print_solution(min_sol)
plt.show()
