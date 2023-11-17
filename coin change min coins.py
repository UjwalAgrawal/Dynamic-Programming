import sys


def minNumberOfCoins(coins, total):
    n = len(coins)

    dp = [[None] * (total + 1) for _ in range(n+1)]

    for j in range(total+1):
        dp[0][j] = sys.maxsize - 1
    for i in range(1, n+1):
        dp[i][0] = 0
    for j in range(1, total+1):
        if (j % coins[0] == 0):
            dp[1][j] = j//coins[0]
        else:
            dp[1][j] = sys.maxsize - 1
    for i in range(2, n+1):
        for j in range(1, total+1):
            if (coins[i-1] <= j):
                dp[i][j] = min(1 + dp[i][j - coins[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return (dp[n][total])


coins = [1, 2, 3]
total = 5

res = minNumberOfCoins(coins, total)
print("Minimum number of coins : ",res)
