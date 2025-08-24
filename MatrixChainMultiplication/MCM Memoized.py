def solve(i, j):
    if i >= j:
        return 0

    m = float("inf")
    if (i, j) in dp:
        return dp[(i, j)]

    for k in range(i, j):
        tempAns = solve(i, k) + solve(k + 1, j) + arr[i - 1] * arr[k] * arr[j]
        m = min(m, tempAns)

    dp[(i, j)] = m
    return m


if __name__ == "__main__":
    arr = [40, 20, 30, 10, 30]
    n = len(arr)

    dp = {}

    res = solve(1, n - 1)
    print(f"The minimum cost of matrix chain multiplication is {res}")
