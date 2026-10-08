# Take number of vertices
n = int(input("Enter number of vertices: "))

graph = {}

# Create graph
for i in range(n):
    graph[i] = []

# Take number of edges
e = int(input("Enter number of edges: "))

# Take edges
for i in range(e):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))

    graph[u].append(v)
    graph[v].append(u)

print("Graph:", graph)

# BFS
start = int(input("Enter starting vertex for BFS: "))

visited = []
queue = [start]

while queue:
    vertex = queue.pop(0)

    if vertex not in visited:
        visited.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)

print("BFS:", visited)

# DFS
start = int(input("Enter starting vertex for DFS: "))

visited = []
stack = [start]

while stack:
    vertex = stack.pop()

    if vertex not in visited:
        visited.append(vertex)

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                stack.append(neighbour)

print("DFS:", visited)