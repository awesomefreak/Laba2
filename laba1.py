# Сапрыкин Константин ИБ186-1
import time
import math

# Бине
start = time.time()

ans = (pow((1 + math.sqrt(5))/2.,35)-pow((1 - math.sqrt(5))/2.,35))/math.sqrt(5)

print("Бине")
print(int(ans))
print(time.time() - start)

# Итерационая формула?


# Разделяй и властвуй
start = time.time()

f1 = lambda n: f1(n - 1) + f1(n - 2) if n > 2 else 1

print("Разделяй и властвуй")
print(f1(35))
print(time.time() - start)

# Нисходящие ДП
start = time.time()

M = {0: 0, 1: 1}
def f2(n):
    if n in M:
        return M[n]
    M[n] = f2(n - 1) + f2(n - 2)
    return M[n]

print("Нисходящие ДП")
print(f2(35))
print(time.time() - start)

# Восходящие ДП
start = time.time()

def f3(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

print("Восходящие ДП")
print(f3(35))
print(time.time() - start)