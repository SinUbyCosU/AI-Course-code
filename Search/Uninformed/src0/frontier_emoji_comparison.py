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
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

# --- Visualization Logic ---

def print_side_by_side(stack, queue, step_description, last_action_stack=None, last_action_queue=None):
    print("\n" + "★" * 80)
    print(f" STEP: {step_description}")
    print("★" * 80 + "\n")

    # --- Header ---
    print(f"{ 'STACK (Depth-First)':<40} | { 'QUEUE (Breadth-First)':<40}")
    print(f"{ 'LIFO (Last-In, First-Out)':<40} | { 'FIFO (First-In, First-Out)':<40}")
    print("-" * 80)

    # --- Last Action Info ---
    s_action = f"Last Op: {last_action_stack}" if last_action_stack else ""
    q_action = f"Last Op: {last_action_queue}" if last_action_queue else ""
    print(f"{s_action:<40} | {q_action:<40}")
    print("-" * 80)

    # --- Drawing ---
    
    # 1. Prepare Stack Visual (Vertical List)
    s_lines = []
    if not stack.frontier:
        s_lines.append("    [ Empty ]")
    else:
        s_lines.append("    (Top/In/Out)")
        s_lines.append("      ↓")
        for item in reversed(stack.frontier):
            # Using simple spacing for emojis
            s_lines.append(f"    |    {item}    |")
        s_lines.append("    |__________|")
    
    # 2. Prepare Queue Visual (Horizontal Line)
    q_lines = []
    if not queue.frontier:
        q_lines.append("    [ Empty ]")
    else:
        # Visual: OUT <--- [ item | item ] <--- IN
        content = " | ".join(queue.frontier)
        q_lines.append("")
        q_lines.append(f"    Front <--- [ {content} ] <--- Back")
        q_lines.append("")

    # 3. Print side by side
    max_lines = max(len(s_lines), len(q_lines))
    
    for i in range(max_lines):
        s_str = s_lines[i] if i < len(s_lines) else ""
        q_str = q_lines[i] if i < len(q_lines) else ""
        # Adjust padding slightly for emoji width
        print(f"{s_str:<35}      | {q_str:<40}")

    print("\n" + "="*80)
    time.sleep(2.0)

# --- Main Execution ---

if __name__ == "__main__":
    s = StackFrontier()
    q = QueueFrontier()

    print("Initializing Emoji Comparison...\n")
    
    # 1. ADD Apple
    s.add("🍎")
    q.add("🍎")
    print_side_by_side(s, q, "Picked an Apple 🍎", "Added 🍎", "Added 🍎")

    # 2. ADD Banana
    s.add("🍌")
    q.add("🍌")
    print_side_by_side(s, q, "Picked a Banana 🍌", "Added 🍌", "Added 🍌")

    # 3. ADD Grapes
    s.add("🍇")
    q.add("🍇")
    print_side_by_side(s, q, "Picked Grapes 🍇", "Added 🍇", "Added 🍇")

    # 4. REMOVE (The Big Difference)
    s_removed = s.remove() # Expect Grapes
    q_removed = q.remove() # Expect Apple
    
    print_side_by_side(s, q, "TIME TO EAT! (Remove 1 item)", 
                       f"ATE: {s_removed}", 
                       f"ATE: {q_removed}")

    # 5. ADD Watermelon
    s.add("🍉")
    q.add("🍉")
    print_side_by_side(s, q, "Picked Watermelon 🍉", "Added 🍉", "Added 🍉")

    # 6. REMOVE Again
    s_removed = s.remove() # Expect Watermelon
    q_removed = q.remove() # Expect Banana
    
    print_side_by_side(s, q, "EAT AGAIN! (Remove 1 item)", 
                       f"ATE: {s_removed}", 
                       f"ATE: {q_removed}")
