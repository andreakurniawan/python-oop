# Class ada sebuah cetak biru untuk merepresentasikan sebuah object yang akan dibuat
class Hero:
    # def __init__() adalah salah satu magic keyword yang ada di python
    # Merupan sebuah contruct method
    # Method yang pertama kali dijalankan pada saat sebuah kelas dipanggil
    def __init__(self, inputName, inputHealt, inputArmor, inputPower):
        # self, adalah parameter wajib pada sebuah construct method
        self.name = inputName
        self.healt = inputHealt
        self.armor = inputArmor
        self.power = inputPower


# inisialisasi class Hero
hero1 = Hero("Luffy", 100, 90, 100)
hero2 = Hero("Zoro", 100, 80, 90)
hero3 = Hero("Sanji", 100, 70, 80)

# __dict__ adalah fungsi untuk mencetak semua attribut pada class yang telah di inisialisasi
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
