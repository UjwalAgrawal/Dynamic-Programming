if __name__ == '__main__':
    # weights = list(map(int, input("Enter weights: ").split()))
    # values = list(map(int, input("Enter values: ").split()))
    # totalCapacity = int(input("Enter knapsack capacity: "))

    weights = [1,2,3,4]
    values = [2,3,5,7]
    totalCapacity = 6

    n = len(weights)
    dp = [[-1]*(totalCapacity+1) for _ in range(n+1)]
    # print(dp)
    for i in range(n+1):
        for j in range(totalCapacity+1):
            if(i==0 or j==0):
                dp[i][j] = 0
                # print("\n",dp)
    
    for i in range(1,n+1):   #number of items
        for j in range(1,totalCapacity+1):  #capacity at each iteration
            if(weights[i-1]<=j):
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    for i in dp:
        print(i)
    print(dp[-1][-1])


