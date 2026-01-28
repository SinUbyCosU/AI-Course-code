class StackFrontier():
    def __init__(self):
        # Starts with an empty list to hold our nodes (items)
        self.frontier = []
        print("--- Initialized: Empty Stack created ---")

    def add(self, node):
        # .append adds the item to the END of the list
        self.frontier.append(node)
        print(f"ADD: Put '{node}' on top. Current Stack: {self.frontier}")

    def contains_state(self, state):
        # Checks if a state is already in the stack
        exists = any(node == state for node in self.frontier)
        print(f"CHECK: Is '{state}' in stack? {'Yes' if exists else 'No'}")
        return exists

    def empty(self):
        # Returns True if the list is empty
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            # node = self.frontier[-1] looks at the VERY LAST item
            node = self.frontier[-1]
            
            # self.frontier[:-1] keeps everything EXCEPT the last item
            self.frontier = self.frontier[:-1]
            
            print(f"REMOVE: Took '{node}' from the top.")
            print(f"Remaining Stack: {self.frontier}")
            return node

# --- Visual Example ---
print("\n--- STACK OF BOOKS EXAMPLE ---")
s = StackFrontier()

# 1. Adding items
s.add("Math Book")
s.add("Science Book")
s.add("History Book")

print("\n--- THE LIFO MOMENT ---")
# 2. Removing an item
# Even though "Math" was first, "History" is the one that comes out!
s.remove()

print("\n--- ADDING ANOTHER ---")
s.add("Art Book")

print("\n--- CLEARING THE STACK ---")
s.remove() # Takes Art
s.remove() # Takes Science
s.remove() # Takes Math
