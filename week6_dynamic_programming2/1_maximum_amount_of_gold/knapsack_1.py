from sys import stdin


def maximum_gold(capacity, weights):
    values = [[0 for i in range(capacity+1)]for i in range(len(weights)+1)]
    # for elem in values:
    #     print(elem)
    for i in range(1,len(weights)+1):
        for j in range(1,capacity+1):
            if j >= weights[i-1]:
                values[i][j] = max(weights[i-1]+values[i-1][j-weights[i-1]],values[i-1][j])
            else:
                values[i][j] = values[i-1][j]
    # for elem in values:
    #     print(elem)
    return values[len(weights)][capacity]



# res = maximum_gold(10,[1,4,8])
# print(res)

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
