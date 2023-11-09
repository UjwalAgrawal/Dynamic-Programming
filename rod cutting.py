#solved using unbounded knapsack
#instead of using a matrix, dictionary can be used. Though both of them will help retrive data in O(1) time.

def maxRodCut(lengths, price):
    n = len(lengths)
    dp = [[None] * (n+1)] * (n+1)
    for i in range(n+1):
        dp[0][i] = 0        # first row will be all 0's as for zero cuts price is 0
        dp[i][0] = 0        # first column wll be all 0's as we can not have rod length of 0
    
    for i in range(n+1):
        for j in range(n+1):
            if(lengths[i-1]<=j):
                #since we can cut the rod for same length as many times as we want, we dont decrease the count when selected
                dp[i][j] = max(price[i-1] + dp[i][j-lengths[i-1]], dp[i-1][j]) 
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][n]



if __name__ == '__main__':
    n = 8
    price = [1,5,8,9,10,17,17,20]
    lengths = list(range(1, n+1))


    maxCutValue = maxRodCut(lengths, price)
    print(maxCutValue)
