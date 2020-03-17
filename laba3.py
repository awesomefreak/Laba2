# Сапрыкин Константин ИБ186-1
# Решите задачу о Ханойской башне
def moveTower(height, fromPole,  toPole,  withPole):
    if height >= 1:
        moveTower(height-1, fromPole, withPole, toPole)
        moveDisk(fromPole, toPole)
        moveTower(height-1, withPole, toPole, fromPole)

def moveDisk(fp, tp):
    print("Передвигаю диск с", fp, "to", tp)

n = int(input("Введите высоту башни\n"))
moveTower(n, "A", "B", "C")