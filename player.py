# Player class for the Adventure Game project

class Player:
    def __init__(self, name):
        self.name = f'Captain {name}'.title()
        self.energy = 100
        self.pages = 0
    
    def get_name(self):
        return self.name
    
    def get_energy(self):
        return self.energy

    def get_trinket_count(self):
        return self.pages
    
    def reduce_energy(self, amt):
        self.energy -= amt

        if self.energy < 0:
            self.energy = 0

    def add_energy(self, amt):
        self.energy += amt

    def add_trinket(self, amt):
        self.pages += amt
    
    def print_status(self):
        print(f'\n{self.get_name()} | Energy: {self.get_energy()}, Pages: {self.get_trinket_count()}\n')
    
    def look_behind(self):
        print('\nYou look behind you and see the crashing waves of the ocean,')
        print(f'as well as the ship you came here on, the Ship of {self.name.title()}!')
        print('If you replaced every piece of your ship over time, would it be the same ship?\n')

    def attack_enemy(self, enemy, choice):
        if choice == 'a':
            enemy.handle_attack()
        elif choice == 'd':
            enemy.handle_debate()
        else:
            enemy.handle_reassurance()