from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    sorted_array = sorted(segments,key=lambda c: c[1])
    #print(sorted_array)
    point = 0
    # for elem in sorted_array:
    #     if point<elem[0] or point>elem[1]:
    #         point = elem[1]
    #         points.append(point)
    # print(points)
    # return points
    while sorted_array:
        point = sorted_array.pop(0)[1]
        points.append(point)

        for s in sorted_array[:]:
            if s[0] <= point <= s[1]:
                sorted_array.remove(s)
    
    return points

# L=[(4,7),(1,3),(4,5),(5,6)]
# L=[(1,3),(2,5),(3,6)]
# L=[(4,7),(1,3),(4,5),(5,6),(7,9),(3,6)]
# res = optimal_points(L)
# print(res)

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
