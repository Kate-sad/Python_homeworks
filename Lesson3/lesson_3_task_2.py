from smartphone import Smartphone

catalog = [
    Smartphone("Aple", "13", "+79999999999"),
    Smartphone("Sony", "experia 12 mini", "+79888888888"),
    Smartphone("Samsung", "Galaxy", "+79777777777"),
    Smartphone("Xiaomi", "12 Pro", "+79666666666"),
    Smartphone("Aple", "16", "+79555555555")
]

for x in catalog:
    print(f"{x.brandPhone} - {x.modelPhone}. {x.numberPhone}")
