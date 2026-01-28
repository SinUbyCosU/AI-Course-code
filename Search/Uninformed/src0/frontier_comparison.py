import time

# --- The Classes from maze.py (Simplified) ---

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if len(self.frontier) == 0:
            return None
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def remove(self):
        if len(self.frontier) == 0:
            return None
        else:
            # The key difference: pop(0) removes from the START
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# --- Visualization Logic ---

def print_side_by_side(stack, queue, step_description, last_action_stack=None, last_action_queue=None):
    print("\n" + "#" * 80)
    print(f" STEP: {step_description}")
    print("#" * 80 + "\n")

    # --- Header ---
    print(f"{ 'STACK (Depth-First Search)':<40} | { 'QUEUE (Breadth-First Search)':<40}")
    print(f"{ 'Behavior: LIFO (Last-In, First-Out)':<40} | { 'Behavior: FIFO (First-In, First-Out)':<40}")
    print("-" * 80)

    # --- Last Action Info ---
    s_action = f"Last Op: {last_action_stack}" if last_action_stack else ""
    q_action = f"Last Op: {last_action_queue}" if last_action_queue else ""
    print(f"{s_action:<40} | {q_action:<40}")
    print("-" * 80)

    # --- Drawing ---
    
    # 1. Prepare Stack Visual (Vertical List)
    # Top is at the end of the list.
    s_lines = []
    if not stack.frontier:
        s_lines.append("    [ Empty ]")
    else:
        s_lines.append("    (Top/In/Out)")
        s_lines.append("      ↓")
        for item in reversed(stack.frontier):
            s_lines.append(f"    | {item.center(10)} |")
        s_lines.append("    |____________|")
    
    # 2. Prepare Queue Visual (Horizontal Line)
    # Front is index 0, Back is index -1
    q_lines = []
    if not queue.frontier:
        q_lines.append("    [ Empty ]")
    else:
        # Visual: OUT <--- [ item | item ] <--- IN
        content = " | ".join(queue.frontier)
        q_lines.append("")
        q_lines.append("    Front (Out) <--- [ " + content + " ] <--- Back (In)")
        q_lines.append("")

    # 3. Print side by side (roughly)
    # Since their shapes are different, we print the Stack block then the Queue block 
    # slightly adjusted, or just render them in their distinct columns. 
    # For clarity, let's render the Stack column logic vs Queue column logic. 
    
    max_lines = max(len(s_lines), len(q_lines))
    
    for i in range(max_lines):
        s_str = s_lines[i] if i < len(s_lines) else ""
        q_str = q_lines[i] if i < len(q_lines) else ""
        print(f"{s_str:<40} | {q_str:<40}")

    print("\n" + "="*80)
    time.sleep(2.0)

# --- Main Execution ---

if __name__ == "__main__":
    s = StackFrontier()
    q = QueueFrontier()

    print("Initializing Comparison...\n")
    
    # 1. ADD Node A
    s.add("A")
    q.add("A")
    print_side_by_side(s, q, "Added Node 'A'", "Added 'A'", "Added 'A'")

    # 2. ADD Node B
    s.add("B")
    q.add("B")
    print_side_by_side(s, q, "Added Node 'B'", "Added 'B'", "Added 'B'")

    # 3. ADD Node C
    s.add("C")
    q.add("C")
    print_side_by_side(s, q, "Added Node 'C'", "Added 'C'", "Added 'C'")

    # 4. REMOVE (The Big Difference)
    s_removed = s.remove() # Expect C (Last In)
    q_removed = q.remove() # Expect A (First In)
    
    print_side_by_side(s, q, "REMOVE EXECUTED!", 
                       f"REMOVED: {s_removed}", 
                       f"REMOVED: {q_removed}")

    # 5. ADD Node D
    s.add("D")
    q.add("D")
    print_side_by_side(s, q, "Added Node 'D'", "Added 'D'", "Added 'D'")

    # 6. REMOVE Again
    s_removed = s.remove() # Expect D (Last In)
    q_removed = q.remove() # Expect B (Next in line)
    
    print_side_by_side(s, q, "REMOVE EXECUTED!", 
                       f"REMOVED: {s_removed}", 
                       f"REMOVED: {q_removed}")
