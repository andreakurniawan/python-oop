class Hero:

    # Contruct Method
    def __init__(self, name, health, attackPower, defense):
        self.name = name
        self.health = health
        self.power = attackPower
        self.defense = defense

    # Fungsi untuk menyerang
    def serang(self, lawan, nilaiSerang):
        print(self.name, "Menyerang", lawan.name, "dengan kekuatan", nilaiSerang)
        # Jika fungsi serang diapnggil, otomatis fungsi diserang() juga terpanggil
        lawan.diserang(self, self.power)

    # Fungsi untuk diserang
    def diserang(self, lawan, sisaNyawa):
        # Mengurangi nilai health dengan nilai serangan lawan
        effectSerang = self.health - sisaNyawa
        print(self.name, "Diserang", lawan.name, ", Nyawa tersisa", effectSerang)


luffy = Hero("Luffy", 100, 40, 30)
flaminggo = Hero("Flaminggo", 100, 35, 25)

luffy.serang(flaminggo, luffy.power)
