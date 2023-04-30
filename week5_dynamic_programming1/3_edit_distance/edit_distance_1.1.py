def edit_distance(first_string, second_string):
    dist = [[0 for x in range(len(second_string)+1)] for y in range(len(first_string)+1)]
    #print(dist)
    for i in range(0,len(first_string)+1):
        dist[i][0] = i
    for j in range(1,len(second_string)+1):
        dist[0][j] = j
    for i in range(1,len(first_string)+1):
        for j in range(1,len(second_string)+1):
            if first_string[i-1] != second_string[j-1]:
                dist[i][j] = min(1+dist[i-1][j],min(1+dist[i][j-1],1+dist[i-1][j-1]))
            else:
                dist[i][j] = dist[i-1][j-1]
    # for elem in dist:
    #     print(elem)
    return dist[len(first_string)][len(second_string)]

# a = 'editing'
# b = 'distance'
# # a = 'b'
# # b = 'a'
# # a = 'short'
# # b = 'ports'
# # a = 'ab'
# # b = 'ba'
# # a = 'abba'
# # b ='baba'
# res = edit_distance(a,b)
# print(res)

if __name__ == "__main__":
    print(edit_distance(input(), input()))
