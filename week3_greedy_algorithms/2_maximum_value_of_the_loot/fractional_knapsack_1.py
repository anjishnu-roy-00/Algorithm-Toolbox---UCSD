from sys import stdin

def bestitem(weights,values):
    maxVperW = 0
    bestItem = 0
    for i in range(len(weights)):
        if weights[i]>0:
            if values[i]/weights[i] > maxVperW:
                maxVperW = values[i]/weights[i]
                bestItem = i
    return bestItem

def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    for i in range(len(weights)):
        if capacity == 0:
            return value
        b_i = bestitem(weights,values)
        a = min(weights[b_i], capacity)
        value = value + a * (values[b_i]/weights[b_i])
        weights[b_i] = weights[b_i] - a
        capacity = capacity - a
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
