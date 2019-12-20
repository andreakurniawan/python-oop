''' Prinsip Enkapsulasi '''
''' 1. Buat semua variabel bersifat variabel '''
''' 2. Gunakan metode getter dan setter untuk mengambil nilai dari variabel '''


class Hero:

    def __init__(self, name, health, attPower):
        # Variabel Private
        self.__name = name
        self.__health = health
        self.__attPower = attPower

    # Getter
    ''' Digunakan untuk mengambil nilai dari variabel private '''
    def getName(self):
        return self.__name


    def getHealth(self):
        return self.__health


    def serang(self, attackValue):
        self.__health -= attackValue


    # Setter
    ''' Digunakan untuk merubah nilai dari variabel private, dalam arti lain yakni merubah variabel private menjadi public secara tidak langsung. '''
    def setAttPower(self, valAttack):
        self.__attPower = valAttack
        return self.__attPower


zoro = Hero("Zoro", 80, 10)

print(zoro.getName())
print(zoro.getHealth())
zoro.serang(30)
print(zoro.getHealth())
print(zoro.setAttPower(20))
