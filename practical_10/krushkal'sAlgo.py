def find(parent, vertex):
    while parent[vertex] != vertex:
        vertex = parent[vertex]
    return vertex


def union(parent, u, v):
    u = find(parent, u)
    v = find(parent, v)

    parent[v] = u


def kruskal(edges, n):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = list(range(n + 1))
    mst = []
    total_cost = 0

    for u, v, w in edges:

        # Check if adding edge creates a cycle
        if find(parent, u) != find(parent, v):

            mst.append((u, v, w))
            total_cost += w

            union(parent, u, v)

            # MST has n-1 edges
            if len(mst) == n - 1:
                break

    print("MST:", mst)
    print("Total cost:", total_cost)


# Number of vertices
n = int(input("Enter number of vertices: "))

# Number of edges
e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u = int(input("Enter first vertex: "))
    v = int(input("Enter second vertex: "))
    w = int(input("Enter weight: "))

    edges.append((u, v, w))

kruskal(edges, n)