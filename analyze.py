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

# Prepend the corner point to the first column
points[0].insert(0, [corner_x, corner_y])

all_ys = []
for col in points:
    ys = []
    for [x,y] in col:
        ys.append(y)
    ys.sort()
    all_ys.append(ys)

# Generate map
mapping = {}
for row in range(32):
    for col in range(32):
        mapping[(row, col)] = False

idx_col = 0
for col in all_ys:
    idx = 0
    delta = 0
    for i in range(len(col)-1):
        diff = col[i+1] - col[i]
        if diff < 1.5 * tempalte_height :
            idx += 1
            if delta == 0 or diff < delta:
                delta = diff
        else:
            idx += diff // delta
        mapping[(idx, idx_col)] = True
    idx_col += 1

col_idx = 0
for col in all_ys:
    top = col[0]
    if abs(top - corner_y) < 1.5 * tempalte_height:
        mapping[(0, col_idx)] = True
    col_idx += 1

mapping[(0, 0)] = False

result = [(row, col) for (row, col), status in mapping.items() if status ==False]
print(result)
