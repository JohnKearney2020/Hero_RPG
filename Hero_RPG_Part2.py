#Hero RPG Part 2 by John Kearney
#I am basing this on the finished code for part 1, including all the bonus tasks

import time
import random

class Character:
    def __init__(self, health, power, char_class, p_crit, p_crit_heal, crit_heal_amount, p_dodge, invuln, bounty, armor):
        self.health = health
        self.power = power
        self.char_class = char_class
        self.p_crit = p_crit
        self.p_crit_heal = p_crit_heal
        self.crit_heal_amount = crit_heal_amount
        self.p_dodge = p_dodge
        self.invuln = invuln
        self.bounty = bounty
        self.armor = armor

    def alive(self): #check to see if our character is still alive.
        if self.health <= 0 and self.invuln == False:
            return False
        else:
            return True
    
    def print_status(self):
        if self.char_class == 'Hero':
            time.sleep(1)
            print('--------------------------------------------------------')
            print(f'You have {self.health} health and {self.power} power.')
        else: #leaving this one non-descript so it will work for all monsters
            time.sleep(1)
            print(f'The {self.char_class} has {self.health} health and {self.power} power.')
            print('--------------------------------------------------------')
    
    def attack(self, attackee):
        #Apply any critical strike attack percentage modifiers to the attack first.
        crit_strike_status = False
        if self.p_crit != 0: #if the character has any critical strike modifiers we resolve those first
            crit_rng = random.randint(1, 100) #this represents the % chance of the critical strike being applied
            if crit_rng <= self.p_crit: #attackee.crit_damage_chance allows for different characters with different percent critical strikes
                crit_strike_status = True

        #next, apply any critical healing modifiers to the attack
        crit_heal_status = False
        if attackee.p_crit_heal != 0:
            crit_rng = random.randint(1, 100) #this represents the % chance of the critical heal being applied
            if crit_rng <= attackee.p_crit_heal:
                crit_heal_status = True
        
        #next, apply any dodge modifiers
        attack_dodged = False
        if attackee.p_dodge != 0:
            dodge_rng = random.randint(1,100) #this represents the % chance of a character dodging an attack
            if dodge_rng <= attackee.p_dodge:
                attack_dodged = True
        
        #next, apply any armor modifiers.
        armor_reduction = 0
        has_armor = False
        if attackee.armor != 0: #if the attackee has any armor
            has_armor = True
            armor_reduction = attackee.armor

        if attackee.char_class != 'Hero': #if the hero is attacking a monster. Monsters are getting hit.
            #if attackee.char_class != 'Zombie': #zombies take no damage, so they are excluded here
            if attack_dodged == True: #if the monster dodged an attack from our hero
                print(f'The {attackee.char_class} dodged your attack! You deal no damage to it!')
            elif crit_strike_status == True:
                attackee.health -= self.power * 2 - armor_reduction
                time.sleep(1)
                print(f'Critical Strike! You deal {self.power * 2 - armor_reduction} damage to the {attackee.char_class}.')
                if crit_heal_status == True:
                    attackee.health += attackee.crit_heal_amount
                    time.sleep(1)
                    print(f'Oh no! The {attackee.char_class} regenerated {attackee.crit_heal_amount} health.')
            else:
                attackee.health -= self.power - armor_reduction
                time.sleep(1)
                print(f'You deal {self.power - armor_reduction} damage to the {attackee.char_class}.')
                if crit_heal_status == True:
                    attackee.health += attackee.crit_heal_amount
                    time.sleep(1)
                    print(f'Oh no! The {attackee.char_class} regenerated {attackee.crit_heal_amount} health.')
            # else: #if the monster being attacked is a Zombie
            #     print(f'The {attackee.char_class} appeared to take no damage... *GULP*') #zombies take no damage
        else: #if a monster is attacking the hero
            if attack_dodged == True: #if our hero dodged the attack of the monster
                    print(f'You dodged the attack from the {self.char_class}. You take no damage!')
            elif crit_strike_status == True:
                attackee.health -= self.power * 2 - armor_reduction
                print(f'Aaagh! Critical Strike! The {self.char_class} does {self.power * 2 - armor_reduction} damage to you.')
            else:
                attackee.health -= self.power - armor_reduction
                print(f'The {self.char_class} does {self.power - armor_reduction} damage to you.')

class Item:
    def __init__(self, name, description, cost, inventory):
        self.name = name
        self.description = description
        self.cost = cost
        self.inventory = inventory
        self.items = []
    

def keep_going():
    main()

