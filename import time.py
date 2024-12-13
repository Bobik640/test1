import time

# Начальное значение
start = 0
end = 1000000
step = 10

# Цикл увеличения чисел
for number in range(start, end + 1, step):
    print(number)
    time.sleep(0.50)  # Задержка для наглядности (10 мс)
