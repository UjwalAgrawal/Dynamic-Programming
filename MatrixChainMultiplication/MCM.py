# Given the dimension of a sequence of matrices in an array arr[], 
# where the dimension of the ith matrix is (arr[i-1] * arr[i]),
# the task is to find the most efficient way to multiply these matrices together such that 
# the total number of element multiplications is minimum.

def solve(arr, i, j):
    if (i >= j):
        return (0)
    m = float('inf')
    for k in range(i, j):
        tempAns = solve(arr, i, k) + solve(arr, k+1, j) + \
            arr[i-1]*arr[k]*arr[j]
        m = min(tempAns, m)
    return (m)


if __name__ == '__main__':
    arr = [40, 20, 30, 10, 30]
    n = len(arr)-1
    res = solve(arr, 1, n)
    print(f'The minimum cost of matrix chain multiplication is {res}')
