def majority_element_naive(elements):
    d={}
    s = set(elements)
    for elem in s:
        d[elem]=1
    surpass = len(elements)
    for elem in elements:
        if d[elem]>(surpass//2):
            return 1
        d[elem]+=1       
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
