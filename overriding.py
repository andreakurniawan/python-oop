''' Override adalah suatu metode yang digunakan untuk menimpa method yang sudah ada (biasanya method pada super class), yang dilakukan didalam SubClass, yang bertujuan untuk menambahkan / memodifikasi method yang sudah ada, agar lebih dinamis sesuai kebutuhan Subclass tersebut. '''


# Super Class
class Characters:
    __jumlahCharacter = 0

    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def info(self):
        print("{}, Health : {}".format(self.__name, self.__health))


# SubClass
class Younkou(Characters):
    def __init__(self, name):
        super().__init__(name, 1000)

    # Override terhadap mthod info() pada super class diatas.
    def info(self):
        print("{} (Younkou), Health = {}".format(
            self._Characters__name, self._Characters__health))


class Haki(Characters):
    def __init__(self, name):
        super().__init__(name, 800)


# Pemanggilan subclass
kaido = Younkou("Kaido")
# Memanggil method override dalam class Younkou()
kaido.info()

luffy = Haki("Luffy")
# Memanggil method biasa pada Super Class
luffy.info()
