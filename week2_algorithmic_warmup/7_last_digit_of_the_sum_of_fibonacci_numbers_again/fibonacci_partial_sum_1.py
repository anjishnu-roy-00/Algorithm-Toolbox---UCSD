# Uses python3
import sys

def pisano(m):
    prev = 0
    curr = 1
    if m == 1:
        return 1
    if m == 2:
        return 3
    for i in range(3,m*m+2):
        s = prev + curr
        prev = curr%m
        curr = s%m
        #print(s)
        #print(prev,curr)
        if prev == 0 and curr == 1:
            return (i-2)


def fibonacci_huge_naive(n, m, flag):
    
    get_pis = pisano(m)
    #print(get_pis)
    ran = n % get_pis
    #print(ran)
    if ran == 0:
        return 0
    if ran == 1 or ran == 2:
        return 0
    s = 0
    a = 1
    b = 1
    for i in range(3,ran+1):
        s = a + b
        a = b
        b = s
    #print(s)
    if flag == 1:
        return s%m
    return s-1



def fibonacci_partial_sum(from_,to):
    a = fibonacci_huge_naive(from_+1,10,0)
    b = fibonacci_huge_naive(to+2,10,0)+10
    if from_ == 0:
        a = 0
    if to == 0:
        b = 0
    if from_ == to and from_ !=0 and to != 0:
        return fibonacci_huge_naive(from_,10,1)
    # print(a)
    # print(b)
    return (b-a)%10

# res = fibonacci_partial_sum(1,2)
# print(res)

# def fibonacci_partial_sum_naive(from_, to):
#     _sum = 0

#     current = 0
#     _next  = 1

#     for i in range(to + 1):
#         if i >= from_:
#             _sum += current

#         current, _next = _next, current + _next

#     return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
