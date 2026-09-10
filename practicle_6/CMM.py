def matrixChain(arr, n):

    m = [[0 for j in range(n)] for i in range(n)]

    for T in range(2, n):
        for i in range(0, n - T):

            j = i + T

            m[i][j] = float('inf')

            for k in range(i + 1, j):

                cost = (m[i][k]
                        + m[k][j]
                        + arr[i] * arr[k] * arr[j])

                if cost < m[i][j]:
                    m[i][j] = cost

    return m[0][n - 1]


n = int(input("Enter number of dimensions: "))

arr = list(map(int, input("Enter dimensions: ").split()))

result = matrixChain(arr, n)

print("Minimum number of multiplications =", result)