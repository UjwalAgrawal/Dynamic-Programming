if __name__ == "__main__":
    x = input('Starting string: ')
    y = input('Target string: ')

    m = len(x)
    n = len(y)

    #first find LCS (i.e. that part of the string which is in same sequence in both start and target string)

    dp = [[None] * (n+1) for _ in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 0
    for i in range(n+1):
        dp[0][i] = 0

    for i in range(1,m+1):
        for j in range(1, n+1):
            if(x[i-1] == y[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    print(f'Length of longest common subsequence is {dp[m][n]}')

    # apart from LCS all other characters need to be deleted
    print(f'Number of deletions required is {m - dp[m][n]}')

    print(f'number of insertions required is {n - dp[m][n]}')

