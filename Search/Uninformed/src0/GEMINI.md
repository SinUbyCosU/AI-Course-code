# Maze Solver

This project is a Python-based application designed to solve mazes using search algorithms. It reads a text-based maze representation, finds a path from a starting point (A) to a goal (B), and outputs the solution both to the console and as an image file.

## Project Overview

The core logic resides in `maze.py`, which implements a generic search algorithm.
*   **Current Algorithm:** Depth-First Search (DFS) via the `StackFrontier` class.
*   **Alternative Algorithm:** Breadth-First Search (BFS) is implemented in `QueueFrontier` but not active by default.
*   **Visualization:** Uses the `pillow` library to generate an image (`maze.png`) of the solved maze, highlighting the path and explored states.

## Prerequisites

*   **Python 3.x**
*   **Pillow** (Python Imaging Library)

## Installation

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the maze solver, provide a maze text file as a command-line argument:

```bash
python maze.py maze1.txt
```

You can replace `maze1.txt` with any valid maze file (e.g., `maze2.txt`, `maze3.txt`).

## Input Format

Maze files are text files where:
*   `#`: Represents a **Wall**.
*   `A`: Represents the **Start** position.
*   `B`: Represents the **Goal** position.
*   ` ` (Space): Represents an **Open Path**.

**Example (`maze1.txt`):**
```text
#####B#
##### #
####  #
#### ##
     ##
A######
```

## Key Files

*   **`maze.py`**: The main script containing the `Maze`, `Node`, `StackFrontier`, and `QueueFrontier` classes. It handles parsing, solving, and rendering.
*   **`requirements.txt`**: Lists external dependencies (currently only `pillow`).
*   **`maze*.txt`**: Example maze layouts.

## Outputs

1.  **Console:** Displays the initial maze, the solving process (number of states explored), and the solved maze path.
2.  **Image:** Generates `maze.png` in the current directory, showing:
    *   **Walls**: Dark Gray
    *   **Start**: Red
    *   **Goal**: Green
    *   **Solution Path**: Yellow
    *   **Explored Cells**: Red/Orange tint
