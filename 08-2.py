import re  

# шукаємо всі числа в тексті через генератор 
def generator_numbers(text):
    numbers = re.findall(r'\d+\.\d+|\d+', text)
    for num in numbers:
        yield float(num)  # повертаємо по одному числу


# функція для підрахунку загального прибутку
def sum_profit(text, func):
    total = 0
    for number in func(text):  # перебираємо всі числа з генератора
        total += number
    return total


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
text2 = "Загальний дохід працівника складається з декількох частин: 2000.05 як основний дохід, доповнений додатковими надходженнями 100.45 і 678.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

total_income2 = sum_profit(text2, generator_numbers)
print(f"Загальний дохід: {total_income2}")
