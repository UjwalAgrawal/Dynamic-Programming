if __name__ == '__main__':
    # arr  = [1,1,2,3]
    # diff = 1

    arr = list(map(int, input("Enter the array elements: ").split()))
    diff = int(input("Enter the difference: "))

    s = sum(arr)
    n = len(arr)

    if((diff+s)%2):
        print("Number of subest with given difference is : 0")
    
    else:
        target = (diff + s)//2

        dp = [[0] * (target+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                if(arr[i-1] <= j):
                    dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        print(f"Number of subest with given difference is : {dp[n][target]}")