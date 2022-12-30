import point2D as p2d

# Données du problème (générées aléatoirement)
NOMBRE_DE_VILLES = 15

class ant:
    state : list[p2d.point2D]

    def __init__(self, ville : p2d.point2D) -> None:
        self.state = [ville]

    def cal_fitness(self):
        return p2d.cal_distance(self.state)

    def reset_it(self, ville: p2d.point2D):
        self.state = [ville]

    def add_cp(self, ville: p2d.point2D):
        self.state.append(ville)

    def get_state(self) -> p2d.point2D:
        return self.state.copy()

instance = p2d.generate_instance(NOMBRE_DE_VILLES)
population = []
for elem in instance:
    population.append(ant(elem))