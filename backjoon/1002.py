import math

text_case = input()
for _ in range(int(text_case)):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))
    if r1 + r2 < dist:
        print(0)
    elif r1 + r2 == dist or abs(r1-r2) == dist:
        print(1)
    elif abs(r1-r2) < dist < (r1+r2):
        print(2)
    elif dist == 0 and r1==r2:
        print(-1)
    else:
        print(0)