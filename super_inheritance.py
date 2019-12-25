# Super Class
class Characters:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def info(self):
        print("{}, Health {}".format(self.name, self.health))


# SubClass
class Hero_Fire(Characters):
    def __init__(self, name):
        ''' super(), artinya mewakili nama dari super class '''
        super().__init__(name, 80)
        ''' method ini akan langsung dijalankan, ketika pemanggilan subclass, tanpa harus memanggil nama methodnya. '''
        super().info()


# Pemanggilan class super Class
nami = Characters("Nami", 70)
nami.info()

# Pemanggilan SubClass
sanji = Hero_Fire("Sanji")
