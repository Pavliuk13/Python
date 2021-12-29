from sys import argv


capacity = int(argv[1])
weights = list(map(int,argv[2:]))

def best_knapsack(capacity, weights):
    bars = [0] + weights
    bars_dict = {}
    for i in range(0, capacity + 1):
        bars_dict[(i, 0)] = 0
    for i in range(0, len(bars)):
        bars_dict[(0, i)] = 0
    for i in range(1, len(bars)):
        for mass in range(1, capacity + 1):
            bars_dict[(mass, i)] = bars_dict[(mass, (i - 1))]
            if bars[i] <= mass:
                temp_mass = bars_dict[(mass-bars[i]), i - 1] + bars[i]
                if bars_dict[(mass,i)] < temp_mass:
                    bars_dict[(mass,i)] = temp_mass
    return max(bars_dict.values())


print(best_knapsack(capacity,weights))