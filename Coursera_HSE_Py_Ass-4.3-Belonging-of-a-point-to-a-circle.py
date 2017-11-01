x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def IsPointCircle(x, y):
    if (x - xc) ** 2 + (y - yc) ** 2 <= r ** 2:
        return True
if IsPointCircle(x, y):
    print('Yes')
else:
    print('No')
