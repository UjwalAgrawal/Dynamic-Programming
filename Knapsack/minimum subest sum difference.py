#divide the partition into two sets whose difference of sums is minimum and print their difference

if __name__ == '__main__':
    # arr = [1,2,7]
    arr = list(map(int, input("Enter the array elements: ").split()))
    r = sum(arr) #range of the subsets i.e. the total of the set numbers
    n = len(arr)

    #initialization of the dp matrix
    dp = [[False ]* (r + 1) for i in range(n+1)]

    for i in range(n+1): 
        dp[i][0] = True #since 0 is always possible if no item is selected in the subset
    
    for i in range(1,n+1):
        for j in range(1,r+1):
            if(arr[i-1]<=j):
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    #the difference is always going to be less than half of the range
    newList = [i for i in range(r//2) if dp[n][i]] #sums that are possible from the given array
    # print(dp)
    # print(newList)
    print(f"The minimum difference between the two subset sums is : {r - 2*newList[-1]}")
