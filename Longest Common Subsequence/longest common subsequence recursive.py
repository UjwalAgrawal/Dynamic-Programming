def LCS(x, y, n, m):
    if (n == 0 or m == 0):
        return 0
    if (x[n-1] == y[m-1]):
        return (1 + LCS(x, y, n-1, m-1))
    else:
        return max(LCS(x, y, n-1, m), LCS(x, y, n, m-1))


x = input("Enter first string: ")
y = input("Enter second string: ")

n = len(x)
m = len(y)

res = LCS(x, y, n, m)
print(f"Longest common subsequence size is {res}")
