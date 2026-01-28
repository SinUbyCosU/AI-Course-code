import sys

# ---------------------------------------------------------
# LAYER 1: THE ARCHITECT (Parsing)
# ---------------------------------------------------------
def load_maze(filename):
    """
    Reads the file and returns:
    - grid: A list of lists (2D array) representing rows.
    - start: (row, col) tuple.
    - goal: (row, col) tuple.
    """
    with open(filename) as f:
        contents = f.read().splitlines()

    height = len(contents)
    width = max(len(line) for line in contents)
    
    grid = []
    start = None
    goal = None

    for r in range(height):
        row_data = []
        for c in range(width):
            try:
                char = contents[r][c]
            except IndexError:
                char = " " # Handle uneven lines

            row_data.append(char)
            
            if char == "A":
                start = (r, c)
            elif char == "B":
                goal = (r, c)
        
        grid.append(row_data)

    if start is None or goal is None:
        raise Exception("Maze must have Start (A) and Goal (B)")

    return grid, start, goal

# ---------------------------------------------------------
# LAYER 2: THE NAVIGATOR (Neighbors)
# ---------------------------------------------------------
def get_neighbors(state, grid):
    """
    Returns a list of (action, (r, c)) for valid moves.
    state: (row, col)
    """
    row, col = state
    height = len(grid)
    width = len(grid[0])
    
    candidates = [
        ("up",    (row - 1, col)),
        ("down",  (row + 1, col)),
        ("left",  (row, col - 1)),
        ("right", (row, col + 1))
    ]

    result = []
    for action, (r, c) in candidates:
        # Check bounds
        if 0 <= r < height and 0 <= c < width:
            # Check for walls
            if grid[r][c] != "#":
                result.append((action, (r, c)))
    
    return result

# ---------------------------------------------------------
# LAYER 3: THE BRAIN (Solver Loop)
# ---------------------------------------------------------
def solve_maze(grid, start, goal):
    """
    Uses Stack (DFS) logic to find a path.
    Returns: A list of coordinates [(r,c), (r,c)...] representing the path.
    """
    
    # We need to store 'parent' info to reconstruct the path later.
    # Structure: { child_state: parent_state }
    came_from = {start: None}
    
    # The Frontier: A list of states to explore
    frontier = [start]
    
    # The Explored Set: To avoid loops
    explored = set()

    print("Starting Search...")

    while len(frontier) > 0:
        # STACK LOGIC: Pop from the end (LIFO)
        current = frontier.pop()
        
        # Check Goal
        if current == goal:
            print(f"Goal Found at {current}!")
            return reconstruct_path(came_from, current)

        # Add to Explored
        explored.add(current)

        # Get Neighbors
        for action, neighbor in get_neighbors(current, grid):
            if neighbor not in explored and neighbor not in came_from:
                # Add to frontier
                frontier.append(neighbor)
                # Record parent so we can backtrack
                came_from[neighbor] = current

    print("No solution found.")
    return None

# ---------------------------------------------------------
# LAYER 4: THE ARTIST (Backtracking & Printing)
# ---------------------------------------------------------
def reconstruct_path(came_from, current):
    """
    Backtracks from Goal -> Start using the 'came_from' dictionary.
    """
    path = []
    while current is not None:
        path.append(current)
        current = came_from[current]
    
    path.reverse() # We want Start -> Goal
    return path

def print_result(grid, path):
    """
    Prints the grid with the path marked as '*'.
    """
    # Convert path list to a set for fast lookup
    path_set = set(path) if path else set()

    print("\n--- SOLVED MAZE ---")
    for r, row in enumerate(grid):
        line_str = ""
        for c, char in enumerate(row):
            if (r, c) in path_set and char not in ("A", "B"):
                line_str += "*" # Draw Path
            elif char == "#":
                line_str += "█" # Draw Wall (prettier)
            else:
                line_str += char
        print(line_str)
    print("-------------------")


# ---------------------------------------------------------
# MAIN EXECUTION
# ---------------------------------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simple_maze.py <maze_file>")
        sys.exit(1)

    filename = sys.argv[1]
    
    # 1. Load
    grid, start, goal = load_maze(filename)
    print(f"Maze Loaded. Start: {start}, Goal: {goal}")

    # 2. Solve
    path = solve_maze(grid, start, goal)

    # 3. Print
    if path:
        print(f"Path Length: {len(path)} steps.")
        print_result(grid, path)
