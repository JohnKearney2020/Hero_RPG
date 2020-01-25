#Hero RPG Part 1 by John Kearney

import time

class Character:
    def __init__(self, character_health, character_power, char_class):
        self.health = character_health
        self.power = character_power
        self.char_class = char_class

    def alive(self): #check to see if our character is still alive.
        if self.health <= 0:
            return False
        else:
            return True
    
    def print_status(self):
        if self.char_class == 'Hero':
            print(f'You have {self.health} health and {self.power} power.')
        else: #leaving this one non-descript so it will work for all monsters
            print(f'The {self.char_class} has {self.health} health and {self.power} power.')
    
    def attack(self, attackee): #I chose attackee as the parameter instead of monster b/c I may want to use the attack() method on other enemy objects, not just the monster
    #object we created
        if attackee.char_class != 'Zombie':
            attackee.health -= self.power


class HeroBaseStats(Character):
    def __init__(self, character_health, character_power):
        super().__init__(character_health, character_power)

class GoblinBaseStats(Character):
    def __init__(self, monster_health, monster_power):
        super().__init__(character_health, character_power)


def main():

    hero = Character(10, 5, 'Hero')
    #monster = Character(6, 2, 'Goblin')
    monster = Character(6, 2, 'Zombie')
    first_loop = False

    #while monster_health > 0 and hero_health > 0:
    while monster.alive() and hero.alive():
        #print("You have {} health and {} power.".format(hero_health, hero_power))
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
            if monster.char_class != 'Zombie':
                print(f'You deal {hero.power} damage to the Goblin.')
            else:
                print(f'The {monster.char_class} appeared to take no damage... *GULP*')

        elif raw_input == "2":
            pass
            #monster.attack(hero)
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

        if monster.health > 0: # Goblin attacks hero after the hero attacks it OR if the hero chooses to do nothing
            monster.attack(hero)
            print(f'The {monster.char_class} does {monster.power} damage to you.')
            if hero.health <= 0:
                time.sleep(0.8)
                print('- You are dead.')
        else:
            print(f'- The {monster.char_class} is dead.')
            
main()
