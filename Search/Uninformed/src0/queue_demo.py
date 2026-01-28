import time

class VisualQueue:
    def __init__(self):
        # We use a standard Python list to act as our queue
        self.container = []

    def is_empty(self):
        return len(self.container) == 0

    def add(self, item):
        """
        Adds an item to the 'back' of the queue.
        """
        self.container.append(item)
        self.visualize(f"ENQUEUE (Added): {item}")

    def remove(self):
        """
        Removes the item from the 'front' of the queue.
        This is the First-In, First-Out (FIFO) behavior.
        """
        if self.is_empty():
            print("Cannot remove: Queue is empty!")
            return None
        
        # Pop from index 0 (the first item added)
        # Note: In a real large app, collections.deque is more efficient than list for this.
        item = self.container.pop(0) 
        self.visualize(f"DEQUEUE (Removed): {item}")
        return item

    def visualize(self, action):
        """
        Prints a diagram of the queue's current state.
        """
        print("\n" + "="*50)
        print(f" ACTION: {action}")
        print("="*50)
        
        if self.is_empty():
            print("\n    [ Empty Queue ]\n")
        else:
            # Visualize like a line at a store:
            # Front (First person) <--- [ Person A | Person B ] <--- Back (New person)
            
            content_str = " | ".join(self.container)
            print(f"\n    Front (Out) <--- [ {content_str} ] <--- Back (In)\n")
        
        print("-" * 50)
        time.sleep(1.0)

# --- Main Execution ---
if __name__ == "__main__":
    print("Initializing a new Queue...\n")
    q = VisualQueue()

    # 1. Add items (Enqueue)
    q.add("Person A")
    q.add("Person B")
    q.add("Person C")

    # 2. Remove an item (Dequeue)
    # Notice that 'Person A' (the FIRST one added) is the FIRST one removed.
    q.remove()

    # 3. Add a new item
    q.add("Person D")

    # 4. Remove remaining items
    q.remove()
    q.remove()
    q.remove()
    
    # 5. Try to remove from empty queue
    q.remove()
