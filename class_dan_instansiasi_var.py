class Hero:
    # class variabel
    jumlahHero = 0

    def __init__(self, inputName, inputHealt, inputArmor, inputPower):
        # Instansiasi Variabel / attribut
        self.name = inputName
        self.healt = inputHealt
        self.armor = inputArmor
        self.power = inputPower

        # Mengakses class variabel yang ada diluar method
        # jumlahHero pada class variabel akan bertambah satu, setiap kali class Hero() di inisialisasi
        Hero.jumlahHero += 1


# inisialisasi class Hero
hero1 = Hero("Luffy", 100, 90, 100)
print("Hero", Hero.jumlahHero, hero1.name)
hero2 = Hero("Zoro", 100, 80, 90)
print("Hero", Hero.jumlahHero, hero2.name)
hero3 = Hero("Sanji", 100, 70, 80)
print("Hero", Hero.jumlahHero, hero3.name)
