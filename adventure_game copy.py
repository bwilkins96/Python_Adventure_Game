# Adventure Game Project

from player import Player
from enemies import Enemy, Crab, Philosopher, ExistentialCrisis, BoltzmannBrain

def print_header():
    print('-'*29)
    print('Welcome to my Adventure Game!')
    print('-'*29)

def print_help():
    print('\nPress "w" to take a step, "s" to check your status, "l" to look behind you, or "q" to quit')

def print_intro(player):
    print(f'\nHello {player.get_name()}!')

    print('\nYou are on the beach of an uninhabited island searching for treasure.')
    print('You are not searching for just any treasure, this treasure is')
    print('rumored to contain the answers to one of life\'s greatest mysteries.')
    print('This treasure is rumored to contain answers pertaining to the meaning of life,')
    print('as well as lots of gold!')

    print_help()

def handle_move(moves, player):
    print(f'\nAccording to your map, you are {moves} steps away from the treasure.')
    
    while True:
        choice = input('What do you do ("h" for help)? ')[0].lower()

        if choice == 's':
            player.print_status()
        elif choice == 'l':
            player.look_behind()
        elif choice == 'h':
            print_help()

        if choice in ['w','q']: break

        if choice == 'w':
            pass
        else:
            pass

def main():
    print_header()
    
    name = input('\nWhat is your name? ')
    player = Player(name)
    print_intro(player)

    moves = 10
    while moves >= 2:
        handle_move(moves, player)
        moves -= 1

if __name__ == '__main__': main()