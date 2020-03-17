# Сапрыкин Константин ИБ186-1

# г)Задача о неограниченном рюкзаке, каждый предмет может быть взят любое количество раз
# (Задание не конкретоне, думаю данная задача норм)

WeightLimit = int(input("Введите лимит веса\n"))
n = int(input("количество предметов\n"))
print("Введите вес и ценность предмета через пробел")
items = dict()
for _ in range(n):
	w, v = input().split(" ")
	items[int(w)] = int(v)
d = [0]*(WeightLimit + 1)
for x in items:
	for i in range(x, WeightLimit + 1):
		d[i] = max(d[i],d[i-x] + items[x])
print(d[WeightLimit])
