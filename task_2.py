import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    sample = set()
    if (min < 1) or (max > 1000) or ((quantity <= min) and (quantity >= max)):      #перевірка відповідності заданих параметрів
        print(s_list = list(sample))
    else:
        while len(sample) < quantity:                                               #додаємо унікальні елементи, поки їх к-ть не задовольнить умову
            el = random.randint(min, max)
            sample.add(el)
    s_list = list(sample)                                                           #записуємо елементи в список
    s_list.sort()                                                                   #відстровуємо за зростанням
    print(s_list)


get_numbers_ticket(1,49,6)