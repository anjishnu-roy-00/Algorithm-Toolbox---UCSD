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
        return 0
    s = 0
    a = 1
    b = 1
    for i in range(3,ran+1):
        s = a + b
        a = b
        b = s
    print(s)
    return ((s%m+10)-1)%10



def fibonacci_sum(n):
    if n==0:
        return 0
    return fibonacci_huge_naive(n+2,10)


res = fibonacci_sum(100)
print(res)

# def fibonacci_sum(n):
#     if n <= 1:
#         return n

#     previous, current, _sum = 0, 1, 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         _sum += current

#     return _sum % 10


# if __name__ == '__main__':
#     n = int(input())
#     print(fibonacci_sum(n))
