def equalSumPartition(arr, target):
    n = len(arr)

    dp = [[False] * (target+1) for _ in range(n+1)]  #initilize with None 

    for i in range(n+1):
        dp[i][0] = True
    
    # for i in range(n+1):
    #     print(dp[i])
    
    for i in range(1,n+1):
        for j in range(1,target+1):
            if(arr[i-1] <= j):
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]

if __name__ == '__main__':
    arr = [1,5,5,11,6]

    # arr = list(map(int, input("Enter the array: ").split()))

    n = len(arr)

    s = sum(arr)
    if(s%2):
        print("Equal sum partitioning is not possible")
    else:
        flag = equalSumPartition(arr, s//2)
        if(flag):
            print("Equal sum partition is possible")
        else:
            print("Equal sum partition is not possible")

    