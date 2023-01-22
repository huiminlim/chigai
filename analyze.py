import os

# Set directory path of current folder
DATA_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\data\\sample_1"

with open(f"{DATA_DIR}\\corner.txt", "r") as f:
    [corner_x, corner_y, template_width, tempalte_height] = [int(x) for x in f.readline().split(" ")]
print(corner_x, corner_y, template_width, tempalte_height)

points = [[]]
prev_x = corner_x
with open(f"{DATA_DIR}\\output.txt", "r") as f:
    for line in f:
        [x, y] = [int(x) for x in line.strip().split(" ")]
        if not abs(prev_x - x) < template_width:
            points[-1].sort()
            points.append([])
            prev_x = x
        points[-1].append([x, y])

indexes = {}
for x in range(32):
    for y in range(32):
        indexes[(x,y)] = False

out = []
prev_y = corner_y
for col in points:
    for point in col:
        x = point[0]
        y = point[1]
        idx_x = abs(x-corner_x) // template_width
        idx_y = abs(y-prev_y) // tempalte_height
        print(x, y, idx_x, idx_y)
        out.append((idx_x, idx_y))
    # print()
    break

out.sort()
for p in out:
    print(p)

