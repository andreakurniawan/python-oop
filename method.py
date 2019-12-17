class Character:
    sumCharacter = 0

    def __init__(self, name, category, attack, valAttack, valDefense):
        self.name = name
        self.category = category
        self.attack = attack
        self.valAttack = valAttack
        self.valDefense = valDefense

        Character.sumCharacter += 1


    ''' Method dibagi menjadi 3 berdasarkan nilai kembali yang dihasilkan. '''
    # 1. Method tanpa argumen dan tanpa return (void method)
    def infoCharacter(self):
        print("Name \t\t: ", self.name)
        print("Category \t: ", self.category)
        print("Attack \t\t: ", self.attack)
        print("Value Attack \t: ", self.valAttack)
        print("Defense \t: ", self.valDefense)


    # 2. Method dengan argument dan tanpa return
    def inputOwner(self, ownerName):
        name = self.name + "->" + ownerName
        print(name)


    # 3. Method dengan argument dan return
    def UpgradeDefense(self, valUp):
        self.valDefense += valUp


character1 = Character("Arlong", "Fire", "FireBall", 80, 60)

character1.infoCharacter()
character1.inputOwner("Andrea")
character1.UpgradeDefense(10)
