# Player class for the Adventure Game project

class Player:
    'A player class designed for the Adventure Game project'

    def __init__(self, name):
        """
        Produces a player instance that stores name, amount of energy,
        pages, whether a revive was used, and encountered enemies
        e.g. Player(name)
        """
        self.name = name.title()
        self.energy = 100
        self.pages = 0
        self.used_second_chance = False
        self.encounters = {}
    
    def get_name(self):
        "Returns the player's name"
        return self.name
    
    def get_energy(self):
        "Returns the player's energy level"
        return self.energy

    def get_trinket_count(self):
        "Returns the player's number of pages"
        return self.pages
    
    def has_used_chance(self):
        "Returns whether the player has used a revive"
        return self.used_second_chance
    
    def reduce_energy(self, amt):
        "Reduces player energy by amount"
        self.energy -= amt

        if self.energy < 0:
            self.energy = 0

    def add_energy(self, amt):
        "Increases player energy by amount"
        self.energy += amt

        if self.energy > 100:
            self.energy = 100

    def add_trinket(self, amt):
        "Adds amount to player page count"
        self.pages += amt
    
    def reduce_trinket(self, amt):
        "Subtracts amount from player page count"
        self.pages -= amt

        if self.pages < 0:
            self.pages = 0
    
    def add_encounter(self, name):
        "Adds to the tracking of player encounters"
        encounter = self.encounters.get(name, 0)
        self.encounters[name] = encounter + 1
    
    def print_status(self):
        "Prints the player's current energy and page count"
        print(f'\n{self.get_name()} | Energy: {self.get_energy()}, Pages: {self.get_trinket_count()}\n')
    
    def look_behind(self, moves):
        "Prints a message describing the player looking behind themselves"

        print('\nYou look behind you and see the crashing waves of the ocean,')
        print(f'as well as the ship you came here on, the Ship of {self.get_name()}!')
        print('If you replaced every piece of your ship over time, would it be the same ship?\n')

        # Prints a message related to previous moves
        moves_taken = 10 - moves
        if moves_taken == 1:
            print('You also see your footprints from the previous move.\n')
        elif moves_taken > 1:
            print(f'You also see your footprints from the previous {moves_taken} moves.\n')

    def attack_enemy(self, enemy, choice):
        "Handles player battle choice"
        if choice == 'a':
            enemy.handle_attack()
        elif choice == 'd':
            enemy.handle_debate()
        else:
            enemy.handle_reassurance()
    
    def handle_defeat(self):
        "Handles player energy reaching zero and player revive"
        print('Your energy has been reduced to zero!')

        # Allows revive if not already used and page count is at least 5
        if (not self.has_used_chance()) and (self.get_trinket_count() >= 5):
            input('\nPress <enter> to continue. ')
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
        
        input('\nPress <enter> to continue. ')

    def print_end_personal(self):
        "Prints ending player energy and page count"
        energy = self.get_energy()
        pages = self.get_trinket_count()

        if energy == 0: 
            energy = 'no'

        if pages == 0:
            pages = 'no pages'
        elif pages == 1:
            pages = '1 page'
        else:
            pages = f'{pages} pages'

        print(f'At the end of your adventure, you had {energy} energy and {pages}.')
    
    def print_encounters(self):
        "Prints information about encountered enemies"
        total_encounters = len(self.encounters.keys())
        encounter_str = '\nYou encountered '

        count = 1
        for enemy in self.encounters:
            # Adds to and formats encounter string 
            num_encountered = self.encounters[enemy]

            enemy_name = enemy.lower()
            if enemy_name[0] == 'b': 
                enemy_name = enemy_name.capitalize()
            
            if count == total_encounters and count > 1: 
                encounter_str += 'and '

            # Handles making enemy names singular or plural
            if num_encountered == 1:
                encounter_str += f'1 {enemy_name}'
            else:
                if enemy_name[0] == 'e':
                    enemy_name = enemy_name[:len(enemy_name)-2] + 'e'
                
                encounter_str += f'{num_encountered} {enemy_name}s'
            
            if total_encounters > 2:
                encounter_str += ', '
            else:
                encounter_str += ' '

            count += 1
        
        # Final formatting of encounter string
        if total_encounters == 0:
            encounter_str += 'no enemies'
        elif total_encounters <= 2:
            # Removes extra space
            encounter_str = encounter_str[:len(encounter_str)-1]
        else:
            # Removes comma and extra space
            encounter_str = encounter_str[:len(encounter_str)-2]
        
        encounter_str += '.'
        print(encounter_str)
    
    def print_end_stats(self, treasure_found):
        "Prints player's ending stats"
        self.print_end_personal()
        self.print_encounters()

        if self.has_used_chance():
            print('\nYou read philosophy to regain energy when you were down.')
        
        if treasure_found:
            print('\nYou found the treasure and it had lots of gold inside!')
            print('You found a scroll and upon opening it, awoke and realized it was all a dream.')
        else:
            print('\nYou did not find the treasure!')