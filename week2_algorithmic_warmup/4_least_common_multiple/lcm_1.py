def hcf(a,b):
    if b==0:
        return a
    r = a%b
    a = b
    b = r
    return hcf(a,b)  
def lcm(a, b):
    c = max(a,b)
    d = min(a,b)
    gcd = hcf(c,d)
    lcm = int(c*d/gcd)
    return lcm


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

