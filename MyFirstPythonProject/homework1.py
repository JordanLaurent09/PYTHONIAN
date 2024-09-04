import random
#Задание 8

def generate_random_number():
  # Запрашиваем у пользователя границы диапазона
  lower_bound = int(input("Введите нижнюю границу диапазона: "))
  upper_bound = int(input("Введите верхнюю границу диапазона: "))

  # Генерируем случайное число в заданном диапазоне
  random_number = random.randint(lower_bound, upper_bound)

  # Выводим сгенерированное число на экран
  print(f"Случайное число в диапазоне от {lower_bound} до {upper_bound}: {random_number}")

if __name__ == "__main__":
  generate_random_number()




"""""""""""""""""""""""""""""
#Задание 7

def celsius_to_fahrenheit(celsius):
  return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5/9

def main():
  print("Выберите опцию:")
  print("1. Перевести из Цельсия в Фаренгейт")
  print("2. Перевести из Фаренгейта в Цельсий")

  choice = input("Введите 1 или 2: ")

  if choice == '1':
      celsius = float(input("Введите температуру в градусах Цельсия: "))
      fahrenheit = celsius_to_fahrenheit(celsius)
      print(f"Температура в градусах Фаренгейта: {fahrenheit:.2f}")
  elif choice == '2':
      fahrenheit = float(input("Введите температуру в градусах Фаренгейта: "))
      celsius = fahrenheit_to_celsius(fahrenheit)
      print(f"Температура в градусах Цельсия: {celsius:.2f}")
  else:
      print("Некорректный выбор. Пожалуйста, введите 1 или 2.")

if __name__ == "__main__":
  main()
"""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""
#Задание 6

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
      return "Ошибка: деление на ноль!"
  return x / y

def calculator():
  print("Выберите операцию:")
  print("1. Сложение")
  print("2. Вычитание")
  print("3. Умножение")
  print("4. Деление")

  try:
      choice = input("Введите номер операции (1/2/3/4): ")

      if choice in ['1', '2', '3', '4']:
          num1 = float(input("Введите первое число: "))
          num2 = float(input("Введите второе число: "))

          if choice == '1':
              print(f"{num1} + {num2} = {add(num1, num2)}")

          elif choice == '2':
              print(f"{num1} - {num2} = {subtract(num1, num2)}")

          elif choice == '3':
              print(f"{num1} * {num2} = {multiply(num1, num2)}")

          elif choice == '4':
              result = divide(num1, num2)
              print(f"{num1} / {num2} = {result}")

      else:
          print("Неверный ввод. Пожалуйста, выберите правильную операцию.")

  except ValueError:
      print("Ошибка: введите числовое значение.")

calculator()


"""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""
#Задание 5

def check_even_odd(number):
  if number % 2 == 0:
      return "Число четное"
  else:
      return "Число нечетное"

# Запрос ввода от пользователя
try:
  user_input = int(input("Введите целое число: "))
  result = check_even_odd(user_input)
  print(result)
except ValueError:
  print("Пожалуйста, введите корректное целое число.")


"""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""
#Задание 4
def convert_seconds_to_dhms(seconds):
  # Вычисляем количество дней
  days = seconds // 86400
  seconds %= 86400

  # Вычисляем количество часов
  hours = seconds // 3600
  seconds %= 3600

  # Вычисляем количество минут
  minutes = seconds // 60

  # Оставшиеся секунды
  seconds %= 60

  # Формируем строку в нужном формате
  return f"{days}:{hours:02}:{minutes:02}:{seconds:02}"

# Пример использования функции
total_seconds = int(input("Введите количество секунд: "))
formatted_time = convert_seconds_to_dhms(total_seconds)
print("Формат времени (дни:часы:минуты:секунды):", formatted_time)


"""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""
#Задание 3
def find_fraction(decimal_number):
  # Преобразуем вещественное число в дробь
  fraction = Fraction(decimal_number).limit_denominator()

  # Выводим результат в требуемом формате
  print(f"{decimal_number} = {fraction.numerator}/{fraction.denominator}")

# Пример использования функции
find_fraction(14.375)

"""""""""""""""""""""""""""""


"""""""""""""""""""""""""""""
# Задание 1
def calculate_expression(n):
  #Преобразуем число в строку
  n_str = str(n)

  #Создадим числа n и nn
  nn = int(n_str * 2)  
  nnn = int(n_str * 3)

  # Считаем сумму n + nn + nnn
  result = n + nn + nnn

  return result

# Пример использования функции
n = int(input("Введите целое число n: "))
result = calculate_expression(n)
print("Результат выражения n + nn + nnn:", result)

"""""""""""""""""""""""""""""

"""""""""""""""""""""""""""""
#Задание 2
def print_even_numbers_until_237(numbers):
  for number in numbers:
      if number == 237:
          break
      if number % 2 == 0:
          print(number)

# Пример использования функции
numbers_list = [1, 4, 6, 8, 10, 13, 237, 14, 16, 18]
print_even_numbers_until_237(numbers_list)

"""""""""""""""""""""""""""""

