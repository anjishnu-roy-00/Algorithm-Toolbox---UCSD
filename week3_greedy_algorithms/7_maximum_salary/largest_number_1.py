from itertools import permutations



def largest_number_efficient(numbers):
    num_string = []
    for elem in numbers:
        num_string.append(str(elem))
    new = []
    max_str = ""
    while num_string:
        max_str = num_string[0]
        for elem in num_string:
            if  elem+max_str > max_str+elem:
                max_str = elem
        new.append(max_str)
        num_string.remove(max_str)
    ret = ""
    for elem in new:
        ret += elem
    return ret


# L = [1,2,3,456,789,1200]
# res = largest_number_efficient(L)
# print(res)
        


# def largest_number_naive(numbers):
#     numbers = list(map(str, numbers))

#     largest = 0

#     for permutation in permutations(numbers):
#         largest = max(largest, int("".join(permutation)))

#     return largest


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(largest_number_efficient(input_numbers))
