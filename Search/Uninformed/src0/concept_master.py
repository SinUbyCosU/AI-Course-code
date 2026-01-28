import time

# --- UTILS FOR PRETTY PRINTING ---
def print_header(title):
    print("\n" + "█" * 80)
    print(f"   {title}")
    print("█" * 80)

def print_concept(msg):
    print(f"\n🧠 \033[1mCONCEPT CHECK:\033[0m {msg}\n")

# ==========================================
# PART 1: THE STACK (LIFO)
# Scenario: The "Chair" where you dump clothes
# ==========================================

class ClothesChair:
    def __init__(self):
        self.pile = []
    
    def throw_on_top(self, item):
        self.pile.append(item)
        print(f"➕ THREW '{item}' on the pile.")
        self.show_pile()
        
    def pick_up(self):
        if not self.pile:
            print("Chair is clean!")
            return
        
        # KEY CONCEPT: We take the last item added
        item = self.pile.pop() 
        print(f"➖ PICKED UP '{item}' (It was on top)")
        self.show_pile()

    def show_pile(self):
        print(f"   [ Current Chair State ]")
        if not self.pile:
            print("   (Empty Chair)")
        else:
            for i, item in enumerate(reversed(self.pile)):
                if i == 0:
                    print(f"   👕 {item} <--- TOP (Accessible)")
                else:
                    print(f"   👚 {item} (Buried)")
        print("-" * 40)
        time.sleep(1.5)

# ==========================================
# PART 2: THE QUEUE (FIFO)
# Scenario: Delhi Metro Security Line
# ==========================================

class MetroLine:
    def __init__(self):
        self.line = []
    
    def join_line(self, person):
        self.line.append(person)
        print(f"➕ '{person}' joined the back of the line.")
        self.show_line()
        
    def pass_security(self):
        if not self.line:
            print("Line is empty!")
            return
            
        # KEY CONCEPT: We take the first item (Index 0)
        person = self.line.pop(0)
        print(f"✅ '{person}' passed security (Was at front)")
        self.show_line()

    def show_line(self):
        print(f"   [ Current Metro Line ]")
        if not self.line:
            print("   (No crowd)")
        else:
            print("   Security Guard 👮")
            print("       ^")
            print("       |")
            for i, person in enumerate(self.line):
                if i == 0:
                    print(f"   🧍 {person} (Next Turn)")
                else:
                    print(f"   🧍 {person} (Waiting...)")
        print("-" * 40)
        time.sleep(1.5)

# ==========================================
# MAIN EXECUTION
# ==========================================

if __name__ == "__main__":
    
    # --- STACK DEMO ---
    print_header("PART 1: THE STACK (Last-In, First-Out)")
    print("Imagine 'The Chair' in your room where you pile clothes.")
    
    chair = ClothesChair()
    
    chair.throw_on_top("Blue Jeans")
    chair.throw_on_top("Gym T-Shirt")
    chair.throw_on_top("Red Hoodie")
    
    print_concept("You want the Blue Jeans at the bottom?\nYou CANNOT take them yet. You must remove the Red Hoodie first.")
    
    chair.pick_up() # Removes Red Hoodie
    chair.pick_up() # Removes Gym T-Shirt
    chair.pick_up() # Removes Blue Jeans
    
    # --- QUEUE DEMO ---
    print_header("PART 2: THE QUEUE (First-In, First-Out)")
    print("Imagine a Metro Station Security Check.")
    
    metro = MetroLine()
    
    metro.join_line("Rahul (Student)")
    metro.join_line("Priya (Office)")
    metro.join_line("Amit (Uncle)")
    
    print_concept("Who goes first?\nRahul came first, so Rahul goes first. Amit cannot cut the line.")
    
    metro.pass_security() # Rahul passes
    metro.pass_security() # Priya passes
    metro.pass_security() # Amit passes
    
    print_header("SUMMARY")
    print("1. STACK = A Pile. You interact with the TOP. (LIFO)")
    print("2. QUEUE = A Line. You interact with the FRONT. (FIFO)")
    print("\n")
