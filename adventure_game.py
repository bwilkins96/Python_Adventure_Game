# Adventure Game project designed for Maryville University
# SWDV 600: Intro to Programming

from player import Player
from enemies import Enemy, Crab, Philosopher, ExistentialCrisis, BoltzmannBrain

class AdventureGame:
    def __init__(self):
        self.moves = 10
        self.game_over = False
    
    def get_moves(self):
        return self.moves
    
    def is_game_over(self):
        return self.game_over
    
    def decrement_moves(self):
        self.moves -= 1

    def end_game(self):
        self.game_over = True
    
    def set_up_player(self):
        while True:
            name = input('\nWhat is your name? ')
            if len(name) > 0: break
            print('You didn\'t enter anything! :)')

        self.player = Player(name)

    def print_header(self):
        print('-'*29)
        print('Welcome to my Adventure Game!')
        print('-'*29)

    def print_help(self):
        print('\nPress "w" to take a step, "s" to check your status, "l" to look behind you, or "q" to quit')

    def print_intro(self):
        print(f'Hello {self.player.get_name()}!')

        print('\nYou are on the beach of an uninhabited island searching for treasure.')
        print('You are not searching for just any treasure, this treasure is')
        print('rumored to contain the answers to one of life\'s greatest mysteries.')
        print('This treasure is rumored to contain answers pertaining to the meaning of life,')
        print('as well as lots of gold!')

    def handle_step(self):
        print('\nYou take a step forward.')

        # Handle random event here

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
                self.player.print_status()
            elif choice == 'l':
                self.player.look_behind()
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