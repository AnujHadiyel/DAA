# =========================================================
# A* SEARCH ALGORITHM
# =========================================================

def astar(start, goal, get_neighbors, guess):

    frontier = [[guess(start), 0, start, [start]]]

    visited = []
    explored_count = 0

    while len(frontier) > 0:

        best = 0

        # Find node with smallest f value
        for i in range(1, len(frontier)):

            if frontier[i][0] < frontier[best][0]:
                best = i

        # Remove best node
        node = frontier.pop(best)

        f, g, place, path = node

        # Skip already visited nodes
        if place in visited:
            continue

        visited.append(place)
        explored_count = explored_count + 1

        # Goal reached
        if place == goal:
            return path, explored_count

        # Explore neighbours
        for nxt in get_neighbors(place):

            if nxt in visited:
                continue

            new_g = g + 1
            new_f = new_g + guess(nxt)

            frontier.append(
                [new_f, new_g, nxt, path + [nxt]]
            )

    return None, explored_count


print("A* is ready to use")


# =========================================================
# PART A - GRID
# =========================================================

grid = [
    ".............",
    "......###....",
    "S............G",
    "......###....",
    "............."
]


# =========================================================
# FIND START AND GOAL
# =========================================================

def find(letter):

    for r in range(len(grid)):

        for c in range(len(grid[r])):

            if grid[r][c] == letter:
                return (r, c)

    return None


start = find("S")
goal = find("G")

rows = len(grid)
cols = len(grid[0])


print("Start is at:", start)
print("Goal is at:", goal)
print()


# Display grid
for line in grid:
    print(" ".join(line))


# =========================================================
# GRID NEIGHBOURS
# =========================================================

def grid_neighbors(box):

    r, c = box

    out = []

    # Up, Down, Left, Right
    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]:

        nr = r + dr
        nc = c + dc

        # Check boundaries
        if 0 <= nr < rows and 0 <= nc < cols:

            # Check wall
            if grid[nr][nc] != "#":

                out.append((nr, nc))

    return out


print(
    "From the start",
    start,
    "the robot can step to:",
    grid_neighbors(start)
)


# =========================================================
# GRID HEURISTICS
# =========================================================

# Heuristic 1: Zero heuristic
def grid_zero(box):

    return 0


# Heuristic 2: Manhattan distance
def grid_manhattan(box):

    r, c = box

    return abs(r - goal[0]) + abs(c - goal[1])


print(
    "Manhattan guess from the start:",
    grid_manhattan(start)
)


# =========================================================
# SOLVE GRID USING ZERO HEURISTIC
# =========================================================

path_zero, explored_zero = astar(
    start,
    goal,
    grid_neighbors,
    grid_zero
)


# =========================================================
# SOLVE GRID USING MANHATTAN HEURISTIC
# =========================================================

path_manh, explored_manh = astar(
    start,
    goal,
    grid_neighbors,
    grid_manhattan
)


# =========================================================
# GRID RESULTS
# =========================================================

print()
print("Guess              Path length       Boxes explored")
print("-" * 55)


print(
    "Zero (no hint)     ",
    len(path_zero) - 1,
    "steps             ",
    explored_zero
)


print(
    "Manhattan           ",
    len(path_manh) - 1,
    "steps             ",
    explored_manh
)


print()

print(
    "Same shortest path. "
    "But Manhattan explores fewer boxes."
)


# =========================================================
# DISPLAY GRID PATH
# =========================================================

def show_grid_path(path):

    path_set = set(path)

    for r in range(rows):

        line = ""

        for c in range(cols):

            if (r, c) == start:

                line += " S "

            elif (r, c) == goal:

                line += " G "

            elif (r, c) in path_set:

                line += " * "

            else:

                line += " " + grid[r][c] + " "

        print(line)


print()
print("The robot's path:")
print()

show_grid_path(path_manh)


# =========================================================
# PART B - 8 PUZZLE
# =========================================================

goal_state = "123456780"
start_state = "123450678"


# =========================================================
# DISPLAY PUZZLE
# =========================================================

def show_puzzle(state):

    for r in range(3):

        row = state[r * 3 : r * 3 + 3]

        row = row.replace("0", "_")

        print("   " + "  ".join(row))


print()
print("Start:")
show_puzzle(start_state)

print()

print("Goal:")
show_puzzle(goal_state)


# =========================================================
# 8-PUZZLE NEIGHBOURS
# =========================================================

def puzzle_neighbors(state):

    out = []

    # Find empty space
    zero = state.index("0")

    # Convert index to row and column
    r = zero // 3
    c = zero % 3

    # Up, Down, Left, Right
    for dr, dc in [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]:

        nr = r + dr
        nc = c + dc

        # Stay inside 3x3 puzzle
        if 0 <= nr < 3 and 0 <= nc < 3:

            new_zero = nr * 3 + nc

            tiles = list(state)

            # Swap empty space with neighbouring tile
            tiles[zero], tiles[new_zero] = (
                tiles[new_zero],
                tiles[zero]
            )

            out.append("".join(tiles))

    return out


print()
print(
    "From the start, we can reach these arrangements:"
)

for s in puzzle_neighbors(start_state):

    print("  ", s)


# =========================================================
# 8-PUZZLE HEURISTICS
# =========================================================

# Heuristic 1: No hint
def puzzle_zero(state):

    return 0


# Heuristic 2: Wrong tiles
def puzzle_wrong_tiles(state):

    count = 0

    for i in range(9):

        # Ignore empty space
        if state[i] != "0":

            if state[i] != goal_state[i]:

                count = count + 1

    return count


print()
print(
    "Wrong tiles in the start:",
    puzzle_wrong_tiles(start_state)
)


# =========================================================
# SOLVE 8-PUZZLE USING ZERO HEURISTIC
# =========================================================

ans_zero, count_zero = astar(
    start_state,
    goal_state,
    puzzle_neighbors,
    puzzle_zero
)


# =========================================================
# SOLVE 8-PUZZLE USING WRONG-TILES HEURISTIC
# =========================================================

ans_smart, count_smart = astar(
    start_state,
    goal_state,
    puzzle_neighbors,
    puzzle_wrong_tiles
)


# =========================================================
# 8-PUZZLE RESULTS
# =========================================================

print()
print(
    "Guess              Moves to solve       Arrangements explored"
)

print("-" * 65)


print(
    "Zero (no hint)     ",
    len(ans_zero) - 1,
    "moves                ",
    count_zero
)


print(
    "Wrong-tiles         ",
    len(ans_smart) - 1,
    "moves                ",
    count_smart
)


print()

print(
    "Same number of moves. "
    "But the smart guess can explore fewer arrangements."
)


# =========================================================
# SHOW PUZZLE SOLUTION STEP BY STEP
# =========================================================

print()
print("Solving the puzzle, one slide at a time:")
print()


for step, state in enumerate(ans_smart):

    print("Move", step, ":")

    show_puzzle(state)

    print()