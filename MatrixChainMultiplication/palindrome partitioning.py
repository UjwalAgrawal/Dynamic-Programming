def solve(arr, i, j):
    if (dp[i][j] != -1):
        return dp[i][j]
    if (i >= j):
        return (0)
    if arr[i:j+1] == arr[i:j+1][::-1]:
        return (0)
    m = float('inf')
    for k in range(i, j):
        if(dp[i][k] != -1):
            left = dp[i][k]
        else:
            left = solve(arr, i , k)
        if(dp[k+1][j] != -1):
            right = dp[k+1][j]
        else:
            right = solve(arr, k+1 , j)
        tempAns = left + 1 + right
        m = min(tempAns, m)
    dp[i][j] = m
    return (m)


if __name__ == '__main__':
    arr = 'malayalan'
    n = len(arr)

    global dp
    dp = [[-1] * (n+1) for _ in range(n+1)]

    res = solve(arr, 0, n-1)

    print(f'The minimum number of partitions required to make all the partitions palindrome is {res}')
