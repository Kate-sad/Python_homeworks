def month_to_season(number_month):
    if number_month == 12 or number_month == 1 or number_month == 2:
        print("Зима")
    elif number_month == 3 or number_month == 4 or number_month == 5:
        print("Весна")
    elif number_month == 6 or number_month == 7 or number_month == 8:
        print("Лето")
    elif number_month == 9 or number_month == 10 or number_month == 11:
        print("Осень")
    else:
        print("Такого месяца не существует")


number_month = int(input("введите номер месяца: "))
month_to_season(number_month)
