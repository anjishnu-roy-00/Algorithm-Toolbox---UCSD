from itertools import combinations
invcount = 0
def merge(array,temp_arr,left,mid,right):
    #print(B)
    #print(C)
    invcount=0
    k = left
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if array[i] <= array[j]:
            temp_arr[k] = array[i]
            k+=1
            i+=1
        else:
            temp_arr[k] = array[j]
            invcount += (mid-i + 1)
            k+=1
            j+=1
    while i<= mid:
        temp_arr[k] = array[i]
        i+=1
        k+=1
    while j<= right:
        temp_arr[k] = array[j]
        j+=1
        k+=1
    for i in range(left,right+1):
        array[i] = temp_arr[i]
    return invcount

def _merge_sort(array,temp_arr,left,right):
    invcount=0
    if left < right:
        mid = (left+right)//2
        invcount+= _merge_sort(array,temp_arr,left,mid)
        invcount+= _merge_sort(array,temp_arr,mid+1,right)
        invcount+= merge(array,temp_arr,left,mid,right)
    return invcount

def inversions_efficient(array):
    temp_arr = [0]*len(array)
    return _merge_sort(array,temp_arr,0,len(array)-1)


# L = [2911,11,895,65,123,123,123,44,-200,1234,5400,2390,-2390,2390]
# L = [18, 16, 7, 13, 20, 4, 2, 15, 2, 1, 12]

# result = inversions_efficient(L)
# print(result)


# def inversions_naive(a):
#     number_of_inversions = 0
#     for i, j in combinations(range(len(a)), 2):
#         if a[i] > a[j]:
#             number_of_inversions += 1
#     return number_of_inversions


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_efficient(elements))
