if __name__ == '__main__':
    a = input("Enter first string: ")
    b = input("Enter second string: ")

    m = len(a)
    n = len(b)

    dp = [[None] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = 0
    for j in range(n+1):
        dp[0][j] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if (a[i-1] == b[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(f'Is the first string present in second string subsequence: {
          dp[m][n] == m}')
