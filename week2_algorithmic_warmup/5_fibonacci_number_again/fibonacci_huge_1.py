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


def fibonacci_huge_naive(n, m):
    
    get_pis = pisano(m)
    #print(get_pis)
    ran = n % get_pis
    #print(ran)
    if ran == 0:
        return 0
    if ran == 1 or ran == 2:
        return 1
    s = 0
    a = 1
    b = 1
    for i in range(3,ran+1):
        s = a + b
        a = b
        b = s
    return s%m







res = fibonacci_huge_naive(10,10)
print(res)



# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     print(fibonacci_huge_naive(n, m))
