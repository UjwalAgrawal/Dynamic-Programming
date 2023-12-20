dp = {}

def knapsack(weights, values, totalCapacity, n):
    if(n==0 or totalCapacity==0):
        return(0)
    if((n, totalCapacity) in dp):
        return dp[(n, totalCapacity)]
    if(weights[n-1] <= totalCapacity):
        dp[(n, totalCapacity)] = max(
            values[n-1] + knapsack(weights, values, totalCapacity - weights[n-1], n-1), knapsack(weights, values, totalCapacity, n-1)
        )
    else:
        dp[(n, totalCapacity)] = knapsack(weights, values, totalCapacity, n-1)
    return dp[(n, totalCapacity)]




weights = list(map(int, input("Enter weights: ").split()))
values = list(map(int, input("Enter values: ").split()))
totalCapacity = int(input("Enter knapsack capacity: "))
maxValue = knapsack(weights, values, totalCapacity, len(weights))
print(maxValue)




