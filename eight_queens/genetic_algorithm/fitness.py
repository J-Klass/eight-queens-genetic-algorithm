class Fitness:
    def __init__(self, queen_placements):
        self.queen_placements = queen_placements
        self.number_of_opposing_queens = 0
        self.fitness = 0.0

    def opposing_queens(self):
        if self.number_of_opposing_queens == 0:
            n_opposing_queens = 0
            for index_a, queen_a in enumerate(self.queen_placements):
                for index_b, queen_b in enumerate(self.queen_placements):
                    if queen_a != queen_b:
                        if abs(index_a - index_b) == abs(
                            queen_a.position - queen_b.position
                        ):
                            n_opposing_queens += 1
            self.number_of_opposing_queens = n_opposing_queens

        return self.number_of_opposing_queens

    def placement_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / (1 + float(self.opposing_queens()))
        return self.fitness
