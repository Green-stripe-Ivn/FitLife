import time  # Импортируем модуль time для замедленного вывода

LITRE = 1000  # Константы для расчета потребления воды
MILLILITER_PER_KG = 30
# Проект FitLife - MVP версия 1.0
print('Проект FitLife', flush=True)
time.sleep(1)  # Вывод версии
print('*' * 40, 'MVP версия 1.0', sep='\n')

#  1. Знакомство
# Спрашиваем имя
user_name = input('Приветствуем тебя в нашей фитнес программе. Как твоё имя: ')
user_name = user_name.title()
# Спрашиваем возраст
user_age = input(f'Очень приятно, {user_name}. Нам важно знать твой возраст: ')
user_age = int(user_age.lower())

# 2. Сбор данных
user_weight = input('Укажи свой вес (кг): ')
user_weight = float(user_weight)
user_height = input('Укажи свой рост (м): ')
user_height = float(user_height)
# и сохрани в user_height (тип float)

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / user_height ** 2
bmi = round(bmi, 1)
# Подсчет воды: вес * 30 мл
water_ml = user_weight * MILLILITER_PER_KG
water_l = water_ml / LITRE
water_needed = water_l

# 4. Вывод красивого результата
print(f'\nГотовы твои полезные рекомендации, {user_name}:',
      f'В возрасте {user_age}, при Индексе Массы Тела {bmi:.1f}, '
      f'тебе необходимо выпивать около {water_needed:.1f} л. воды в день.',
      'Расчет окончен. Будьте здоровы!', sep='\n')
