dp = {}

def LCS(x, y, m, n):
    if (n == 0 or m == 0):
        return 0
    if((m,n) in dp):
        return dp[(m,n)]
    if (x[m-1] == y[n-1]):
        dp[(m,n)] =  (1 + LCS(x, y, m-1, n-1))
    else:
        dp[(m,n)] = max(LCS(x, y, m-1, n), LCS(x, y, m, n-1))
    return dp[(m,n)]


x = input("Enter first string: ")
y = input("Enter second string: ")

m = len(x)
n = len(y)
# dp = [[None] * (n+1) for _ in range(m+1)]


res = LCS(x, y, m, n)
print(f"Longest common subsequence size is {res}")
