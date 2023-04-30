def change(money):
    # write your code here
    den = [10,5,1]
    i = 0
    a = 0
    s = 0
    while money > 0:
        a = int(money/den[i])
        money = money%den[i]
        s+=a
        i+=1
    return s

'''
res = change(2)
print(res)
'''


if __name__ == '__main__':
    m = int(input())
    print(change(m))