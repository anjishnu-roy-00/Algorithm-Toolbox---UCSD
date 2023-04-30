import math
def compute_operations(n):
    array = [0]*(n+1)
    output_sequence = []
    for i in range(2,n+1):
            a1 = math.inf
            m2 = math.inf
            m3 = math.inf
            if i - 1 >= 0:
                 a1 = 1 + array[i-1]
            if i % 2 == 0 and i/2 >= 0:
                 m2 = 1 + array[i//2]
            if i % 3 == 0 and i/3 >= 0:
                 m3 = 1 + array[i//3]
            array[i] = min(a1,min(m2,m3))
    num = array[n]
    #print(array[n//2])
    while(n>1):
        if n%3 == 0 and array[int(n//3)]+1 == array[int(n)]:
            output_sequence.append(int(n))
            n/=3
        elif n%2 == 0 and array[int(n//2)]+1 == array[int(n)]:
             output_sequence.append(int(n))
             n/=2
        elif array[int(n-1)]+1 == array[int(n)]:
             output_sequence.append(int(n))
             n-=1
    output_sequence.append(1)
    output_sequence.reverse()
    return output_sequence
    

# res = compute_operations(96234)
# print(res)

if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)
