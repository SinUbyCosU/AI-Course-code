import time
import os

class VisualStack:
    def __init__(self):
        # We use a standard Python list to act as our stack
        self.container = []

    def is_empty(self):
        return len(self.container) == 0

    def add(self, item):
        """
        Adds an item to the 'top' of the stack.
        (In a list, the 'top' is the end of the list).
        """
        self.container.append(item)
        self.visualize(f"PUSH (Added): {item}")

    def remove(self):
        """
        Removes the item from the 'top' of the stack.
        This is the Last-In, First-Out (LIFO) behavior.
        """
        if self.is_empty():
            print("Cannot remove: Stack is empty!")
            return None
        
        # .pop() without arguments removes the last item in the list
        item = self.container.pop()
        self.visualize(f"POP (Removed): {item}")
        return item

    def visualize(self, action):
        """
        Prints a diagram of the stack's current state.
        """
        # Clear screen for animation effect (works on Linux/Mac/Windows)
        # os.system('cls' if os.name == 'nt' else 'clear') 
        
        print("\n" + "="*40)
        print(f" ACTION: {action}")
        print("="*40)
        
        if self.is_empty():
            print("\n    [ Empty Stack ]\n")
        else:
            print("        (Top)")
            print("          ↓")
            # Iterate backwards to show the top item first
            for item in reversed(self.container):
                print(f"    |  {item.center(12)}  |")
            print("    |________________|")
            print("        (Bottom)\n")
        
        print("-" * 40)
        # Pause briefly so we can see the step
        time.sleep(1.0)

# --- Main Execution ---
if __name__ == "__main__":
    print("Initializing a new Stack...\n")
    stack = VisualStack()

    # 1. Add items (Pushing)
    stack.add("Book A")
    stack.add("Book B")
    stack.add("Book C")

    # 2. Remove an item (Popping)
    # Notice that 'Book C' (the last one added) is the first one removed.
    stack.remove()

    # 3. Add a new item
    stack.add("Book D")

    # 4. Remove remaining items
    stack.remove()
    stack.remove()
    stack.remove()
    
    # 5. Try to remove from empty stack
    stack.remove()
