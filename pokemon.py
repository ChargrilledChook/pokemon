import math

class Pokemon:

	def __init__(self, name, type, health, max_health, damage, s_damage, is_ko = False, level = 1):
		self.name = name
		self.type = type
		self.health = health
		self.max_health = max_health
		self.damage = damage
		self.s_damage = s_damage
		self.is_ko = is_ko
		self.level = level

	def speak(self):
		print(f'{self.name}!')

	def attack(self, other):
		other.health -= self.damage

	def damage_calculator(self, other):
		if self.type == 'Grass' and other.type == 'Fire':
			return 0.5
		if self.type == 'Grass' and other.type == 'Water':
			return 2
		if self.type == 'Water' and other.type == 'Grass':
			return 0.5
		if self.type == 'Water' and other.type == 'Fire':
			return 2
		if self.type == 'Fire' and other.type == 'Water':
			return 0.5
		if self.type == 'Fire' and other.type == 'Grass':
			return 2
		if self.type == other.type:
			return 1

	def s_attack(self, other):
		other.health -= math.floor(self.damage_calculator(other) * self.damage)

	def heal(self, potion):
		self.health += potion
		if self.health > self.max_health:
			self.health = self.max_health

	def knocked_out(self):
		if self.health <= 0 :
			self.is_ko == True


