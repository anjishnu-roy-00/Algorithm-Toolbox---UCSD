def lcs2(first_sequence, second_sequence):
    dist = [[0 for x in range(len(second_sequence)+1)] for y in range(len(first_sequence)+1)]
    #print(dist)
    for i in range(1,len(first_sequence)+1):
        for j in range(1,len(second_sequence)+1):
            insertion = dist[i][j-1]
            deletion = dist[i-1][j] 
            mismatch = dist[i-1][j-1] + 1
            if first_sequence[i-1] == second_sequence[j-1]:
                dist[i][j] = mismatch
            else:
                dist[i][j] = max(insertion,deletion)
    # for elem in dist:
    #     print(elem)
    return dist[len(first_sequence)][len(second_sequence)]

# a = [2,7,5]
# b = [2,5]
# a=[7]
# b=[1,2,3,4]
# a=[2,7,8,3]
# b=[5,2,8,7]
# res = lcs2(a,b)
# print(res)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
