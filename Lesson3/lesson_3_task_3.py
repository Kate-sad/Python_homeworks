from address import Address
from mailing import Mailing

to_adress = Address("123456", "Ялта", "Верхняя", "15", "4")
from_adress = Address("987654", "Волгоград", "Нижняя", "15", "3")
my_cost = 12
my_track = "tgft68759hvbh"
my_mailing = Mailing (to_adress, from_adress, my_cost, my_track)

print(my_mailing)
