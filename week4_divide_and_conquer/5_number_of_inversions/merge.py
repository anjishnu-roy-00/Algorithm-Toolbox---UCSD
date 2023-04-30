from itertools import combinations

def merge(B,C):
    #print(B)
    #print(C)
    D = []
    bi = 0
    ci = 0
    while bi < len(B) and ci < len(C):
        if B[bi] <= C[ci]:
            D.append(B[bi])
            bi+=1
        else:
            D.append(C[ci])
            ci+=1
    if bi == len(B) and ci != len(C):
        for elem in C[ci:]:
            D.append(elem)
    elif ci == len(C) and bi!= len(B):
        for elem in B[bi:]:
            D.append(elem)
    return D

def merge_sort(array):
    if len(array) <= 1:
        return array
    m = len(array)//2
    B = merge_sort(array[0:m])
    C = merge_sort(array[m:])
    res = merge(B,C)
    return res


L = [2911,11,895,65,123,123,123,44,-200,1234,5400,2390,-2390,2390]
result = merge_sort(L)
print(result)


# def inversions_naive(a):
#     number_of_inversions = 0
#     for i, j in combinations(range(len(a)), 2):
#         if a[i] > a[j]:
#             number_of_inversions += 1
#     return number_of_inversions


# if __name__ == '__main__':
#     input_n = int(input())
#     elements = list(map(int, input().split()))
#     assert len(elements) == input_n
#     print(inversions_naive(elements))
