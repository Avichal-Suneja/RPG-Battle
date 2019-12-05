'''
    RPG BATTLE
    Coded by - Avichal Suneja
'''

# Importing various classes to be used in the main file
from Classes.game import Person, bcolors
from Classes.magic import spell
from Classes.inventory import items
import random


# Black magic list:
fire    = spell("Fire", 10, 100, "Black")
thunder = spell("Thunder", 10, 100, "Black")
quake   = spell("Quake", 14, 140, "Black")
meteor  = spell("Meteor", 20, 200, "Black")

# White magic list:
cure = spell("Cure", 15, 100, "White")
cura = spell("Cura", 20, 200, "White")

# Creating some items:
potion       = items("Potion", "potion", "Heals 50 HP", 50)
mega_potion  = items("Mega Potion", "potion", "Heals 100 HP", 100)
super_potion = items("Super Potion", "potion", "Heals 500 HP", 500)
elixir       = items("Elixir", "elixir", "Restores full HP/MP of one party member", 9999)
mega_elixir  = items("Mega Elixir", "mega_elixir", "Restores full HP/MP of all party members", 9999)
grenade      = items("Grenade", "attack", "Deals a damage of 500 HP", 500)

# Creating arrays of spells and items
player_spells = [fire, thunder, quake, meteor, cure, cura]
player_items  = [{"item": potion, "qty":15}, {"item": mega_potion, "qty":5},
                {"item": super_potion, "qty":3}, {"item": elixir, "qty":3},
                {"item": mega_elixir, "qty":1},{"item": grenade, "qty":1}]


# initialising players:
player1 = Person("Avichal:", 500, 45, 60, 34, player_spells, player_items)
player2 = Person("Nick   :", 500, 45, 60, 34, player_spells, player_items)
player3 = Person("Robot  :", 500, 45, 60, 34, player_spells, player_items)
# initialising enemies:
enemy1  = Person("Imp    :", 300, 40, 50, 20,player_spells,player_items) 
enemy2  = Person("Villain:", 1200, 100, 120, 10, player_spells,player_items)
enemy3  = Person("Imp    :", 300, 20, 50, 20,player_spells,player_items)
enemies = [enemy1, enemy2, enemy3]
players = [player1, player2, player3]
print("\n\n")

# Header and set loop to true
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)
running = True

