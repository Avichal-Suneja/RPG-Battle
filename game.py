import random
from . magic import spell
from . inventory import items
import os
os.system('cls')


class bcolors:
	HEADER    = '\033[95m'
	OKBLUE    = '\033[94m'
	OKGREEN   = '\033[92m'
	WARNING   = '\033[93m'
	FAIL      = '\033[91m'
	ENDC      = '\033[0m'
	BOLD      = '\033[1m'
	UNDERLINE = '\033[4m'


class Person:
	def __init__(self, name, hp, mp, atk, df, magic, items):
		self.maxhp = hp
		self.hp = hp
		self.maxmp = mp
		self.mp = mp
		self.atkl = atk-10
		self.atkh = atk+10
		self.df = df
		self.magic = magic
		self.items = items
		self.action = ['Attack', 'Magic', 'Items']
		self.name = name

	def generate_damage(self):
		return random.randrange(self.atkl, self.atkh)

	def generate_spell_damage(self, i):
		mgl = self.magic[i]["dmg"] - 5
		mgh = self.magic[i]["dmg"] + 5
		return random.randrange(mgl, mgh)

	def take_damage(self, dmg):
		self.hp -= dmg
		if self.hp < 0:
			self.hp = 0
		return self.hp

	def heal(self, dmg):
		self.hp += dmg
		if self.hp>self.maxhp:
			self.hp = self.maxhp

	def get_hp(self):
		return self.hp

	def get_maxhp(self):
		return self.maxhp

	def get_mp(self):
		return self.mp

	def get_maxmp(self):
		return self.maxmp

	def reduce_mp(self, cost):
		self.mp -= cost

	def get_spell_name(self, i):
		return self.magic[i]["name"]

	def get_spell_mp_cost(self, i):
		return self.magic[i]["cost"]


	def choose_action(self):
		print(bcolors.BOLD+"    "+ self.name+ bcolors.ENDC)
		print( bcolors.OKBLUE + "    ACTIONS:" + bcolors.ENDC)
		i = 1
		for items in self.action:
			print("        ",str(i) + ':', items)
			i += 1

	def choose_magic(self):
		print("\n    ",bcolors.OKBLUE + bcolors.BOLD + "MAGIC:" + bcolors.ENDC)
		i = 1
		for spell in self.magic:
			print("        ",str(i) , '.', spell.name, "(cost:", spell.cost ,")")
			i += 1

	def choose_items(self):
		print("\n    ",bcolors.OKBLUE + bcolors.BOLD + "ITEMS:" + bcolors.ENDC)
		i = 1
		for item in self.items:
			print("        ",str(i), '.', item["item"].name, ":", item["item"].description, "(x", item["qty"],")")
			i +=1

	def get_stats(self):

		hp_bar = int(((self.hp/self.maxhp)*100)/4)
		mp_bar = int(((self.mp/self.maxmp)*100)/10)
		
		print("                           _________________________               __________  ")
		print(bcolors.BOLD + self.name + "          " + str(self.hp) + "/" + str(self.maxhp) + " |" + bcolors.OKGREEN + hp_bar*"█" +(25-hp_bar)*" " + bcolors.ENDC + "|       "
	          + bcolors.BOLD + str(self.mp) + "/" + str(self.maxmp) + " |" + bcolors.OKBLUE +mp_bar*"█"+(10-mp_bar)*" "+
	           bcolors.ENDC +   "| ")

	def get_enemy_stats(self):
		hp_bar = int(((self.hp/self.maxhp)*100)/2)
		if self.name == "villain":
			spaces = 29
		else:
			spaces = 27
		print(spaces*" " + 50*"_")
		print(bcolors.BOLD + self.name + "          " + str(self.hp) + "/" + str(self.maxhp) + " |" +
		 bcolors.FAIL+ hp_bar*"█"+(50-hp_bar)*" " +"|"+bcolors.ENDC)

	def choose_target(self, enemies):
		i = 1
		print("\n", bcolors.FAIL, bcolors.BOLD ,"    TARGET:",bcolors.ENDC)

		for enemy in enemies:
			if enemy.get_hp != 0:
				print(bcolors.BOLD ,str(i),".", enemy.name, bcolors.ENDC)
				i += 1

			
			

		choice = int(input("        Choose Action: ")) - 1
		return choice

	def intelligent_choice(self):
		if self.get_mp() < 10:
			enemy_choice = 1

		elif self.get_hp() > 0.4*self.get_maxhp():
			enemy_choice = 2

		
		elif self.get_hp() <= 0.4*self.get_maxhp():
			enemy_choice = 3

		return enemy_choice






