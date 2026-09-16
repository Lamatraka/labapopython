first_aud = input("Введите название первой аудитории: ")
second_aud = input("Введите название второй аудитории: ")

print("Исходные значения:")
print("Первая аудитория:", first_aud)
print("Вторая аудитория:", second_aud)

third = first_aud
first_aud = second_aud
second_aud = third

print("После обмена:")
print("Первая аудитория:", first_aud)
print("Вторая аудитория:", second_aud)