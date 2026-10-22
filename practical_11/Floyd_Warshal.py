
def floyd_warshall(D, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]

    print("Shortest Distance Matrix:")
    for i in range(V):
        print(D[i])


INF = float('inf')

D = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

V = 4
floyd_warshall(D, V)
