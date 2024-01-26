from datetime import datetime

def get_days_from_today(date:str):
    today = datetime.now()                                  #отримуємо сьогоднішню дату
    try:
        date_dt = datetime.strptime(date, "%Y-%m-%d")       #перетворюємо введену дату в формат datetime
        between = today - date_dt                           #знаходимо к-ть днів між датами
        if today.date() > date_dt.date() :                  #якщо задана дата минула
            print(between.days)
        elif today.date() < date_dt.date() :                #якщо задана дата ще не настала
            print(between.days)
        else:                                               #якщо задана сьогоднішня дата
            print(f"Ви ввели сьогоднішню дату")
    except ValueError:                                      #якщо введено дату в невірному форматі
        print("Ви ввели дату в невірному форматі. \nВведіть дату у форматі РРРР-ММ-ДД: ")

get_days_from_today("2015-08-29")