def main():
    # =====================================================================
    #                         Item Creation
    # =====================================================================
    SuperTonic = Item('SuperTonic','This heals you for 10 when used.', 3, 10)
    Armor = Item('Armor', 'This reduces damage by 2 when you are struck. These do stack.', 6, 2)
    Evade = Item('Evade Potion','This increases your chance to dodge attacks by 8%. These do stack.', 1, 10)
    CritPotion = Item('Critical Strike Potion', 'This increases your chance of dealing a critical strike by 8%. These do stack.', 1, 5)
    CritHealPotion = Item('Critical Healing Potion', 'This increases your chance of healing yourself by 3 after being struck. The percentage does stack.', 1, 5)


    
    #====================================================================================================================================
    #                                                           Character Creation
    #====================================================================================================================================
    #format: Character(health | power | type | critical strike % | critical heal % | critical heal amount | % to dodge | invulnerable | bounty )
    hero = Character(health = 10, power = 5, char_class = 'Hero', p_crit = 0, p_crit_heal = 0, crit_heal_amount = 3, p_dodge = 0, invuln = False, bounty = 8, armor = 0)
    print('1.) Goblin (Health: 2, Power: 2, Bounty: 1 coin)')
    print('2.) Medic (Health: 10, Power: 2, Bounty: 2 coins)')
    print('3.) Zombie (Health: 5, Power: 3, Bounty: 5 coins)')
    print('4.) Shadow (Health: 1, Power: 3, Bounty: 5 coins)')
    print('5.) Wizard (Health: 5, Power: 6, Bounty: 6 coins)')
    print('6.) Werewolf (Health: 12, Power: 3, Bounty: 7 coins)')
    print('7.) Stop Adventuring (quit game)')
    print('---------------------------------------------------------')
    monster_choice = int(input(f'Greetings noble adventurer. There are many monsters that need to be slain. First, you must choose one to fight. Which would you like to fight?: '))
    while monster_choice != 7:
        #format: Character(health | power | type | critical strike % | critical heal % | critical heal amount | % to dodge | invulnerable | bounty | armor )
        if monster_choice == 1:
            monster = Character(health = 2, power = 2, char_class = 'Goblin', p_crit = 0, p_crit_heal = 0, crit_heal_amount = 0, p_dodge = 0, invuln = False, bounty = 1, armor = 0)
        elif monster_choice == 2:
            monster = Character(health = 10, power = 2, char_class = 'Medic', p_crit = 0, p_crit_heal = 20, crit_heal_amount = 2, p_dodge = 0, invuln = False, bounty = 2, armor = 0)
        elif monster_choice == 3:
            monster = Character(health = 5, power = 3, char_class = 'Zombie', p_crit = 0, p_crit_heal = 0, crit_heal_amount = 0, p_dodge = 0, invuln = True, bounty = 5, armor = 0)
        elif monster_choice == 4:
            monster = Character(health = 1, power = 3, char_class = 'Shadow', p_crit = 0, p_crit_heal = 0, crit_heal_amount = 0, p_dodge = 90, invuln = False, bounty = 5, armor = 0)
        elif monster_choice == 5:
            monster = Character(health = 5, power = 6, char_class = 'Wizard', p_crit = 0, p_crit_heal = 40, crit_heal_amount = 3, p_dodge = 0, invuln = False, bounty = 6, armor = 0)
        elif monster_choice == 6:
            monster = Character(health = 12, power = 3, char_class = 'Werewolf', p_crit = 10, p_crit_heal = 25, crit_heal_amount = 3, p_dodge = 15, invuln = False, bounty = 6, armor = 0)
        else:
            print(f'Goodbye.')

        go_to_store = input('Would you like to go to the Store to buy items to aid you? (Y/N): ')
        go_to_store = go_to_store.upper()
        while go_to_store != 'Y' and go_to_store != 'N': #check for bad input
            print(f'Invalid input {go_to_store}. Try again.')
            go_to_store = input('Would you like to go to the Store to buy items to aid you? (Y/N): ')
            go_to_store = go_to_store.upper
        
        if go_to_store == 'Y':
            print('-------------------------------------------------')
            print('               List of Store Items')
            print('-------------------------------------------------')
            print(f'1.) {SuperTonic.name} -- {SuperTonic.description} -- Cost: {SuperTonic.cost} -- # in stock: {SuperTonic.inventory}')
            print(f'2.) {Armor.name} -- {Armor.description} -- Cost: {Armor.cost} -- # in stock: {Armor.inventory}')
            print(f'3.) {Evade.name} -- {Evade.description} -- Cost: {Evade.cost} -- # in stock: {Evade.inventory}')
            print(f'4.) {CritPotion.name} -- {CritPotion.description} -- Cost: {CritPotion.cost} -- # in stock: {CritPotion.inventory}')
            print(f'5.) {CritHealPotion.name} -- {CritHealPotion.description} -- Cost: {CritHealPotion.cost} -- # in stock: {CritHealPotion.inventory}')
            print(f'6.) Go Back')
            print()
            print(f'You have {hero.bounty} coins.')
            store_choice = int(input('What would you like to buy?: '))
            while store_choice != 6:
                if store_choice == 1: #they buy SuperTonic
                    if SuperTonic.inventory <=0:
                        print(f'Sorry, we are all out of {SuperTonic.name}')
                    elif hero.bounty < SuperTonic.cost:
                        print(f'Sorry, you don\'t have enough coins to buy this. You have {hero.bounty} coins, the {SuperTonic.name} costs {SuperTonic.cost}.')
                    else:
                        SuperTonic.inventory -= 1
                        hero.bounty -= SuperTonic.cost
                        print('1.) Use now')
                        print('2.) Add to inventory and save for later.')
                        now_or_later = int(input('Which do you want to do?: '))
                        if now_or_later == 1:
                            hero.health += 10
                            print(f'You now have {hero.health} health.')
                        #else:

                elif store_choice == 2: #they buy Armor
                    if Armor.inventory <=0:
                        print(f'Sorry, we are all out of {Armor.name}')
                    elif hero.bounty < Armor.cost:
                        print(f'Sorry, you don\'t have enough coins to buy this. You have {hero.bounty} coins, the {Armor.name} costs {Armor.cost}.')
                    else:
                        Armor.inventory -= 1
                        hero.bounty -= Armor.cost
                        print('1.) Use now')
                        print('2.) Add to inventory and save for later.')
                        now_or_later = int(input('Which do you want to do?: '))
                        if now_or_later == 1:
                            hero.armor += 2
                            print(f'You now have {hero.armor} armor.')
                        #else:
                
                elif store_choice == 3: #they buy Evade potion
                    if Evade.inventory <=0:
                        print(f'Sorry, we are all out of {Evade.name}')
                    elif hero.p_dodge >= 90:
                        print(f'Sorry, you\'ve already maxed out your % chance to dodge. You are at {hero.p_dodge}%')
                    elif hero.bounty < Evade.cost:
                        print(f'Sorry, you don\'t have enough coins to buy this. You have {hero.bounty} coins, the {Evade.name} costs {Evade.cost}.')
                    else:
                        Evade.inventory -= 1
                        hero.bounty -= Evade.cost
                        print('1.) Use now')
                        print('2.) Add to inventory and save for later.')
                        now_or_later = int(input('Which do you want to do?: '))
                        if now_or_later == 1:
                            hero.p_dodge += 8
                            print(f'You now have {hero.p_dodge}% chance to dodge.')
                        #else:

                elif store_choice == 4: #they buy a critical strike potion
                    if CritPotion.inventory <= 0:
                        print(f'Sorry, we are all out of {CritPotion.name}')
                    elif hero.bounty < CritPotion.cost:
                        print(f'Sorry, you don\'t have enough coins to buy this. You have {hero.bounty} coins, the {CritPotion.name} costs {CritPotion.cost}.')
                    else:
                        CritPotion.inventory -= 1
                        hero.bounty -= CritPotion.cost
                        print('1.) Use now')
                        print('2.) Add to inventory and save for later.')
                        now_or_later = int(input('Which do you want to do?: '))
                        if now_or_later == 1:
                            hero.p_crit += 8
                            print(f'You now have {hero.p_crit}% chance to dodge.')
                        #else:
                
                elif store_choice == 5: #they buy a critical healing potion
                    if CritHealPotion.inventory <= 0:
                        print(f'Sorry, we are all out of {CritHealPotion.name}')
                    elif hero.bounty < CritHealPotion.cost:
                        print(f'Sorry, you don\'t have enough coins to buy this. You have {hero.bounty} coins, the {CritHealPotion.name} costs {CritHealPotion.cost}.')
                    else:
                        CritHealPotion.inventory -= 1
                        hero.bounty -= CritHealPotion.cost
                        print('1.) Use now')
                        print('2.) Add to inventory and save for later.')
                        now_or_later = int(input('Which do you want to do?: '))
                        if now_or_later == 1:
                            hero.p_crit_heal += 8
                            print(f'You now have {hero.p_crit_heal}% chance to heal yourself for {hero.crit_heal_amount}')
                        #else:
                time.sleep(1)
                print('-------------------------------------------------')
                print(f'You have {hero.bounty} coins.')
                store_choice = int(input('What would you like to buy?: '))
        print('------------------------')
        time.sleep(1)
        print('------------------------')

        while monster.alive() and hero.alive(): #Finally, we get to the actual combat
            time.sleep(1)
            hero.print_status()
            monster.print_status()
            time.sleep(1)
            print()
            print("What do you want to do?")
            print(f'1.) fight the {monster.char_class}')
            print('2.) do nothing')
            print('3.) flee')
            print('4.) Use an item in your inventory to aid you.')
            print('> ', end=' ')

            store_chosen = False #used to keep the monster from attacking the player if they choose to go to the store
            raw_input = input()
            if raw_input == "1": # Hero attacks monster
                hero.attack(monster)
                if monster.health < 0 and monster.invuln == True:
                    print(f'The {monster.char_class} refuses to die! AAAAAAGGHHHHH!')
            elif raw_input == "2":
                pass #this will take us to the 'if monster.health > 0:' line below.
            elif raw_input == "3":
                for i in range(11): #11 so this executes 10 times
                    #print('-', end='')
                    time.sleep(0.8)
                    if i == 0:
                        print('- There are footsteps right behind you!...')
                    elif i == 3:
                        print('- Keep going! you are getting away...')
                    elif i == 7:
                        print('- You nearly tripped, be careful!...')
                    elif i == 10:
                        print(f'- You hear no signs of the {monster.char_class} anymore. Phew! You made it...')
                        time.sleep(3)
                    else:
                        print('-')
                    
                #print("Goodbye.")
                break
            elif raw_input == '4':
                store_chosen = True
                print('-------------------------------------------------')
                print('               List of Store Items')
                print('-------------------------------------------------')
                print(f'1.) {SuperTonic.name} -- {SuperTonic.description} -- Cost: {SuperTonic.cost} -- # in stock: {SuperTonic.inventory}')
                print(f'2.) {Armor.name} -- {Armor.description} -- Cost: {Armor.cost} -- # in stock: {Armor.inventory}')
                print(f'3.) {Evade.name} -- {Evade.description} -- Cost: {Evade.cost} -- # in stock: {Evade.inventory}')
                print(f'4.) {CritPotion.name} -- {CritPotion.description} -- Cost: {CritPotion.cost} -- # in stock: {CritPotion.inventory}')
                print(f'5.) {CritHealPotion.name} -- {CritHealPotion.description} -- Cost: {CritHealPotion.cost} -- # in stock: {CritHealPotion.inventory}')
                print(f'6.) Go Back')
                print()
                store_choice = int(input('What would you like to buy?: '))
                while store_choice != 6:
                    # if store_choice == 1:
                    #     hero.health += 10
                    #     print(f'You now have {hero.health} health.')
                    # elif store_choice == 2:
                    
                    # elif store_choice == 3:
                    
                    # elif store_choice == 4:
                    
                    # elif store_choice == 5:

                    

                    store_choice = int(input('What would you like to buy?: '))
            else:
                print(f'Invalid input {raw_input}')

            if store_chosen == False: #if the player chose to go to the store, we skipp the part where the monster attacks them.
                if monster.health > 0 or monster.invuln == True: # monster attacks hero after the hero attacks it OR if the hero chooses to do nothing
                    monster.attack(hero)
                    if hero.health <= 0 and hero.invuln == False:
                        time.sleep(0.8)
                        print('- You are dead.')
                        print('-------------------------------------------------')
                else:
                    time.sleep(1)
                    print(f'- The {monster.char_class} is dead. You collect the bounty of {monster.bounty} coins.')
                    hero.bounty += monster.bounty
                    print('-------------------------------------------------')
            
        time.sleep(1.5)
        print('1.) Goblin (Health: 2, Power: 2, Bounty: 1 coin)')
        print('2.) Medic (Health: 10, Power: 2, Bounty: 2 coins)')
        print('3.) Zombie (Health: 5, Power: 2, Bounty: 5 coins)')
        print('4.) Shadow (Health: 1, Power: 3, Bounty: 5 coins)')
        print('5.) Wizard (Health: 5, Power: 6, Bounty: 6 coins)')
        print('6.) Werewolf (Health: 12, Power: 3, Bounty: 7 coins)')
        print('7.) Stop Adventuring (quit game)')
        print('---------------------------------------------------------')
        monster_choice = int(input(f'Would you like to fight another monster?: '))
        # if monster_choice == 7:
        #     time.sleep(1)
        #     print('-------------------------------------------------')
        #     print(f'Farewell!')
        #     print('-------------------------------------------------')
        #     break
    time.sleep(1)
    print('-------------------------------------------------')
    print('Farewell!')
    print('-------------------------------------------------')
main()
#keep_going()