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

    def print_header(self):
        print('-'*29)
        print('Welcome to my Adventure Game!')
        print('-'*29)

    def print_help(self):
        print('\nPress "w" to take a step, "s" to check your status, "l" to look behind you, or "q" to quit')

    def print_intro(self):
        print(f'\nHello {self.player.get_name()}!')

        print('\nYou are on the beach of an uninhabited island searching for treasure.')
        print('You are not searching for just any treasure, this treasure is')
        print('rumored to contain the answers to one of life\'s greatest mysteries.')
        print('This treasure is rumored to contain answers pertaining to the meaning of life,')
        print('as well as lots of gold!')

        self.print_help()

    def handle_move(self):
        print(f'\nAccording to your map, you are {self.get_moves()} steps away from the treasure.')
        
        while True:
            choice = input('What do you do ("h" for help)? ')[0].lower()

            if choice == 's':
                self.player.print_status()
            elif choice == 'l':
                self.player.look_behind()
            elif choice == 'h':
                self.print_help()

            if choice in ['w','q']: break

        if choice == 'w':
            print('\nYou take a step forward.')
        else:
            self.end_game()

    def run(self):
        self.print_header()
        
        name = input('\nWhat is your name? ')
        self.player = Player(name)
        self.print_intro()

        while not self.is_game_over():
            if self.get_moves() >= 2:
                self.handle_move()
                self.decrement_moves()
            else:
                print('You found the treasure!')
                self.end_game()
        
        print('\nGAME OVER!\n')

if __name__ == '__main__': AdventureGame().run()