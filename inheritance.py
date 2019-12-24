""" Inheritance (Pewarisan), adalah suatu class yang mewarisi semua property dan method dari class tertentu. Class yang menjadi pewaris disebut 'Super Class', sedangkan class yang mewarisi disebut 'Sub Class'."""


# Super Class
class Hero:

    def __init__(self, name, health):
        # Property/Variabel yang dimiliki Super Class
        self.name = name
        self.health = health

    # Method yang dimiliki Super Class
    @property
    def info(self):
        return "Name Hero : {}, Health : {}".format(self.name, self.health)


# Sub Class, yang mewarisi method dan property/variabel dari Super Class
class Hero_api(Hero):
    pass


# Pemanggilan Super Class
luffy = Hero("Luffy", 100)
print(luffy.info)

# Pemanggilan Sub Class
zoro = Hero_api("Zoro", 98)
print(zoro.info)
print(help(zoro))
