import time
import sys

# --- SIMULATION CLASSES ---

class StockroomStack:
    def __init__(self):
        self.items = []
        self.name = "STOCKROOM (Stack/LIFO)"
        self.icon = "🚧"

    def push(self, item):
        self.items.append(item)
        return f"Worker stacked {item}"

    def pop(self):
        if not self.items:
            return "Stockroom is empty!"
        item = self.items.pop() # Removes from the END (Top)
        return f"Worker unpacked {item}"
    
    def peek(self):
        return self.items[-1] if self.items else None

class CheckoutQueue:
    def __init__(self):
        self.items = []
        self.name = "CHECKOUT LINE (Queue/FIFO)"
        self.icon = "🏭"

    def enqueue(self, item):
        self.items.append(item)
        return f"{item} joined the line"

    def dequeue(self):
        if not self.items:
            return "No customers waiting!"
        item = self.items.pop(0) # Removes from the START (Front)
        return f"Cashier served {item}"

# --- VISUALIZATION ENGINE ---

def render_scene(stack, queue, message, last_stack_action="", last_queue_action=""):
    # ANSI Colors for nicer output
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    print("\n" * 2)
    print(f"{HEADER}{'='*90}{RESET}")
    print(f"{BOLD} SCENE: {message}{RESET}")
    print(f"{HEADER}{'='*90}{RESET}")

    # --- Prepare The Stockroom (Left Side) ---
    stock_lines = []
    stock_lines.append(f"{BLUE}📦 THE STOCKROOM (LIFO){RESET}")
    stock_lines.append(f"   {last_stack_action}")
    stock_lines.append(f"   {'-'*25}")
    
    if not stack.items:
        stock_lines.append("   [ Empty Pallet ]")
    else:
        stock_lines.append("       (Top / Newest)")
        stock_lines.append("          ↓")
        for item in reversed(stack.items):
            # Box visual
            stock_lines.append(f"      | {item} |")
        stock_lines.append("      |__________|")
        stock_lines.append("      (Pallet)")

    # --- Prepare The Checkout (Right Side) ---
    queue_lines = []
    queue_lines.append(f"{GREEN}🏪 THE CHECKOUT (FIFO){RESET}")
    queue_lines.append(f"   {last_queue_action}")
    queue_lines.append(f"   {'-'*25}")
    
    if not queue.items:
        queue_lines.append("   [ No Line ]")
    else:
        # A nice horizontal representation
        # Cashier <--- [ Person ] <--- [ Person ]
        
        # We split the line into multiple rows if it gets too long, 
        # but for this demo, we'll keep it simple vertical list for alignment
        queue_lines.append("   Start of Line (Being Served)")
        queue_lines.append("   ↓")
        for i, item in enumerate(queue.items):
            if i == 0:
                prefix = f"   🛒 {item} (Next)"
            else:
                prefix = f"      {item}"
            queue_lines.append(prefix)
        queue_lines.append("      ↑")
        queue_lines.append("   End of Line (New Arrivals)")

    # --- Merge and Print Side-by-Side ---
    max_h = max(len(stock_lines), len(queue_lines))
    
    for i in range(max_h):
        left = stock_lines[i] if i < len(stock_lines) else ""
        # Remove ANSI codes for length calculation to align properly (simplified approximation)
        # Using a fixed width buffer is safer:
        padding = 45
        
        # We print left side, move cursor, print right side
        # Note: ANSI codes mess up 'ljust', so we manually pad visually
        # A simple tab separation strategy:
        
        print(f"{left:<50} 	 {queue_lines[i] if i < len(queue_lines) else ''}")

    print(f"{HEADER}{'='*90}{RESET}")
    time.sleep(2.5) # Pause to let the user see

# --- MAIN SCRIPT ---

if __name__ == "__main__":
    s = StockroomStack()
    q = CheckoutQueue()

    # 1. Opening Time
    render_scene(s, q, "THE MALL OPENS! (Empty State)")

    # 2. Arrivals
    s_act = s.push("📦 Hats")
    q_act = q.enqueue("👵 Granny")
    render_scene(s, q, "First arrivals", s_act, q_act)

    s_act = s.push("📦 Shoes")
    q_act = q.enqueue("👨 BizMan")
    render_scene(s, q, "More traffic", s_act, q_act)

    s_act = s.push("📦 Toys")
    q_act = q.enqueue("🛹 Skater")
    render_scene(s, q, "Busy busy!", s_act, q_act)

    # 3. ACTION!
    # STACK: The worker grabs the TOP box (Toys). "Hats" are buried at the bottom.
    # QUEUE: The cashier serves the FRONT person (Granny). "Skater" waits.
    
    s_act = s.pop() 
    q_act = q.dequeue()
    render_scene(s, q, "WORK BEGINS! (Pop vs Dequeue)", s_act, q_act)

    # 4. New Arrival Distraction
    s_act = s.push("📦 Candy")
    q_act = q.enqueue("👮 Cop")
    render_scene(s, q, "New Arrivals Interrupting", s_act, q_act)

    # 5. Action Again
    # STACK: Worker grabs "Candy" (Just arrived!). "Hats" are getting dusty.
    # QUEUE: Cashier serves "BizMan". "Cop" has to wait his turn.
    
    s_act = s.pop()
    q_act = q.dequeue()
    render_scene(s, q, "WORK CONTINUES...", s_act, q_act)

    # 6. Clearing out
    render_scene(s, q, "Closing Time Rush - Speed Mode!")
    
    while s.items or q.items:
        s_act = s.pop() if s.items else "Done"
        q_act = q.dequeue() if q.items else "Done"
        render_scene(s, q, "Processing...", s_act, q_act)
