# Enemy classes

class Enemy:
    def __init__(self, name, intro):
        self.name = name
        self.introduction = intro
        self.energy = 100

    def get_name(self):
        return self.name
    
    def get_intro(self):
        return self.introduction
    
    def get_energy(self):
        return self.energy
    
    def add_energy(self, amt):
        self.energy += amt
    
    def reduce_energy(self, amt):
        self.energy -= amt
    
    def print_intro(self):
        for line in self.get_intro():
            print(line)

class Crab(Enemy):
    def __init__(self):
        intro = ['\nA crab approaches you!']
        super().__init__('Crab', intro)

class Philosopher(Enemy):
    def __init__(self):
        intro = [
            '\nA philosopher approaches you, saying "I will convince you to not dig up that',
            'buried treasure! It\'s unnecessary, you see, because I already know what',
            'the meaning of life is!"'
            ]
        super().__init__('Philosopher', intro)

class ExistentialCrisis(Enemy):
    def __init__(self):
        intro = [
            '\nYou are plagued by an existential crisis! What if you discover that',
            'you\'re current beliefs are wrong?'
            ] 
        super().__init__('Existential Crisis', intro)

class BoltzmannBrain(Enemy):
    def __init__(self):
        intro = [
            '\nSuprisingly, a floating Boltzmann brain approaches you!',
            'It says to you, from within your own brain, "Yes, I did spontaneously',
            'pop into existence and I\'m going to stop you!',
            '\nYou\'re not sure how any of this is even possible.'
            ]
        super().__init__('Botzmann Brain', intro)