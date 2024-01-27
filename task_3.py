import re

def normalize_phone(phone_number: str) -> str :
    number = re.sub(r"\D","",phone_number)          # видаляємо всі символи окрім цифр
    if len(number) == 10:                           # у номера не вистачає коду "+38"
        form_number = "+38"+number
    elif len(number) == 11 :                        # у номера не вистачає коду "+3"
        form_number = "+3"+number
    else:                                           # у номера не вистачає коду "+"
        form_number = "+"+number
    return form_number

print(normalize_phone("    +38(050)123-32-34"))
print(normalize_phone("     0503451234"))
print(normalize_phone("(050)8889900"))
print(normalize_phone("38050-111-22-22"))
print(normalize_phone("8050 111 22 11   "))