def gcd(a, b):
    if b==0:
        return a
    r = a%b
    a = b
    b = r
    return gcd(a,b)



if __name__ == "__main__":
    a, b = map(int, input().split())
    c = a
    d = b
    a = max(c,d)
    b = min(c,d)
    print(gcd(a, b))
