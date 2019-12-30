from Hero import HeroIntelligent, HeroStrength


lina = HeroIntelligent("Lina")
slandar = HeroStrength("Slandar")

lina.show_info()
slandar.show_info()
lina.gainExp = 100
slandar.gainExp = 150

print("=========Level Naik=========")

lina.show_info()
slandar.show_info()
