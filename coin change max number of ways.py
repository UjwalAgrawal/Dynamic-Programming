def maxNumberOfWays(coins, target):
    nc = len(coins)
    dp = [[0] * (target + 1) for i in range(nc+1)]

    for i in range(nc + 1):
        dp[i][0] = 1

    for i in range(1, nc+1):
        for j in range(1, target + 1):
            if(coins[i-1] <= j):
                dp[i][j] = dp[i][j-coins[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    return dp[nc][target]


if __name__ == '__main__':
    coins = [1,2,3]
    target = 5

    res = maxNumberOfWays(coins, target)
    print(f"There are {res} ways.")