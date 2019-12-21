class Hero:

    # Private class variabel
    __jumlahHero = 0

    def __init__(self, name, health):
        # Private instance variabel
        self.__name = name
        self.__health = health
        Hero.__jumlahHero += 1

    # Getter, untuk mengambil nilai dari variabel __jumlahHero yang bersifat private
    # static method (decorator)
    # Menandakan bahwa method dibawahnya adalah method static, tdk memiliki argument
    @staticmethod  # method yg nempel ke object dan class
    def getJumlah():
        return Hero.__jumlahHero

    # method yang memiliki argument, tetapi pada saat pemanggilan tidak perlu mengirimkan suatu parameter
    # Arugment disini merunjuk pada nama class yg memiliki class variabel bersifat private
    @classmethod
    def getJumlah2(cls):
        return cls.__jumlahHero


nami = Hero("Nami", 80)
cupper = Hero("Cupper", 76)
print(nami.getJumlah())
print(Hero.getJumlah2())
