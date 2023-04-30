def binary_search(keys, query):
    # write your code here
    mid = 0
    seek = len(keys)
    flag = 0
    left = 0
    right = len(keys)-1
    while right >= left:
        mid = (left+right)//2
        if query == keys[mid] and mid<seek:
            flag = 1
            seek = mid
            right = mid - 1
        if query < keys[mid]:
            right = mid - 1
        if query > keys[mid]:
            left = mid + 1
    if flag == 1:
        return seek
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
