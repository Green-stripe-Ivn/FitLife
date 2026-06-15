import time #Импортируем модуль time для замедленного вывода с помощью аргумента flush и функции sleep


LITRE = 1000 #Константы для расчета потребления воды
MILLILITER_PER_KG = 30
# Проект FitLife - MVP версия 1.0
print('Проект FitLife', flush=True)
time.sleep(1) #Вывод версии
print('*'*40)
print('MVP версия 1.0')

# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_name = input('Приветствуем тебя в нашей фитнес программе. Как твоё имя: ' )
user_name = user_name.title()
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
user_age = input(f'Очень приятно, {user_name}. Нам важно знать твой возраст: ')
user_age = int(user_age.lower())


# 2. Сбор данных
user_weight = input('Укажи свой вес (кг): ' )
user_weight = float(user_weight)
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
user_height = input('Укажи свой рост (м): ') #Попробовать try/except
user_height = float(user_height)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = user_weight / user_height ** 2
bmi = round(bmi,1)


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_ml = user_weight * MILLILITER_PER_KG
water_l = water_ml / LITRE
water_needed = water_l


# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f'\nГотовы твои полезные рекомендации, {user_name}:')
print(f'В возрасте {user_age}, при Индексе Массы Тела {bmi:.1f}, тебе необходимо выпивать около {water_needed:.1f} л. воды в день.')
print("\nРасчет окончен. Будьте здоровы!")