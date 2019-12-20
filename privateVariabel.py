class Hero:
    # Class Variabel
    jumlah = 0

    def __init__(self, name, health):
        ''' Variabel Public bersifat publik, bisa diakses ketika pemanggilan fungsi dilakukan. '''
        # variabel public
        self.name = name
        self.health = health

        ''' Variabel Private bersifat tertutup, biasanya digunakan untuk enkapsulasi data. '''
        # variabel private
        self.__private = "Privasi"

        ''' Variabel Protected, hampir sama dengan variabel publik, hanya saja bersifat convensional yang hanya boleh digunakan untuk kelas itu saja. '''
        # variabel protected
        self._protected = "Proteksi"


jugo = Hero("Jugo", 100)
print(jugo.__dict__)
print(jugo._protected)
