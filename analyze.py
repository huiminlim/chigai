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

ys = []
ys.append(corner_y)
for p in points[1]:
    ys.append(p[1])
ys.sort()
print(ys)

idx = 0
delta = 0
for i in range(len(ys)-1):
    diff = ys[i+1]-ys[i]
    if diff < 1.5 * tempalte_height :
        idx += 1
        if delta == 0 or diff < delta:
            delta = diff
    else:
        idx += diff // delta

    print(idx, diff)
