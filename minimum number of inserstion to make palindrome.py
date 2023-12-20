if __name__ == '__main__':
    a = input("Enter the string: ")
    b = a[::-1]

    n = len(a)

    dp = [[None] * (n+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[0][i] = 0
        dp[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,n+1):
            if(a[i-1]==b[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    print(f'Minimum number of instertions to make the string palindromic is {n - dp[n][n]}')
    