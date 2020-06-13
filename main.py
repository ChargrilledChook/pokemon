from pokemon import Pokemon
from dummy import Dummy

bulb = Pokemon('Bulbasaur', 'Grass', 10, 10, 3, 2)
doug = Dummy('Doug', 69)

bulb.speak()

print(doug.health)
bulb.attack(doug)
print(doug.health)
