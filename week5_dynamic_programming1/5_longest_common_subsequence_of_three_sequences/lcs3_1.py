def lcs3(first_sequence, second_sequence, third_sequence):
    dist = [[[0 for x in range(len(third_sequence)+1)] for y in range(len(second_sequence)+1)] for z in range(len(first_sequence)+1)]
    #print(dist)
    for i in range(1,len(first_sequence)+1):
        for j in range(1,len(second_sequence)+1):
            for k in range(1,len(third_sequence)+1):
                a,b,c = dist[i][j][k-1],dist[i][j-1][k],dist[i-1][j][k]
                d,e,f = dist[i][j-1][k-1],dist[i-1][j][k-1],dist[i-1][j-1][k]
                g = dist[i-1][j-1][k-1]
                if first_sequence[i-1] == second_sequence[j-1] and second_sequence[j-1] == third_sequence[k-1]:
                    dist[i][j][k] = 1 + g
                else:
                    dist[i][j][k] = max(a,max(b,max(c,max(d,max(e,max(f,g))))))
    # for elem in dist:
    #     print(elem)
    return dist[len(first_sequence)][len(second_sequence)][len(third_sequence)]


# a = [1,2,3]
# b = [2,1,3]
# c = [1,3,5]
# a = [8,3,2,1,7]
# b = [8,2,1,3,8,10,7]
# c = [6,8,3,1,4,7]
# res = lcs3(a,b,c)
# print(res)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
