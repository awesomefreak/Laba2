# Сапрыкин Константин ИБ186-1

# Черепашка

a = []
with open("laba4.in", "r") as f:
	h, w = [int(x) for x in f.readline().split(" ")]
	for _ in range(h): 
		a.append([int(x) for x in f.readline().split(" ")])
for x in range(1, w):
	a[0][x] = a[0][x] + a[0][x-1]
for x in range(1, h):
	a[x][0] = a[x][0] + a[x-1][0]
for x in range(1, h):
	for y in range(1, w):
		a[x][y] = a[x][y] + max(a[x-1][y], a[x][y-1])
print(a[h-1][w-1])


