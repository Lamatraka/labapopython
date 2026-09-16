print("Оформление заказа")

order_name = input("Название заказа: ")
customer = input("Имя заказчика: ")

item1 = input("Название первой позиции: ")
qty1 = int(input("Количество первой позиции: "))
price1 = float(input("Цена первой позиции (руб.): "))

item2 = input("Название второй позиции: ")
qty2 = int(input("Количество второй позиции: "))
price2 = float(input("Цена второй позиции (руб.): "))

delivery = float(input("Стоимость доставки (руб.): "))
skidka = float(input("Скидка на товары (0-100 %): "))
paid = float(input("Внесённая сумма (руб.): "))

cost1 = qty1 * price1
cost2 = qty2 * price2
total = cost1 + cost2

discount_rub = total * skidka / 100
after_discount = total - discount_rub

itogo = after_discount + delivery

total_qty = qty1 + qty2
change = paid - itogo

print()
print("Заказ:", order_name)
print("Заказчик:", customer)
print(f"{item1} | {qty1} | {price1:.2f} | {cost1:.2f}")
print(f"{item2} | {qty2} | {price2:.2f} | {cost2:.2f}")
print(f"Стоимость товаров без доставки: {total:.2f}")
print(f"Скидка ({skidka:.2f} %): -{discount_rub:.2f}")
print(f"Стоимость доставки: {delivery:.2f}")
print(f"Общая сумма с учётом скидки и доставки: {itogo:.2f}")
print(f"Общее количество единиц: {total_qty}")
print(f"Сдача: {change:.2f}")