while running:
	print("===========================")
	print("\n\n")
	print("NAME                      HP                                      MP          ")
	# Getting the health bars and magic point bars of players and enemies
	for player in players:
		player.get_stats()
	print("\n")
	for enemy in enemies:
		enemy.get_enemy_stats()
		print("\n")


	 
    # Action for all the players one by one starts here
	for player in players:
		
		
		player.choose_action()
		choice = input("Enter choice: ")
		
		index = int(choice)-1

        # Conditon if player choses to attack
		if index==0:
		    dmg = player.generate_damage()
		    enemy = player.choose_target(enemies)
		    enemies[enemy].take_damage(dmg)
		    print("You attacked", enemies[enemy].name, "for",dmg,"Damage")
		    if enemies[enemy].get_hp() == 0:
		    	print(bcolors.FAIL, enemies[enemy].name.replace(" ",""), "is dead", bcolors.ENDC)
		    	del enemies[enemy]

        # Condition if player wants to use magic
		elif index==1:
		    player.choose_magic()
		    magic_choice = int(input("Choose magic: "))-1

		    if magic_choice == -1:
			    continue
		
		    spell = player.magic[magic_choice]
		    magic_dmg = spell.generate_damage()

		    if spell.cost > player.get_mp():
			    print(bcolors.FAIL + "You don't have enough MP" + bcolors.ENDC)
			    continue

		    player.reduce_mp(spell.cost)

		    if spell.kind == "White":
			    player.heal(magic_dmg)
			    print(bcolors.OKGREEN,spell.name,"healed",magic_dmg,"HP",bcolors.ENDC)
		    elif spell.kind == "Black":
		    	enemy = player.choose_target(enemies)
		    	print(bcolors.FAIL,"Spell ",spell.name ," inflicted "+ str(magic_dmg) +
		    	      " Damage to",enemies[enemy].name.replace(" ",""), bcolors.ENDC)
		    	enemies[enemy].take_damage(magic_dmg)
		    	if enemies[enemy].get_hp() == 0:
		    		print(bcolors.FAIL, enemies[enemy].name.replace(" ",""), "is dead", bcolors.ENDC,"\n")
		    		del enemies[enemy]

		    	
		# Condition if player wants to use items    			    			    			    
		elif index == 2:
			player.choose_items()
			item_choice = int(input("Choose item: ")) - 1
			item = player.items[item_choice]["item"]

			if item_choice == -1:
				continue

			if player.items[item_choice]["qty"] == 0:
				print(bcolors.FAIL,"Item requested is out of stock!",bcolors.ENDC)
				continue

			player.items[item_choice]["qty"] -= 1
			if item.kind == "potion":
				player.heal(item.prop)
				print(bcolors.OKGREEN,item.name,"heals for",item.prop,"HP",bcolors.ENDC)

			elif item.kind == "mega_elixir":
				# Restoring HP and MP of all party members
				for player in players:
					player.mp = player.maxmp
					player.hp = player.maxhp

				print(bcolors.OKGREEN,item.name,"fully restores HP/MP of all members",bcolors.ENDC)

			elif item.kind == "elixir":
				player.mp = player.maxmp
				player.hp = player.maxhp
				print(bcolors.OKGREEN,item.name,"fully restores HP/MP of current member",bcolors.ENDC)
				    								
			elif item.kind == "attack":
				enemy = player.choose_target(enemies)
				enemies[enemy].take_damage(item.prop)
				print(bcolors.FAIL,item.name,"deals",item.prop,"damage to",enemies[enemy].name.replace(" ",""),bcolors.ENDC)
				if enemies[enemy].get_hp() == 0:
					print(bcolors.FAIL, enemies[enemy].name.replace(" ",""), "is dead", bcolors.ENDC)
					del enemies[enemy]

	
	# Checking if enemy won and terminating the loop
	if len(players) == 0:
		print(bcolors.FAIL + "Your enemy has defeated you" + bcolors.ENDC)
		exit(0)

	# Checking if player won and terminating the loop
	elif len(enemies) == 0:
		print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
		exit(0)

	# Enemy's Artificial Intelligence (not really)   		    			    								
	for enemy in enemies:
	    enemy_choice = int(enemy.intelligent_choice())

	    # Enemy's Intelligent attack 
	    if enemy_choice == 1:
	    	mini = players[0].get_hp()
	    	i=0
	    	# Finding the player with minimum HP to attack the weakest player
	    	for player in players:
	    		if player.get_hp() < mini:
	    			i+=1
	    	enemy_dmg = enemy.generate_damage()
	    	if i == 0:
	    		players[i].take_damage(enemy_dmg)
	    	elif i == 1:
	    		players[i].take_damage(enemy_dmg)
	    	elif i == 2:
	    		players[i].take_damage(enemy_dmg)
	    	print( enemy.name,"attacked "+ players[i].name + " for",enemy_dmg,"Damage")
	    	if players[i].get_hp() == 0:
	    		print(bcolors.FAIL, players[i].name.replace(" ",""), "is dead", bcolors.ENDC,"\n")
	    		del players[i]
	    	print("---------------------------------------------")

        # Enemy's Intelligent Magic Choice
	    if enemy_choice == 2:
	    	if enemy.get_mp() >= 40:
	    		no_of_spell = 3
	    	elif enemy.get_mp() >=14 and enemy.get_mp() < 40:
	    		no_of_spell = random.randrange(0,3)
	    	spell0 = enemy.magic[no_of_spell]
	    	spell_dmg = spell0.generate_damage()
	    	enemy.reduce_mp(spell0.cost)
	    	mini = players[0].get_hp()
	    	i=0
	    	# Finding the player with minimum HP to attack the weakest player
	    	for player in players:
	    		if player.get_hp() < mini:
	    			i+=1
	    	if i == 0:
	    		players[i].take_damage(spell_dmg)
	    	elif i == 1:
	    		players[i].take_damage(spell_dmg)
	    	elif i == 2:
	    		players[i].take_damage(spell_dmg)
	    	print(bcolors.FAIL,enemy.name," attacked "+ players[i].name + " with Meteor for",spell_dmg,"Damage",bcolors.ENDC)
	    	if players[i].get_hp() == 0:
	    		print(bcolors.FAIL, players[i].name.replace(" ",""), "is dead", bcolors.ENDC,"\n")
	    		del players[i]
	    	print("---------------------------------------------")

        # Enemy Heals itself
	    if enemy_choice == 3:
	    	if enemy.get_mp() >= 15 and enemy.get_mp() < 20:
	    		no_of_spell = 4
	    	elif enemy.get_mp() >= 20:
	    		no_of_spell = 5

	    	spell0 = enemy.magic[no_of_spell]
	    	spell_dmg = spell0.generate_damage()

	    	enemy.heal(spell_dmg)
	    	enemy.reduce_mp(spell0.cost)
	    	
	    	print(bcolors.OKGREEN,spell0.name,"healed",enemy.name,"for",spell_dmg,"HP",bcolors.ENDC)

''' -------------------------------------  END OF CODE ---------------------------------------------------'''




	
	

	
	
	
		
		
					
					
	

	



    
    

   
    
    
    


	    
	    

	    

	    

	    

	    
	    

		



