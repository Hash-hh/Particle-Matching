import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from numpy import int64

all_solutions = [{'solution': array([0, 1, 2], dtype=int64), 'energy': -3.75, 'num_occurrences': 273}, {'solution': array([0, 1, 2], dtype=int64), 'energy': -3.75, 'num_occurrences': 1}, {'solution': array([0, 0, 2], dtype=int64), 'energy': -3.0, 'num_occurrences': 159}, {'solution': array([0, 1, 2], dtype=int64), 'energy': -3.0, 'num_occurrences': 116}, {'solution': array([0, 1, 0], dtype=int64), 'energy': -3.0, 'num_occurrences': 87}, {'solution': array([0, 0, 2], dtype=int64), 'energy': -1.75, 'num_occurrences': 49}, {'solution': array([0, 0, 0], dtype=int64), 'energy': -1.75, 'num_occurrences': 26}, {'solution': array([0, 1, 0], dtype=int64), 'energy': -1.75, 'num_occurrences': 17}, {'solution': array([0, 0, 1], dtype=int64), 'energy': -1.381966011250105, 'num_occurrences': 26}, {'solution': array([1, 0, 2], dtype=int64), 'energy': -1.381966011250105, 'num_occurrences': 37}, {'solution': array([0, 2, 0], dtype=int64), 'energy': -1.381966011250105, 'num_occurrences': 25}, {'solution': array([0, 0, 2], dtype=int64), 'energy': -1.381966011250105, 'num_occurrences': 47}, {'solution': array([0, 2, 0], dtype=int64), 'energy': -1.381966011250105, 'num_occurrences': 1}, {'solution': array([0, 0, 1], dtype=int64), 'energy': -0.7499999999999998, 'num_occurrences': 15}, {'solution': array([0, 0, 0], dtype=int64), 'energy': -0.7499999999999998, 'num_occurrences': 13}, {'solution': array([0, 2, 0], dtype=int64), 'energy': -0.7499999999999998, 'num_occurrences': 13}, {'solution': array([1, 0, 0], dtype=int64), 'energy': -0.7499999999999998, 'num_occurrences': 15}, {'solution': array([0, 0, 0], dtype=int64), 'energy': 0.0, 'num_occurrences': 2}, {'solution': array([0, 2, 2], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 5}, {'solution': array([0, 0, 1], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 1}, {'solution': array([1, 1, 2], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 4}, {'solution': array([0, 2, 2], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 2}, {'solution': array([0, 1, 1], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 1}, {'solution': array([0, 0, 2], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 4}, {'solution': array([0, 0, 2], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 6}, {'solution': array([0, 0, 2], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 2}, {'solution': array([0, 1, 0], dtype=int64), 'energy': 0.4860679774997898, 'num_occurrences': 2}, {'solution': array([0, 1, 0], dtype=int64), 'energy': 0.6180339887498949, 'num_occurrences': 1}, {'solution': array([0, 2, 2], dtype=int64), 'energy': 0.6180339887498949, 'num_occurrences': 3}, {'solution': array([0, 1, 0], dtype=int64), 'energy': 0.6180339887498949, 'num_occurrences': 2}, {'solution': array([0, 0, 1], dtype=int64), 'energy': 0.6180339887498949, 'num_occurrences': 5}, {'solution': array([1, 1, 0], dtype=int64), 'energy': 0.6180339887498949, 'num_occurrences': 2}, {'solution': array([0, 0, 0], dtype=int64), 'energy': 0.6180339887498949, 'num_occurrences': 5}, {'solution': array([0, 1, 1], dtype=int64), 'energy': 0.6180339887498949, 'num_occurrences': 5}, {'solution': array([0, 0, 0], dtype=int64), 'energy': 0.6180339887498949, 'num_occurrences': 5}, {'solution': array([0, 2, 1], dtype=int64), 'energy': 1.0000000000000009, 'num_occurrences': 2}, {'solution': array([1, 2, 0], dtype=int64), 'energy': 1.0000000000000009, 'num_occurrences': 1}, {'solution': array([0, 0, 1], dtype=int64), 'energy': 1.0000000000000009, 'num_occurrences': 1}, {'solution': array([1, 2, 0], dtype=int64), 'energy': 1.0000000000000009, 'num_occurrences': 1}, {'solution': array([1, 0, 2], dtype=int64), 'energy': 1.4860679774997907, 'num_occurrences': 2}, {'solution': array([2, 0, 0], dtype=int64), 'energy': 2.25, 'num_occurrences': 1}, {'solution': array([0, 0, 0], dtype=int64), 'energy': 2.25, 'num_occurrences': 3}, {'solution': array([0, 1, 2], dtype=int64), 'energy': 2.48606797749979, 'num_occurrences': 1}, {'solution': array([0, 1, 1], dtype=int64), 'energy': 2.48606797749979, 'num_occurrences': 1}, {'solution': array([2, 1, 0], dtype=int64), 'energy': 2.5615528128088303, 'num_occurrences': 3}, {'solution': array([0, 1, 2], dtype=int64), 'energy': 2.8541019662496847, 'num_occurrences': 2}, {'solution': array([0, 0, 0], dtype=int64), 'energy': 3.0000000000000004, 'num_occurrences': 1}, {'solution': array([0, 1, 0], dtype=int64), 'energy': 5.3731056256176615, 'num_occurrences': 1}, {'solution': array([0, 0, 1], dtype=int64), 'energy': 5.48606797749979, 'num_occurrences': 1}, {'solution': array([0, 0, 0], dtype=int64), 'energy': 7.3731056256176615, 'num_occurrences': 1}, {'solution': array([0, 0, 0], dtype=int64), 'energy': 11.53935903020517, 'num_occurrences': 1}]

correct_solution = [0, 1, 2]

# Extract energy values and num_occurrences
energies = [d["energy"] for d in all_solutions]
num_occurrences = [d["num_occurrences"] for d in all_solutions]
solutions = [d["solution"] for d in all_solutions]

# Create the histogram
bars = plt.bar(energies, num_occurrences, width=0.2, zorder=3, color='red')

# Iterate over the bars and color the ones matching the provided solution in green
for bar, solution in zip(bars, solutions):
    if np.array_equal(solution, correct_solution):
        bar.set_color('green')

# Set labels and title
plt.xlabel("Energy")
plt.ylabel("Number of Occurrences")
plt.title("Histogram of Energies")

# Show the plot
plt.show()