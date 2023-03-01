# Adventure Game project designed for Maryville University
# SWDV 600: Intro to Programming

from random import random, randrange
from player import Player
from enemies import Enemy, Crab, Philosopher, ExistentialCrisis, BoltzmannBrain

class AdventureGame:
    def __init__(self):
        self.moves = 10
        self.game_over = False
        self.possible_encounters = [
            'Pages', 'Crab', 'Philosopher', 'Existential', 'Botzmann'
        ]
        self.current_enemy = None
        self.player = None
    
    def get_moves(self):
        return self.moves
    
    def is_game_over(self):
        return self.game_over
    
    def get_encounters(self):
        return self.possible_encounters
    
    def get_enemy(self):
        return self.current_enemy

    def get_player(self):
        return self.player
    
    def decrement_moves(self):
        self.moves -= 1

    def end_game(self):
        self.game_over = True

    def is_battle_over(self):
        return not (self.get_enemy().get_energy() > 0 and self.get_player().get_energy() > 0)
    
    def set_up_player(self):
        while True:
            name = input('\nWhat is your name? ')
            
            if len(name) == 0:
                print('You didn\'t enter anything! :)')
            elif len(name) > 50:
                print('That\'s a really long name! Please enter something shorter. :)')
            else:
                break

        self.player = Player(name)
    
    def set_up_enemy(self, type):
        if type == 'Crab':
            self.current_enemy = Crab()
        elif type == 'Philosopher':
            self.current_enemy = Philosopher()
        elif type == 'Existential':
            self.current_enemy = ExistentialCrisis()
        else:
            self.current_enemy = BoltzmannBrain()
    
    def get_random_choice(self):
        rand_val = random()

        if rand_val < 0.35:
            choice = 0
        elif rand_val < 0.55:
            choice = 1
        elif rand_val < 0.75:
            choice = 2
        elif rand_val < 0.95:
            choice = 3
        else:
            choice = 4
        
        return self.get_encounters()[choice]
    
    def get_attack_choice(self):
        enemy_name = self.current_enemy.get_name().lower()

        while True:
            choice = input(f'What do you do about the {enemy_name} ("h" for help)? ')
            
            if len(choice) > 0:
                choice = choice[0].lower()

            if choice in ['a', 'd', 'r', 'q']:
                break
            elif choice == 'h':
                print()
                self.print_attack_help()

        return choice

    def print_header(self):
        print('-'*29)
        print('Welcome to my Adventure Game!')
        print('-'*29)

    def print_help(self):
        print('\nPress "w" to take a step, "s" to check your status, "l" to look behind you, or "q" to quit')

    def print_attack_help(self):
        print('Press "a" to attack, "d" to debate, or "r" to reassure')

    def print_intro(self):
        print(f'Hello {self.get_player().get_name()}!')

        print('\nYou are on the beach of an uninhabited island searching for treasure.')
        print('You are not searching for just any treasure, this treasure is')
        print('rumored to contain the answers to one of life\'s greatest mysteries.')
        print('This treasure is rumored to contain answers pertaining to the meaning of life,')
        print('as well as lots of gold!')

    def print_battle_status(self):
        p = self.get_player()
        e = self.get_enemy()

        status = f'\n{p.get_name()}: {p.get_energy()} energy  |  {e.get_name()}: {e.get_energy()} energy'
        print(status)
        print('-'*len(status))

    def handle_step(self):
        print('\nYou take a step forward.')

        encounter = self.get_random_choice()
        player = self.get_player()

        if encounter == 'Pages':
            num_pages = randrange(1, 10)
            player.add_trinket(num_pages)

            if num_pages == 1:
                print('You found a page.')
            else:
                print(f'You found {num_pages} pages.')
        else:
            self.set_up_enemy(encounter)
            enemy = self.get_enemy()
            enemy.print_intro()

            self.print_battle_status()
            while not self.is_battle_over():
                self.print_attack_help()
                choice = self.get_attack_choice()      
                if choice == 'q': self.end_game(); break

                player.attack_enemy(enemy, choice)
                if enemy.get_energy() > 0: 
                    enemy.attack_player(player)

                self.print_battle_status()
            
            enemy.print_outro()
            self.current_enemy = None

    def handle_move(self):
        if self.get_moves() == 10:
            self.print_help()
        elif self.get_moves() > 1:
            print(f'\nAccording to your map, you are {self.get_moves()} steps away from the treasure.')
        else:
            print('\nAccording to your map, you are only 1 step away from the treasure!')

        while True:
            try:
                choice = input('What do you do ("h" for help)? ')[0].lower()
            except: 
                choice = ''

            if choice == 's':
                self.get_player().print_status()
            elif choice == 'l':
                self.get_player().look_behind()
            elif choice == 'h':
                self.print_help()

            if choice in ['w','q']: break
        
        #print('\033c', end='')

        if choice == 'w':
            self.handle_step()
        else:
            self.end_game()
    
    def handle_treasure(self):
        print('You find a rock with an engraving of an "X".')
        input('This must be the spot! Press <enter> to continue.')

        input('\nYou pull out your trusty shovel. Press <enter> to dig.')
        input('You start digging. Press <enter> to dig.')
        input('You hit the top of something with your shovel. Press <enter> to dig.')
        print('You uncover a treasure chest and pull it out of the hole.')
        input('Press <enter> to open the chest.')

        print('\nYou break a lock and open the chest!')
        print('Within is lots of gold coins...')
        print('However, you don\'t see anything related to the meaning of life')
        input('Press <enter> to investigate further.')
        
        print('\nYou reach into the sea of gold coins and pull out a scroll!')
        input('Press <enter> to open the scroll.')

        print('\nYou awaken in your bed, realizing that it was just a dream.')

    def run(self):
        self.print_header()
        self.set_up_player()
        self.print_intro()

        while not self.is_game_over():
            if self.get_moves() >= 1:
                self.handle_move()
                self.decrement_moves()
            else:
                self.handle_treasure()
                self.end_game()
        
        print('\nGAME OVER!')

if __name__ == '__main__': AdventureGame().run()