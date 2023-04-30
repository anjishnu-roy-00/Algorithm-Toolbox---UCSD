import math

# reference for the math: https://stackoverflow.com/a/54609093

def optimal_summands(n):
    summands = []
    # write your code here
    sum=0
    if n<=2:
        summands.append(n)
        return summands
    k = int((math.sqrt(8*n+1)-1)/2)
    #print(k)
    summands = [i for i in range(1,k)]
    #print(summands)
    sum = int(n - (k*(k-1)/2))
    summands.append(sum)

    return summands

# res = optimal_summands(222)
# print(res)

if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
