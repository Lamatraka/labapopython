pred1 = input("Название первого предмета: ")
pred2 = input("Название второго предмета: ")

kolvo1 = int(input(f"Количество занятий по '{pred1}' за неделю: "))
while kolvo1 < 0:
    kolvo1 = int(input("Количество не может быть отрицательным, повторите: "))

min1 = int(input(f"Продолжительность занятия по '{pred1}' (мин): "))
while min1 <= 0:
    min1 = int(input("Продолжительность должна быть положительной, повторите: "))

kolvo2 = int(input(f"Количество занятий по '{pred2}' за неделю: "))
while kolvo2 < 0:
    kolvo2 = int(input("Количество не может быть отрицательным, повторите: "))

min2 = int(input(f"Продолжительность занятия по '{pred2}' (мин): "))
while min2 <= 0:
    min2 = int(input("Продолжительность должна быть положительной, повторите: "))

time1 = kolvo1 * min1
time2 = kolvo2 * min2
total_min = time1 + time2
total_hours = total_min / 60

available = float(input("Доступное время на неделю (ч): "))
while available < total_hours:
    available = float(input(f"Доступное время не меньше {total_hours:.2f} ч, повторите: "))
ost = available - total_hours
total_min_4 = total_min * 4
total_hours_4 = total_hours * 4

print()
print("Учебная нагрузка")
print(f"Предмет '{pred1}': {time1} мин")
print(f"Предмет '{pred2}': {time2} мин")
print(f"Общая нагрузка: {total_min} мин = {total_hours:.2f} ч")
print(f"Остаток свободного времени: {ost:.2f} ч")
print(f"Нагрузка за 4 недели: {total_min_4} мин = {total_hours_4:.2f} ч")