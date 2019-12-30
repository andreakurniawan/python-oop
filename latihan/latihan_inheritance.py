from Hero import HeroIntelligent, HeroStrength


lina = HeroIntelligent("Lina")
slandar = HeroStrength("Slandar")

lina.show_info()
slandar.show_info()

# Naik Level
lina.gainExp = 200
slandar.gainExp = 250

lina.show_info()
slandar.show_info()
