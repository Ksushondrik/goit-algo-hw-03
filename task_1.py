from datetime import datetime

def get_days_from_today():
    today = datetime.now()                                                      # отримуємо сьогоднішню дату
    date = input("Введіть дату, що Вас цікавить у форматі \"РРРР-ММ-ДД\": ")    # отримуємо дату від користувача
    try:
        date_dt = datetime.strptime(date, "%Y-%m-%d")                           # перетворюємо введену дату в формат datetime
        between = today - date_dt                                               # знаходимо к-ть днів між датами
        if today.date() > date_dt.date() :                                      # якщо задана дата минула
            print(f"Минуло: {between.days} дня(-і/-ів/-ень)")
        elif today.date() < date_dt.date() :                                    # якщо задана дата ще не настала
            print(f"Залишилось: {-between.days} дня(-і/-ів/-ень)")
        else:                                                                   # якщо задана сьогоднішня дата
            print(f"Ви ввели сьогоднішню дату")
    except ValueError:                                                          # якщо введено дату в невірному форматі
        print("Ви ввели дату в невірному форматі. \nВведіть дату у форматі РРРР-ММ-ДД!")

get_days_from_today()
