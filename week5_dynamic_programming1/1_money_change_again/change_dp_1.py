import math
def change(money):
    # write your code here
    min_num_coins = [0]
    coins = [1,3,4]
    for m in range(1,money+1):
        min_num_coins.append(math.inf)
        for coin in coins:
            if m>=coin:
                num_coins = min_num_coins[m-coin]+1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    #print(min_num_coins)
    return min_num_coins[money]


# res = change(34)
# print(res)

if __name__ == '__main__':
    m = int(input())
    print(change(m))
