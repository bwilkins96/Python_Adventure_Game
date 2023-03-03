# Adventure Game project designed for Maryville University
# SWDV 600: Intro to Programming

from random import random, randrange
from player import Player
from enemies import Crab, Philosopher, ExistentialCrisis, BoltzmannBrain

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
            name = input('\nWhat is your name (<enter> to submit)? ')
            
            if len(name) == 0:
                print('You didn\'t enter anything! :)')
            elif len(name) > 35:
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
        
        self.get_player().add_encounter(self.get_enemy().get_name())
    
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
                self.print_attack_help(True)

        return choice

    def print_header(self):
        print('-'*29)
        print('Welcome to my Adventure Game!')
        print('-'*29)

    def print_help(self, additional=False):
        if additional:
            print('\nWhen you take a move, there is a chance of encountering enemies')
            print('and possibly finding other interesting things.')
            print('If attacked, try not to let your energy get too low.\n')

        print('Press "w" to start walking, "s" to check your status, "l" to look behind you, or "q" to quit')

    def print_attack_help(self, additional=False):
        if additional:
            print('\nTry different options on enemies to figure out the best response!')
            print('"q" still ends the game when in a battle.\n')

        print('Press "a" to attack, "d" to debate, or "r" to reassure')

    def print_intro(self):
        print(f'Hello Captain {self.get_player().get_name()}!')

        print('\nYou are on the beach of an uninhabited island searching for treasure.')
        print('You are not searching for just any treasure, this treasure is')
        print('rumored to contain the answers to one of life\'s greatest mysteries.')
        print('This treasure is rumored to contain answers pertaining to the meaning of life,')
        print('as well as lots of gold!')

        self.clear_terminal(True)

    def print_battle_status(self, new_line=True):
        p = self.get_player()
        e = self.get_enemy()

        if new_line: print()
        status = f'Captain {p.get_name()}: {p.get_energy()} energy  |  {e.get_name()}: {e.get_energy()} energy'
        print(status)
        print('-'*len(status))
    
    def clear_terminal(self, wait=False):
        if wait: input('\nPress <enter> to continue. ')
        print('\033c', end='')

    def handle_player_defeat(self):
        self.print_battle_status()
        self.get_player().handle_defeat()
        self.clear_terminal()
        self.print_battle_status(False)

    def handle_step(self):
        print('\nYou begin walking forward.')

        encounter = self.get_random_choice()
        player = self.get_player()

        if encounter == 'Pages':
            num_pages = randrange(1, 9)
            player.add_trinket(num_pages)

            if num_pages == 1:
                print('\nYou find a page.')
            else:
                print(f'\nYou find {num_pages} pages.')
        else:
            self.set_up_enemy(encounter)
            enemy = self.get_enemy()
            enemy.print_intro()
            self.clear_terminal(True)

            self.print_battle_status(False)
            while not self.is_battle_over():
                self.print_attack_help()
                choice = self.get_attack_choice()      
                if choice == 'q': self.end_game(); break
                self.clear_terminal()

                player.attack_enemy(enemy, choice)
                if enemy.get_energy() > 0: 
                    enemy.attack_player(player)

                if player.get_energy() <= 0:
                    self.handle_player_defeat()
                else:
                    self.print_battle_status()
            
            if player.get_energy() > 0:
                enemy.print_outro()
            else:
                self.end_game()

            self.current_enemy = None

    def handle_move(self):
        if self.get_moves() > 1:
            print(f'According to your map, you are {self.get_moves()} moves away from the treasure.')
        else:
            print('According to your map, you are only 1 move away from the treasure!')

        if self.get_moves() == 5 and self.get_player().get_energy() < 100:
            print('The thought of making it halfway to the treasure causes you to regain some energy!')
            self.get_player().add_energy(25)
        
        self.print_help()
        while True:
            try:
                choice = input('What do you do ("h" for help)? ')[0].lower()
            except: 
                choice = ''

            if choice == 's':
                self.get_player().print_status()
            elif choice == 'l':
                self.get_player().look_behind(self.get_moves())
            elif choice == 'h':
                self.print_help(True)

            if choice in ['w','q']: break

        if choice == 'w':
            self.handle_step()
        else:
            self.end_game()

        self.clear_terminal(not self.is_game_over())
    
    def handle_treasure(self):
        print('You find a rock with an engraving of an "X".')
        input('This must be the spot! Press <enter> to continue. ')

        input('\nYou pull out your trusty shovel. Press <enter> to dig. ')
        input('You start digging. Press <enter> to dig. ')
        input('You hit the top of something with your shovel. Press <enter> to dig. ')
        print('You uncover a treasure chest and pull it out of the hole.')
        input('Press <enter> to open the chest. ')

        print('\nYou break a lock and open the chest!')
        print('Within is lots of gold coins...')
        print('However, you don\'t see anything related to the meaning of life.')
        input('Press <enter> to investigate further. ')
        
        print('\nYou reach into the sea of gold coins and pull out a scroll!')
        input('Press <enter> to open the scroll. ')

        print('\nYou awaken in your bed, realizing that it was just a dream.')
        self.clear_terminal(True)

    def handle_game_over(self):
        if self.get_moves() == 0:
            self.get_player().print_end_stats(True)
        else:
            self.get_player().print_end_stats(False)

        print('\nGAME OVER!')

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
        
        self.handle_game_over()
        
if __name__ == '__main__': AdventureGame().run()