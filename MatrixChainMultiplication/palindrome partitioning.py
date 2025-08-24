def solve(i, j):
    if (i, j) in dp:
        return dp[(i, j)]

    if i >= j:
        return 0

    if arr[i : j + 1] == arr[i : j + 1][::-1]:
        return 0

    mini = float("inf")

    for k in range(i, j):
        if (i, k) in dp:
            left = dp[(i, k)]
        else:
            left = solve(i, k)
        if (k + 1, j) in dp:
            right = dp[(k + 1, j)]
        else:
            right = solve(k + 1, j)
        tempAns = left + 1 + right
        mini = min(tempAns, mini)

    dp[(i, j)] = mini
    return mini


if __name__ == "__main__":
    arr = "malayalan"
    n = len(arr)
    dp = {}

    res = solve(0, n - 1)

    print(
        f"The minimum number of partitions required to make all the partitions palindrome is {res}"
    )
