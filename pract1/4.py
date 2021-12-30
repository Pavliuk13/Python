from sys import argv


capacity = int(argv[1])
weights = list(map(int,argv[2:]))


def best_knapsack(max_weight, weights):
    n = len(weights) + 1
    array = [0] * n
    for i in range(n):
        array[i] = [0] * (max_weight + 1)

    for i in range(0, n):
        for j in range(0, max_weight + 1):
            if i != 0 and j != 0:
                if weights[i - 1] > j:
                    array[i][j] = array[i - 1][j]
                else:
                    prev = array[i - 1][j]
                    new_val = array[i - 1][j - weights[i - 1]] + weights[i - 1]
                    array[i][j] = max(prev, new_val)

    return array[n - 1][max_weight]


print(best_knapsack(capacity, weights))