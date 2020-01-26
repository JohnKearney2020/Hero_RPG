#Hero RPG Part 2 by John Kearney
#I am basing this on the finished code for part 1, including all the bonus tasks

import time
import random

class Character:
    def __init__(self, health, power, char_class, p_crit, p_crit_heal, crit_heal_amount, p_dodge, invuln, bounty):
        self.health = health
        self.power = power
        self.char_class = char_class
        self.p_crit = p_crit
        self.p_crit_heal = p_crit_heal
        self.crit_heal_amount = crit_heal_amount
        self.p_dodge = p_dodge
        self.invuln = invuln
        self.bounty = bounty

    def alive(self): #check to see if our character is still alive.
        if self.health <= 0 and self.invuln == False:
            return False
        else:
            return True
    
    def print_status(self):
        if self.char_class == 'Hero':
            print(f'You have {self.health} health and {self.power} power.')
        else: #leaving this one non-descript so it will work for all monsters
            print(f'The {self.char_class} has {self.health} health and {self.power} power.')
    
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

        if attackee.char_class != 'Hero': #if the hero is attacking a monster. Monsters are getting hit.
            #if attackee.char_class != 'Zombie': #zombies take no damage, so they are excluded here
            if attack_dodged == True: #if the monster dodged an attack from our hero
                print(f'The {attackee.char_class} dodged your attack! You deal no damage to it!')
            elif crit_strike_status == True:
                attackee.health -= self.power * 2
                print(f'Critical Strike! You deal {self.power * 2} damage to the {attackee.char_class}.')
                if crit_heal_status == True:
                    attackee.health += attackee.crit_heal_amount
                    print(f'Oh no! The {attackee.char_class} regenerated {attackee.crit_heal_amount} health.')
            else:
                attackee.health -= self.power
                print(f'You deal {self.power} damage to the {attackee.char_class}.')
                if crit_heal_status == True:
                    attackee.health += attackee.crit_heal_amount
                    print(f'Oh no! The {attackee.char_class} regenerated {attackee.crit_heal_amount} health.')
            # else: #if the monster being attacked is a Zombie
            #     print(f'The {attackee.char_class} appeared to take no damage... *GULP*') #zombies take no damage
        else: #if a monster is attacking the hero
            if attack_dodged == True: #if our hero dodged the attack of the monster
                    print(f'You dodged the attack from the {self.char_class}. You take no damage!')
            elif crit_strike_status == True:
                attackee.health -= self.power * 2
                print(f'Aaagh! Critical Strike! The {self.char_class} does {self.power * 2} damage to you.')
            else:
                attackee.health -= self.power
                print(f'The {self.char_class} does {self.power} damage to you.')



def main():
    #====================================================================================================================================
    #                                                           Character Creation
    #====================================================================================================================================
    #format: Character(health | power | type | critical strike % | critical heal % | critical heal amount | % to dodge | invulnerable | bounty )
    hero = Character(health = 100, power = 1, char_class = 'Hero', p_crit = 20, p_crit_heal = 0, crit_heal_amount = 0, p_dodge = 0, invuln = False, bounty = 0)
    print('1.) Goblin (Health: 2, Power: 2, Bounty: 1 coin)')
    print('2.) Medic (Health: 10, Power: 2, Bounty: 2 coins)')
    print('3.) Zombie (Health: 5, Power: 2, Bounty: 5 coins)')
    print('4.) Shadow (Health: 1, Power: 3, Bounty: 5 coins)')
    print('5.) Wizard (Health: 5, Power: 6, Bounty: 6 coins)')
    print('6.) Werewolf (Health: 12, Power: 3, Bounty: 7 coins)')
    print('7.) Stop Adventuring (quit game)')
    print('---------------------------------------------------------')
    monster_choice = int(input(f'Greetings noble adventurer. There are many monsters that need to be slain. Which would you like to fight?:'))

    if monster_choice == 1:
        monster = Character(health = 2, power = 2, char_class = 'Goblin', p_crit = 0, p_crit_heal = 0, crit_heal_amount = 0, p_dodge = 0, invuln = False, bounty = 1)
    elif monster_choice == 2:
        monster = Character(health = 10, power = 2, char_class = 'Medic', p_crit = 0, p_crit_heal = 20, crit_heal_amount = 2, p_dodge = 0, invuln = False, bounty = 2)
    elif monster_choice == 3:
        monster = Character(health = 5, power = 2, char_class = 'Zombie', p_crit = 0, p_crit_heal = 0, crit_heal_amount = 0, p_dodge = 0, invuln = True, bounty = 5)
    elif monster_choice == 4:
        monster = Character(health = 1, power = 3, char_class = 'Shadow', p_crit = 0, p_crit_heal = 0, crit_heal_amount = 0, p_dodge = 90, invuln = False, bounty = 5)
    elif monster_choice == 5:
        monster = Character(health = 5, power = 6, char_class = 'Wizard', p_crit = 0, p_crit_heal = 40, crit_heal_amount = 3, p_dodge = 0, invuln = False, bounty = 6)
    elif monster_choice == 6:
        monster = Character(health = 12, power = 3, char_class = 'Werewolf', p_crit = 10, p_crit_heal = 25, crit_heal_amount = 3, p_dodge = 15, invuln = False, bounty = 6)
    else:
        print(f'Goodbye.')

    first_loop = False

    while monster.alive() and hero.alive():
        if first_loop == False:
            #print(f'You have {hero.health} health and {hero.power} power.')
            hero.print_status()
            #print("The monster has {} health and {} power.".format(monster_health, monster_power))
            #print(f'The monster has {monster.health} health and {monster.power} power.')
            monster.print_status()
            print()
            print("What do you want to do?")
            print("1. fight monster")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            first_loop = True
        else:
            #time.sleep(1.5)
            #print(f'You have {hero.health} health and {hero.power} power.')
            hero.print_status()
            #print("The monster has {} health and {} power.".format(monster_health, monster_power))
            #print(f'The monster has {monster.health} health and {monster.power} power.')
            monster.print_status()
            print()
            time.sleep(0.8)
            print("What do you want to do?")
            print("1. fight monster")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')

        raw_input = input()
        if raw_input == "1": # Hero attacks monster
            hero.attack(monster)
            if monster.health < 0:
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
                
            print("Goodbye.")
            break
        else:
            print(f'Invalid input {raw_input}')

        if monster.health > 0 or monster.invuln == True: # monster attacks hero after the hero attacks it OR if the hero chooses to do nothing
            monster.attack(hero)
            if hero.health <= 0 and hero.invuln == False:
                time.sleep(0.8)
                print('- You are dead.')
        else:
            print(f'- The {monster.char_class} is dead. You collect the bounty of {monster.bounty} coins.')
            self.bounty += monster.bounty
            
main()
