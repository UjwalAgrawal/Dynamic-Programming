def solve(arr, i, j):
    if (i >= j):
        return (0)

    m = float('inf')
    if(dp[i][j] != -1):
        return dp[i][j]

    for k in range(i, j):
        tempAns = solve(arr, i, k) + solve(arr, k+1, j) + \
            arr[i-1]*arr[k]*arr[j]
        m = min(m, tempAns)

    dp[i][j] = m
    return (m)


if __name__ == '__main__':
    arr = [40, 20, 30, 10, 30]
    n = len(arr)

    global dp
    dp = [[-1] * (n+1) for _ in range(n+1)]

    res = solve(arr, 1, n-1)
    print(f'The minimum cost of matrix chain multiplication is {res}')
