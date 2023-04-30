def fibonacci_number(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    s = 0
    a = 1
    b = 1
    for i in range(3,n+1):
        s = a + b
        a = b
        b = s
    return s

'''
res = fibonacci_number(37)
print(res)
'''

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
