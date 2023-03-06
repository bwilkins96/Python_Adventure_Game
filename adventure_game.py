# Adventure Game project designed for Maryville University
# SWDV 600: Intro to Programming

# Running this file produces and runs an Adventure Game instance

from os import system, name as os_name
from random import random, randrange
from player import Player
from enemies import Crab, Philosopher, ExistentialCrisis, BoltzmannBrain

class AdventureGame:
    def __init__(self):
        """
        Produces an Adventure Game instance that tracks moves left, whether the game is over,
        a list of possible encounters, the current enemy, and the player
        e.g. AdventureGame()
        """
        self.moves = 10
        self.game_over = False
        self.possible_encounters = [
            'Pages', 'Crab', 'Philosopher', 'Existential', 'Boltzmann'
        ]
        self.current_enemy = None
        self.player = None

    def get_moves(self):
        "Returns the number of moves left"
        return self.moves

    def is_game_over(self):
        "Returns whether the game is over"
        return self.game_over

    def get_encounters(self):
        "Returns a copy of the list of possible encounters"
        return self.possible_encounters[:]

    def get_enemy(self):
        "Returns the current enemy"
        return self.current_enemy

    def get_player(self):
        "Returns the player instance"
        return self.player

    def decrement_moves(self):
        "Decreases the remaining moves by 1"
        self.moves -= 1

    def end_game(self):
        "Sets the game over variable to true"
        self.game_over = True

    def is_battle_over(self):
        "Returns whether the current battle is over"
        return not (self.get_enemy().get_energy() > 0 and self.get_player().get_energy() > 0)

    def set_up_player(self):
        "Sets up the player instance for a game"
        while True:
            name = input('\nWhat is your name (<enter> to submit)? ')

            # Validates name length
            if len(name) == 0:
                print('You didn\'t enter anything! :)')
            elif len(name) > 35:
                print('That\'s a really long name! Please enter something shorter. :)')
            else:
                break

        self.player = Player(name)

    def set_up_enemy(self, type):
        "Sets up current enemy based on type"
        if type == 'Crab':
            self.current_enemy = Crab()
        elif type == 'Philosopher':
            self.current_enemy = Philosopher()
        elif type == 'Existential':
            self.current_enemy = ExistentialCrisis()
        else:
            self.current_enemy = BoltzmannBrain()

        # Adds enemy to player encounter tracking
        self.get_player().add_encounter(self.get_enemy().get_name())

    def get_random_choice(self):
        "Returns a random encounter choice based on probability"
        rand_val = random()

        # Gets index of encounter choice
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
        "Gets attack choice from user"
        enemy_name = self.current_enemy.get_name().lower()

        while True:
            choice = input(f'What do you do about the {enemy_name} ("h" for help)? ')

            if len(choice) > 0:
                choice = choice[0].lower()

            # Validates choice
            if choice in ['a', 'd', 'r', 'q']:
                break
            elif choice == 'h':
                self.print_attack_help(True)

        return choice

    def print_header(self):
        "Prints header for a game instance"
        print('\n' + ('-'*29))
        print('Welcome to my Adventure Game!')
        print('-'*29)

    def print_help(self, additional=False):
        """
        Prints help for main game loop
        Uses additional parameter for printing more info when "h" is pressed
        """
        if additional:
            print('\nWhen you take a move, there is a chance of encountering enemies')
            print('and possibly finding other interesting things.')
            print('If attacked, try not to let your energy get too low.\n')

        print('Press "w" to start walking, "s" to check your status, "l" to look behind you, or "q" to quit')

    def print_attack_help(self, additional=False):
        """
        Prints help for battles
        Uses additional parameter for printing more info when "h" is pressed
        """
        if additional:
            print('\nTry different options on enemies to figure out the best response!')
            print('"q" still ends the game when in a battle.\n')

        print('Press "a" to attack, "d" to debate, or "r" to reassure')

    def print_intro(self):
        "Prints intro for game instance"
        print(f'Hello Captain {self.get_player().get_name()}!')

        print('\nYou are on the beach of an uninhabited island searching for treasure.')
        print('You are not searching for just any treasure, this treasure is')
        print('rumored to contain the answers to one of life\'s greatest mysteries.')
        print('This treasure is rumored to contain answers pertaining to the meaning of life,')
        print('as well as lots of gold!')

        self.clear_terminal(True)

    def print_battle_status(self, new_line=True):
        "Prints the current status of the battle"
        p = self.get_player()
        e = self.get_enemy()

        if new_line: print()
        status = f'Captain {p.get_name()}: {p.get_energy()} energy  |  {e.get_name()}: {e.get_energy()} energy'
        print(status)
        print('-'*len(status))

    def clear_terminal(self, wait=False):
        """
        Clears the terminal screen
        Uses the wait parameter to determine whether to first prompt user for input
        """
        if wait: input('\nPress <enter> to continue. ')

        if os_name == 'nt':
            # Windows
            system('cls')
        else:
            # Linux or Mac
            system('clear')

        # Prints extra line
        print()

        # NOTE: This function does not clear the shell when run in Thonny
        # This function should work properly when run in a terminal!

    def handle_player_defeat(self):
        "Handles player energy hitting zero during a battle"
        self.get_player().handle_defeat()

        # Handles player revive
        if self.get_player().get_energy() > 0:
            self.clear_terminal()
            self.print_battle_status(False)

    def handle_step(self):
        "Handles the step between moves, in which encounters are generated"
        print('\nYou begin walking forward.')

        encounter = self.get_random_choice()
        player = self.get_player()

        if encounter == 'Pages':
            # Handles player finding between 1 and 8 pages
            num_pages = randrange(1, 9)
            player.add_trinket(num_pages)

            if num_pages == 1:
                print('\nYou find a page.')
            else:
                print(f'\nYou find {num_pages} pages.')
        else:
            # Handles enemy encounters / battles
            self.set_up_enemy(encounter)
            enemy = self.get_enemy()
            enemy.print_intro()
            self.clear_terminal(True)

            # Battle loop
            self.print_battle_status(False)
            while not self.is_battle_over():
                self.print_attack_help()
                choice = self.get_attack_choice()
                if choice == 'q': self.end_game(); break
                self.clear_terminal()

                player.attack_enemy(enemy, choice)
                if enemy.get_energy() > 0:
                    enemy.attack_player(player)

                self.print_battle_status()
                if player.get_energy() <= 0:
                    self.handle_player_defeat()

            if player.get_energy() > 0:
                enemy.print_outro()
            else:
                self.end_game()

            # Clears current enemy
            self.current_enemy = None

    def handle_move(self):
        "Handles a move in the main game loop"
        if self.get_moves() > 1:
            print(f'According to your map, you are {self.get_moves()} moves away from the treasure.')
        else:
            print('According to your map, you are only 1 move away from the treasure!')

        # Increase player energy by 25 when halfway through
        if self.get_moves() == 5 and self.get_player().get_energy() < 100:
            print('The thought of making it halfway to the treasure causes you to regain some energy!')
            self.get_player().add_energy(25)

        self.print_help()
        while True:
            # Gets player choice and handles error caused by input of zero length
            try:
                choice = input('What do you do ("h" for help)? ')[0].lower()
            except:
                choice = ''

            # Handles player choice 
            if choice == 's':
                self.get_player().print_status()
            elif choice == 'l':
                self.get_player().look_behind(self.get_moves())
            elif choice == 'h':
                self.print_help(True)

            # Breaks out of loop if "w" or "q" are selected
            if choice in ['w','q']: break

        if choice == 'w':
            self.handle_step()
        else:
            self.end_game()

        # Clears terminal between moves, waits for input if game is NOT over
        self.clear_terminal(not self.is_game_over())

    def handle_treasure(self):
        "Handles player finding of treasure at end of game"
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
        "Prints end of game stats"
        if self.get_moves() == 0:
            self.get_player().print_end_stats(True)
        else:
            self.get_player().print_end_stats(False)

        print('\nGAME OVER!\n')

    def run(self):
        "Runs an instance of the Adventure Game"
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

# Produces an Adventure Game instance and calls its run method
if __name__ == '__main__': AdventureGame().run()
