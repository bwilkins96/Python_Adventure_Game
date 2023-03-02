# Player class for the Adventure Game project

class Player:
    def __init__(self, name):
        self.name = name.title()
        self.energy = 100
        self.pages = 0
        self.used_second_chance = False
    
    def get_name(self):
        return self.name
    
    def get_energy(self):
        return self.energy

    def get_trinket_count(self):
        return self.pages
    
    def has_used_chance(self):
        return self.used_second_chance
    
    def reduce_energy(self, amt):
        self.energy -= amt

        if self.energy < 0:
            self.energy = 0

    def add_energy(self, amt):
        self.energy += amt

        if self.energy > 100:
            self.energy = 100

    def add_trinket(self, amt):
        self.pages += amt
    
    def reduce_trinket(self, amt):
        self.pages -= amt

        if self.pages < 0:
            self.pages = 0
    
    def print_status(self):
        print(f'\n{self.get_name()} | Energy: {self.get_energy()}, Pages: {self.get_trinket_count()}\n')
    
    def look_behind(self):
        print('\nYou look behind you and see the crashing waves of the ocean,')
        print(f'as well as the ship you came here on, the Ship of {self.get_name()}!')
        print('If you replaced every piece of your ship over time, would it be the same ship?\n')

    def attack_enemy(self, enemy, choice):
        if choice == 'a':
            enemy.handle_attack()
        elif choice == 'd':
            enemy.handle_debate()
        else:
            enemy.handle_reassurance()
    
    def handle_defeat(self):
        print('Your energy has been reduced to zero!')

        if (not self.has_used_chance()) and (self.get_trinket_count() >= 5):
            input('\nPress <enter> to continue.')
            print('\nYou are laying in the sand when you have an idea!')
            print('You have collected a number of pages and reading them should bring your energy back up.')
            input_val = input('Press <enter> to read all of your pages or "q" to quit. ')

            if len(input_val) > 0 and input_val[0].lower() == 'q': return

            print(f'\nYou read all {self.get_trinket_count()} of your pages, each containing a philosophy essay.')
            print('A gust of wind blows your pages away, but your energy is back up to 100.')
            print('You get the feeling you will only be able to do that once.')

            self.reduce_trinket(self.get_trinket_count())
            self.add_energy(100)

            self.used_second_chance = True 
        elif self.has_used_chance():
            print('Unfortunatley, you are so tired that reading more philosophy will not help.')
        
        input('\nPress <enter> to continue.')

    def print_end_stats(self, treasure_found):
        print(f'At the end of your adventure, you had {self.get_energy()} energy and {self.get_trinket_count()} pages.')

        if treasure_found:
            print('\nYou found the treasure and it had lots of gold inside!')
            print('You found a scroll and upon opening it, awoke and realized it was all a dream.')
        else:
            print('\nYou did not find the treasure!')