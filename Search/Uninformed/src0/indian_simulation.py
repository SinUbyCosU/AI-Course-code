import time
import sys

# --- SIMULATION CLASSES ---

class RotiStack:
    def __init__(self):
        self.items = []
        self.name = "DHABA KITCHEN (Stack/LIFO)"
        self.icon = "🔥"

    def push(self, item):
        self.items.append(item)
        return f"Chef made {item}"

    def pop(self):
        if not self.items:
            return "Basket is empty!"
        item = self.items.pop() # Removes from the END (Top)
        return f"Waiter served {item}"

class TicketQueue:
    def __init__(self):
        self.items = []
        self.name = "RAILWAY COUNTER (Queue/FIFO)"
        self.icon = "🚂"

    def enqueue(self, item):
        self.items.append(item)
        return f"{item} joined the line"

    def dequeue(self):
        if not self.items:
            return "Counter is empty!"
        item = self.items.pop(0) # Removes from the START (Front)
        return f"Clerk issued ticket to {item}"

# --- VISUALIZATION ENGINE ---

def render_scene(stack, queue, message, last_stack_action="", last_queue_action=""):
    # ANSI Colors
    HEADER = '\033[95m'
    ORANGE = '\033[33m' # Saffron-ish
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    print("\n" * 2)
    print(f"{HEADER}{'='*90}{RESET}")
    print(f"{BOLD} SCENE: {message}{RESET}")
    print(f"{HEADER}{'='*90}{RESET}")

    # --- Prepare The Roti Basket (Stack) ---
    stack_lines = []
    stack_lines.append(f"{ORANGE}🥘 THE ROTI BASKET (LIFO){RESET}")
    stack_lines.append(f"   {last_stack_action}")
    stack_lines.append(f"   {'-'*25}")
    
    if not stack.items:
        stack_lines.append("   [ Empty Basket ]")
    else:
        stack_lines.append("       (Hot & Fresh)")
        stack_lines.append("          ↓")
        for item in reversed(stack.items):
            # Roti visual
            stack_lines.append(f"      | {item} |")
        stack_lines.append("      |__________|")
        stack_lines.append("      (Cloth/Bottom)")

    # --- Prepare The Ticket Line (Queue) ---
    queue_lines = []
    queue_lines.append(f"{CYAN}🚂 TATKAL TICKET LINE (FIFO){RESET}")
    queue_lines.append(f"   {last_queue_action}")
    queue_lines.append(f"   {'-'*25}")
    
    if not queue.items:
        queue_lines.append("   [ No Passengers ]")
    else:
        # Visual: Counter <--- [ Person ] <--- [ Person ]
        
        queue_lines.append("   Ticket Window (Counter)")
        queue_lines.append("   ↓")
        for i, item in enumerate(queue.items):
            if i == 0:
                prefix = f"   🙏 {item} (Next)"
            else:
                prefix = f"      {item}"
            queue_lines.append(prefix)
        queue_lines.append("      ↑")
        queue_lines.append("   End of Line (New Entry)")

    # --- Merge and Print Side-by-Side ---
    max_h = max(len(stack_lines), len(queue_lines))
    
    for i in range(max_h):
        left = stack_lines[i] if i < len(stack_lines) else ""
        
        # Simple tab separation
        print(f"{left:<50} 	 {queue_lines[i] if i < len(queue_lines) else ''}")

    print(f"{HEADER}{'='*90}{RESET}")
    time.sleep(3.0) 

# --- MAIN SCRIPT ---

if __name__ == "__main__":
    s = RotiStack()
    q = TicketQueue()

    # 1. Start
    render_scene(s, q, "MORNING RUSH BEGINS!")

    # 2. Activity
    s_act = s.push("🫓 Plain Roti")
    q_act = q.enqueue("👴 Dadaji")
    render_scene(s, q, "First orders", s_act, q_act)

    s_act = s.push("🍘 Butter Naan")
    q_act = q.enqueue("🎒 Student")
    render_scene(s, q, "Getting busy", s_act, q_act)

    s_act = s.push("🥞 Aloo Paratha")
    q_act = q.enqueue("💼 Sharma Ji")
    render_scene(s, q, "Full House!", s_act, q_act)

    # 3. ACTION!
    # STACK: Waiter takes the TOP Roti (Aloo Paratha). It's the hottest!
    # QUEUE: Clerk calls the FRONT person (Dadaji). He's been waiting longest.
    
    s_act = s.pop() 
    q_act = q.dequeue()
    render_scene(s, q, "SERVICE TIME! (LIFO vs FIFO)", s_act, q_act)

    # 4. New Entry
    s_act = s.push("🫓 Garlic Naan")
    q_act = q.enqueue("📱 Influencer")
    render_scene(s, q, "New Order & New Passenger", s_act, q_act)

    # 5. Service Again
    # STACK: Waiter serves "Garlic Naan" (Just made!). Plain Roti is getting cold at the bottom.
    # QUEUE: Clerk serves "Student". Influencer has to wait.
    
    s_act = s.pop()
    q_act = q.dequeue()
    render_scene(s, q, "KEEP MOVING...", s_act, q_act)

    # 6. Final Rush
    render_scene(s, q, "LUNCH TIME RUSH - CLEARING ALL!")
    
    while s.items or q.items:
        s_act = s.pop() if s.items else "Kitchen Closed"
        q_act = q.dequeue() if q.items else "Counter Closed"
        render_scene(s, q, "Serving...", s_act, q_act)
