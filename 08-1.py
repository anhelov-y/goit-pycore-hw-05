def caching_fibonacci():
    cache = {}  # створюємо пустий словник

    def fibonacci(n):
        # переверка правильності умови
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        # Перевірка наявності у нашому словнику cache 
        if n in cache:
            return cache[n]

        # За відстуності у словнику, обчислити та зберігти 
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Виклик функції
fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610
print(fib(20))  # 6765
print(fib(17))  # 1597