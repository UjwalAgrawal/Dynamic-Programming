if __name__ == '__main__':
    arr = [2,3,7,8,10]
    target = 14

    # arr = list(map(int, input("Enter the array: ").split()))
    # target = int(input("Enter target value: "))

    n = len(arr)

    dp = [[False] * (target+1) for _ in range(n+1)]  #initilize with None 

    for i in range(n+1):
        dp[i][0] = True
    
    # for i in range(n+1):
    #     print(dp[i])
    
    for i in range(n+1):
        for j in range(target+1):
            if(arr[i-1] <= j):
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    # print()
    # for i in range(n+1):
    #     print(dp[i])
    
    print(f"Is Subest possible: {dp[n][target]}")
    