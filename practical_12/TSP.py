def tsp(graph, n):
    dp = {}

    def solve(mask, pos):
        if mask == (1 << n) - 1:
            return graph[pos][0]

        if (mask, pos) in dp:
            return dp[(mask, pos)]

        ans = float('inf')

        for city in range(n):
            if not (mask & (1 << city)):
                cost = graph[pos][city] + solve(
                    mask | (1 << city), city
                )
                ans = min(ans, cost)

        dp[(mask, pos)] = ans
        return ans

    return solve(1, 0)


n = int(input("Enter number of cities: "))

graph = []
print("Enter the cost matrix row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

print("Minimum travelling cost:", tsp(graph, n))