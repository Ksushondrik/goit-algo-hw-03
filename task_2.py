import random

min = int(input("Введіть мінімальне значення діапазону вибірки: "))
max = int(input("Введіть максимальне значення діапазону вибірки:"))
quantity = int(input("Введіть кількість чисел у виграшній комбінації: "))

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:                              # створюємо функцію вибірки
    sample = []
    if (min < 1) or (max > 1000) or (max <= quantity <= min) or (quantity >= (max-min)):        # перевіряємо задані параметри
        print(f"Спробуйте ще раз! {sample}")
    else:
        while (len(sample) < quantity) :                                                        # додаємо випадкові числа в список
            el = random.randint(min, max)
            if el not in sample :
                sample.append(el)
    sample.sort()                                                                               # відсортовуємо за зростанням
    return sample

print(get_numbers_ticket(min, max, quantity))