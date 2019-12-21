class Hero:

    def __init__(self, name, category, attackPower, defensePower):
        self.__name = name
        self.__category = category
        self.__attack = attackPower
        self.__defense = defensePower

    @property   # Merubah method menjadi bersifat variabel
    def info(self):
        ''' Setiap nilai dari variabel akan update, bilamana ada pemanggilan fungsi setter yang dilakukan oleh user '''

        print("\t", self.__name)
        print("========================")
        print("Category : {}".format(self.__category))
        print("Power \t : {}".format(self.__attack))
        print("Defense\t: {}".format(self.__defense))

    @property  # Decorator sebagai patokan untuk method getter dan setter
    def category(self):
        pass

    @category.getter    # Decorator untuk menandakan method Getter
    def category(self):
        return self.__category

    @category.setter    # Decorator untuk menandakan method Setter
    def category(self, newValue):
        self.__category = newValue

    @category.deleter  # Decorator untuk menandakan method Deleter
    def category(self):
        self.__category = None


luffy = Hero("Luffy", "Front Line", 70, 90)
luffy.info  # Memanggil fungsi info()
print("--------------")
print(luffy.category)

luffy.category = "Middle Line"
luffy.info  # Memanggil fungsi info()
print("--------------")
print(luffy.category)

del luffy.category
luffy.info  # Memanggil fungsi info()
print("--------------")
print(luffy.category)
