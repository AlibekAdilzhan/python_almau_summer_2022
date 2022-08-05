map = [
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 2, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]

start = [1, 1]
exit = [0, 3]
queue = [start]

while True:
    current = queue[0]
    cx = current[0]
    cy = current[1]
    if map[cx][cy - 1] == 0:
        queue.append([cx, cy - 1])
        map[cx][cy - 1] = map[cx][cy] + 1
    if map[cx][cy + 1] == 0:
        queue.append([cx, cy + 1])
        map[cx][cy + 1] = map[cx][cy] + 1
    if map[cx + 1][cy] == 0:
        queue.append([cx + 1, cy])
        map[cx + 1][cy] = map[cx][cy] + 1
    if map[cx - 1][cy] == 0:
        queue.append([cx - 1, cy])
        map[cx - 1][cy] = map[cx][cy] + 1
    queue.pop(0)
    if queue == []:
        break



# for i in range(len(map)):
#     print(map[i])


path = []
current = exit
while True:
    x = current[0]
    y = current[1]
    number = map[x][y]
    if map[x - 1][y] == number - 1:
        path.append((x - 1, y))
        current = [x - 1, y]
    elif map[x + 1][y] == number - 1:
        path.append((x + 1, y))
        current = [x + 1, y]
    elif map[x][y + 1] == number - 1:
        path.append((x, y + 1))
        current = [x, y + 1]
    elif map[x][y - 1] == number - 1:
        path.append((x, y - 1))
        current = [x, y - 1]

    if current == start:
        break
print(path)