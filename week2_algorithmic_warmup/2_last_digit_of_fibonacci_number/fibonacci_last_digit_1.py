def fibonacci_last_digit(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    s = 0
    a = 1
    b = 1
    for i in range(3,n+1):
        s = a + b
        a = b%10
        b = s%10
    return s%10

'''
res = fibonacci_last_digit(91239)
print(res)
'''

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
