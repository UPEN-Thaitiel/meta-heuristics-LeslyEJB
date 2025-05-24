# Simulated Annealing - Guided Coding Challenge
# Your goal: Maximize the function f(x) using simulated annealing

# STEP 1: Import required libraries
# - Use 'random' from Python standard library for random number generation
# - Use 'numpy' for the exponential function (np.exp)
from random import random
import numpy as np

# STEP 2: Define the objective function f(x)
# This is the function you want to maximize:
# f(x) = (x - 0.3)^3 - 5x + x^2 - 2
def f(x):
    return (x - 0.3)**3 - 5 * x + x**2 - 2

# STEP 3: Define the SimulatedAnnealing class
# - Initialize with:
#   - min_coordinate: lower bound of x (e.g. -2)
#   - max_coordinate: upper bound of x (e.g. 2)
#   - min_temp: stopping temperature (e.g. 1e-5)
#   - max_temp: starting temperature (e.g. 100)
#   - cooling_rate: how fast the temperature drops (e.g. 0.02)
# - Track actual_state, next_state, best_state
class SimulatedAnnealing:
    def __init__(self, min_coordinate, max_coordinate, min_temp, max_temp, cooling_rate=0.02):
        self.min_coordinate = min_coordinate
        self.max_coordinate = max_coordinate
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.cooling_rate = cooling_rate
        self.actual_state = self.generate_random_x()
        self.best_state = self.actual_state

    # STEP 5: Implement generate_random_x
    # - Generate a new x value within the search range
    def generate_random_x(self):
        return self.min_coordinate + (self.max_coordinate - self.min_coordinate) * random()

    # STEP 6: Implement accept_prob as a static method
    # - Return 1 if new_energy > actual_energy
    # - Else return exp((actual_energy - new_energy) / temp)
    @staticmethod
    def accept_prob(actual_energy, next_energy, temp):
        if next_energy > actual_energy:
            return 1.0
        return np.exp((next_energy - actual_energy) / temp)

    # STEP 7: Implement get_energy as a static method
    # - Return f(x)
    @staticmethod
    def get_energy(x):
        return f(x)

    # STEP 4: Implement the run method
    # - Start with max_temp
    # - While temp > min_temp:
    #     - Generate new_state using generate_random_x()
    #     - Compute energies for current and new state using get_energy()
    #     - If new is better, accept it
    #     - If new is worse, accept it with a probability given by accept_prob()
    #     - Update best_state if current is better
    #     - Cool down the temperature
    #     - Print best result at the end
    def run(self):
        temp = self.max_temp

        while temp > self.min_temp:
            new_state = self.generate_random_x()

            actual_energy = self.get_energy(self.actual_state)
            new_energy = self.get_energy(new_state)

            if self.accept_prob(actual_energy, new_energy, temp) > random():
                self.actual_state = new_state

            if self.get_energy(self.actual_state) > self.get_energy(self.best_state):
                self.best_state = self.actual_state

            temp *= (1 - self.cooling_rate)

        print(f"Best state: x = {self.best_state:.5f}, f(x) = {self.get_energy(self.best_state):.5f}")

# STEP 8: Run the algorithm in main block
# if __name__ == '__main__':
#     algorithm = SimulatedAnnealing(-2, 2, 1e-5, 100)
#     algorithm.run()
if __name__ == '__main__':
    algorithm = SimulatedAnnealing(-2, 2, 1e-5, 100)
    algorithm.run()
