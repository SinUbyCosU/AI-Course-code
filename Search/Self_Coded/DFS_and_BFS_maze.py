with open ("maze.txt", "r") as file:
    content = file.read()
print(content)

lines=content.splitlines()
print("lines in maze:")
for line_number, line in enumerate(lines):
    print(f"{line_number}: {line}   ")

height=len(lines)
width=max(len(line) for line in lines)

print(f"height:{height}, width:{width}")

#step 2c find start A and goal B

start =None
goal=None
for i in range(height):
    for j in range(len(lines[i])):
        if lines[i][j]=='A':
            start=(i,j)
        elif lines[i][j]=='B':
            goal=(i,j)
    print(f"start:{start},goal:{goal}")

#step 3 create walls for the maze
walls=[]
for i in rnage(height):
    row=[]
