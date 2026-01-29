with open ("maze.txt", "r") as file:
    content = file.read()
print(content)

lines=content.splitlines()
print("lines in maze:")
for line_number, line in enumerate(lines):
    print(f"{line_number}: {line}   ")