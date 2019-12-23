''' Rules '''
''' 1. Menggunakan system Level dan Experience
    2. Nilai dari instansiasi variabel pada object berubah setiap kenaikan level
    3. Batas Nilai Experience adalah 100 (contoh)'''


class Hero:
    # Class variabel, untuk menampung banyaknya jumlah hero
    __jumlahHero = 0

    # Construct
    def __init__(self, name, health, attPower, armor):
        # Instansiasi Variabel untuk menampung nilai awal
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor
        self.__level = 1
        self.__exp = 0
        # Instansiasi Variabel untuk menampung nilai maximal, bilamana level naik
        self.__healthMax = self.__healthBase * self.__level
        self.__attPower = self.__attPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level
        # Instansiasi Variabel untuk menampung nilai yang sedang berlangsung
        self.__health = self.__healthMax

        # Nilai class variabel berubah setiap kali membuat hero baru
        Hero.__jumlahHero += 1

    # Property untuk menampilkan informasi dari Hero
    @property
    def info(self):
        return "{} (Level {}) : \n\t Health\t = {}/{} \n\t Power\t = {} \n\t Armor\t = {}".format(self.__name, self.__level, self.__health, self.__healthMax, self.__attPower, self.__armor)

    # Property untuk merubah nilai instance variabel setiap kali level bertambah
    @property
    def gainExp(self):
        pass

    # Method Setter untuk menambahkan nilai experience Hero
    @gainExp.setter
    def gainExp(self, addExp):
        # Nilai dari instance variabel __exp ditambah nilai parameter yg dikirim pada saat pemanggilan setter
        self.__exp += addExp
        # Untuk naik level, nilai __exp harus lebih atau sama dengan 100
        if self.__exp >= 100:
            print(self.__name, "Level UP")
            self.__level += 1
            # Mereset ulang nilai __exp
            self.__exp -= 100
            # Men-set ulang instance variabel yg digunakan untuk menampung nilai maximal
            self.__healthMax = self.__healthBase * self.__level
            self.__attPower = self.__attPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level


naruto = Hero("Naruto", 100, 10, 5)
print(naruto.info)

# Pemanggilan setter gainExp()
naruto.gainExp = 50
naruto.gainExp = 50

print(naruto.info)
