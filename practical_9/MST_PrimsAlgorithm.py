def prims(graph, n):
    visited = [False] * n
    visited[0] = True
    total_cost = 0

    for count in range(n - 1):
        minimum = float('inf')
        u = -1
        v = -1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if graph[i][j] != 0 and not visited[j]:
                        if graph[i][j] < minimum:
                            minimum = graph[i][j]
                            u = i
                            v = j

        if v == -1:
            print("Graph is not connected")
            return

        print(u, "-", v, ":", minimum)
        total_cost += minimum
        visited[v] = True

    print("Total cost:", total_cost)


graph = [
    [0, 2, 0, 6],
    [2, 0, 3, 8],
    [0, 3, 0, 7],
    [6, 8, 7, 0]
]

prims(graph, 4)