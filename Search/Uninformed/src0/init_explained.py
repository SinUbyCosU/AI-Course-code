class BadMusicPlayer:
    def __init__(self):
        # This player is rigid. It can ONLY play this one song.
        self.song = "Default Song.mp3"
        print(f"BadPlayer initialized. Ready to play: {self.song}")

class SmartMusicPlayer:
    def __init__(self, filename):
        # This player is flexible! It takes 'filename' as input
        # and saves it to 'self.song' (ITS own song).
        self.song = filename
        print(f"SmartPlayer initialized. Loaded file: '{filename}'")

if __name__ == "__main__":
    print("--- SCENARIO 1: The Rigid Class ---")
    p1 = BadMusicPlayer()
    p2 = BadMusicPlayer()
    # Both p1 and p2 are stuck playing "Default Song.mp3"
    
    print("\n--- SCENARIO 2: The Flexible Class (Like maze.py) ---")
    # We use the SAME class to make two completely different objects
    m1 = SmartMusicPlayer("maze1.txt")
    m2 = SmartMusicPlayer("maze2.txt")

    print("\nCheck what they remembered:")
    print(f"Player M1 is playing: {m1.song}")
    print(f"Player M2 is playing: {m2.song}")
