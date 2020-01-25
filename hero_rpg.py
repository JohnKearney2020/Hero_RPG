#Hero RPG Part 1 by John Kearney
#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

import time

class HeroBaseStats:
    def __init__(self, hero_health, hero_power):
        self.health = hero_health
        self.power = hero_power

    def attack(self, enemy): #I chose enemy as the parameter instead of goblin b/c I may want to use the attack() method on other enemy objects, not just the goblin
        #object we created
        self.enemy = enemy
        enemy.health -= self.power
        for i in range(11): #11 so this executes 10 times
            time.sleep(0.8)
            if i == 0:
                print('- You draw your weapon and attack!...')
            elif i == 3:
                print('- Your enemy snarls and releases a defeaning roar!!!...')
            elif i == 7:
                print('- *sounds of swords clanging and inhuman screams*')
            elif i == 10:
                print(f'- You do {self.power} damage to the goblin.')
                #time.sleep(2)
            else:
                print('-')
        
        if enemy.health <= 0:
            time.sleep(0.8)
            print('- The goblin is dead!')
    
    def alive(self): #check to see if our hero is still alive.
        if self.health <= 0:
            return False
        else:
            return True

class GoblinBaseStats:
    def __init__(self, goblin_health, goblin_power):
        self.health = goblin_health
        self.power = goblin_power

    def attack(self, hero):
        hero.health -= self.power
        time.sleep(0.8)
        print('-')
        print(f'- The goblin does {self.power} damage to you.')
        time.sleep(0.8)
        print('-')
        if hero.health <= 0:
            # time.sleep(0.8)
            # print('-')
            time.sleep(0.8)
            print('- You are dead.')
    
    def alive(self): #check to see if our goblin is still alive.
        if self.health <= 0:
            return False
        else:
            return True



def main():

    hero = HeroBaseStats(10, 5)
    # hero_health = 10
    # hero_power = 5
    goblin = GoblinBaseStats(6, 2)
    # goblin_health = 6
    # goblin_power = 2
    first_loop = False

    #while goblin_health > 0 and hero_health > 0:
    while goblin.alive() and hero.alive():
        #print("You have {} health and {} power.".format(hero_health, hero_power))
        if first_loop == False:
            print(f'You have {hero.health} health and {hero.power} power.')
            #print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
            print(f'The goblin has {goblin.health} health and {goblin.power} power.')
            print()
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')
            first_loop = True
        else:
            #time.sleep(1.5)
            print(f'You have {hero.health} health and {hero.power} power.')
            #print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
            print(f'The goblin has {goblin.health} health and {goblin.power} power.')
            print()
            time.sleep(0.8)
            print("What do you want to do?")
            print("1. fight goblin")
            print("2. do nothing")
            print("3. flee")
            print("> ", end=' ')

        raw_input = input()
        if raw_input == "1": # Hero attacks goblin
            hero.attack(goblin)
        elif raw_input == "2":
            pass
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
                    print('- You hear no signs of the goblin anymore. Phew! You made it...')
                    time.sleep(3)
                else:
                    print('-')
                
            print("Goodbye.")
            break
        else:
            print(f'Invalid input {raw_input}')

        if goblin.health > 0: # Goblin attacks hero
            goblin.attack(hero)


main()
