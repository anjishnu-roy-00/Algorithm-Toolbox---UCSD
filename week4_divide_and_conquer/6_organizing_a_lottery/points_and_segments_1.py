from sys import stdin

def arrange(starts,ends,points):
    start_label = 0
    point_label = 1
    end_label = 2

    point_counts = [0]*len(points)
    point_map = {}

    combined=[]
    for s in starts:
        combined.append((s,start_label))
    for e in ends:
        combined.append((e,end_label))
    for index,p in enumerate(points):
        combined.append((p,point_label))
        if (p not in point_map):
            point_map[p] = [index]
        else:
            point_map[p].append(index)
    
    sorted_array = sorted(combined,key=lambda c: (c[0],c[1]))
    count = 0
    for item in sorted_array:
        if item[1] == start_label:
            count+=1
        elif item[1] == end_label:
            count-=1
        elif item[1] == point_label:
            indices = point_map[item[0]]
            for i in indices:
                point_counts[i] = count
    
    return point_counts
# def points_cover_naive(starts, ends, points):
#     assert len(starts) == len(ends)
#     count = [0] * len(points)

#     for index, point in enumerate(points):
#         for start, end in zip(starts, ends):
#             if start <= point <= end:
#                 count[index] += 1

#     return count



if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = arrange(input_starts, input_ends, input_points)
    print(*output_count)
