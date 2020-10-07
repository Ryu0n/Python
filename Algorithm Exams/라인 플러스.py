boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]

def rm():
    for k in range(0, len(boxes)):
        if boxes[k][0] == boxes[k][1]:
            boxes[k][0] = 0
            boxes[k][1] = 0

def check():
    count = 0
    for l in range(0, len(boxes)):
        if boxes[l][0] != 0:
            count += 1
        if boxes[l][1] != 0:
            count += 1
    return count


rm()

for i in range(0, len(boxes) - 1):
    f = boxes[i][0]
    s = boxes[i][1]

    if f != s:
        for j in range(i + 1, len(boxes)):
            if f in boxes[j]:
                fAfter = boxes[j][boxes[j].index(f)]
                boxes[i][0] = 0
                boxes[j][boxes[j].index(f)] = 0

            if s in boxes[j]:
                sAfter = boxes[j][boxes[j].index(s)]
                boxes[i][1] = 0
                boxes[j][boxes[j].index(s)] = 0


answer = int(check() / 2)
print(answer)