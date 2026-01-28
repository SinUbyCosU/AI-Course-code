import time

class StackFrontier():
    def __init__(self):
        # CODE: self.frontier = []
        # LOGIC: Initialize an empty list to store our nodes.
        self.frontier = []
        self.visualize("INIT", "self.frontier = [] (Created empty list)")

    def add(self, node):
        # CODE: self.frontier.append(node)
        # LOGIC: Python's .append() always adds to the END of the list.
        # In a stack, the 'END' is our 'TOP'.
        self.frontier.append(node)
        
        explanation = f"CODE: self.frontier.append('{node}')\nLOGIC: Adds to the END of the list (the TOP of our stack)."
        self.visualize("ADD (PUSH)", explanation)

    def remove(self):
        if len(self.frontier) == 0:
            raise Exception("empty frontier")
        else:
            # CODE: node = self.frontier[-1]
            # LOGIC: In Python, [-1] is the shorthand for the LAST item in a list.
            # This allows us to 'peek' at the top item before removing it.
            node = self.frontier[-1]

            # CODE: self.frontier = self.frontier[:-1]
            # LOGIC: This is 'slicing'. It takes everything from the start 
            # up to (but not including) the last item. Effectively deleting the top.
            self.frontier = self.frontier[:-1]
            
            explanation = f"CODE: node = self.frontier[-1] (Grabs '{node}')\nCODE: self.frontier = self.frontier[:-1] (Removes it)"
            self.visualize("REMOVE (POP)", explanation)
            return node

    def visualize(self, action_name, logic_explanation):
        # Header
        print("\n" + "█"*60)
        print(f"  ACTION: {action_name}")
        print("█"*60)
        
        # Code Explanation Section
        print(f"\n[ STEP EXPLANATION ]")
        print(f"{logic_explanation}")
        
        # Visual Diagram Section
        print(f"\n[ VISUAL STATE ]")
        if not self.frontier:
            print("\n    [ Empty Stack ]\n")
        else:
            print("        (Top)")
            print("          ↓")
            # Iterate backwards to show the top item first
            for item in reversed(self.frontier):
                print(f"    |  {item.center(14)}  |")
            print("    |________________|")
            print("        (Bottom)\n")
        
        print("-" * 60)
        time.sleep(2.0)

# --- Execution ---
if __name__ == "__main__":
    s = StackFrontier()

    # Demonstrating the lines you asked about:
    s.add("Math Book")
    s.add("Science Book")
    s.add("History Book")
    
    # Demonstrating the removal logic:
    s.remove()
    s.add("Art Book")
    s.remove()
