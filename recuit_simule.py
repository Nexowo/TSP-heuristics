import random
import numpy as np
import point2D as p2d

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 15
T = 1000
facteur = 0.99

villes = p2d.generate_instance(NOMBRE_DE_VILLES)


def voisinage(solution : list[p2d.point2D]):
    new_solution = solution.copy()
    a = random.randint(0,len(new_solution)-1)
    b = random.randint(0,len(new_solution)-1)

    while a == b:
        b = random.randint(0,len(new_solution)-1)
    
    temp = new_solution[a]
    new_solution[a] = new_solution[b]
    new_solution[b] = temp

    return new_solution

### Initialisation du premier individu
solution = villes.copy() 
random.shuffle(solution)
cout0 = p2d.cal_distance(solution)
###

min_sol=solution
cout_min_sol=cout0
i=0

while T > 0.001:
    print('la ',i,'solution = ',p2d.solution_id(solution),' distance totale= ',cout0,' température actuelle =',T)
    T=T*facteur
    for j in range(50):
        nouv_sol=voisinage(solution)
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
    i+=1

print('voici la solution retenue ',p2d.solution_id(min_sol),' et son coût ', p2d.cal_distance(min_sol))

p2d.print_solution(min_sol)
