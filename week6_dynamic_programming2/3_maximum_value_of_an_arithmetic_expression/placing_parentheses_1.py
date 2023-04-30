import numpy 
import math 

def evaluate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def min_max(M, m, i, j, op):
    min_ = math.inf
    max_ = -math.inf
    for k in range(i, j):
        a = evaluate(M[i][k], M[k+1][j], op[k])
        b = evaluate(M[i][k], m[k+1][j], op[k])
        c = evaluate(m[i][k], M[k+1][j], op[k])
        d = evaluate(m[i][k], m[k+1][j], op[k])
        min_ = min(min_, a, b, c, d)
        max_ = max(max_, a, b, c, d)
    return min_, max_

def maximum_value(dataset):
    # write your code here
    op = []
    nums = []
    for elem in dataset:
        if elem in ['+','-','*']:
            op.append(elem)
        else:
            nums.append(int(elem))
    n = len(nums)
    # print(n)
    # print(op)
    # print(nums)
    mins = numpy.empty((n,n))
    maxs = numpy.empty((n,n))
    for i in range(n):
        mins[i][i] = nums[i]
        maxs[i][i] = nums[i]
    for s in range(1,n):
        i = 0
        for j in range(s,n):
            mins[i][j], maxs[i][j] = min_max(maxs,mins,i,j,op)
            i+=1

    return int(maxs[0][n-1])


# str = '5-8+7*4-8+9'
# str = '3+2*4'
# res = maximum_value(str)
# print(res)

if __name__ == "__main__":
    print(maximum_value(input()))
