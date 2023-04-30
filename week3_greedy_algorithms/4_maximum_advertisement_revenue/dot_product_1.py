from itertools import permutations


def max_dot_product(first_sequence, second_sequence):
    seq1 = sorted(first_sequence)
    seq2 = sorted(second_sequence)
    max_product = 0
    for i in range(len(first_sequence)):
        max_product += seq1[i]*seq2[i]
    return max_product

# res = max_dot_product([2,3,9],[7,4,2])
# print(res)


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
