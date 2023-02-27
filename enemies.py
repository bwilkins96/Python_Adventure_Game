# Enemy classes

class Enemy:
    def __init__(self, name, intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list):
        self.name = name
        self.introduction = intro
        self.outro = outro
        self.attack_msg = a_msg
        self.debate_msg = d_msg
        self.reassurance_msg = r_msg
        self.attacker_msg = a_msg_2
        self.damage_list = dmg_list
        self.energy = 100

    def get_name(self):
        return self.name
    
    def get_energy(self):
        return self.energy
    
    def get_attacker_msg(self):
        return self.attacker_msg
    
    def get_damage_list(self):
        return self.damage_list[:]
    
    def add_energy(self, amt):
        self.energy += amt
    
    def reduce_energy(self, amt):
        self.energy -= amt
    
    def print_intro(self):
        for line in self.introduction:
            print(line)

    def print_outro(self):
        for line in self.outro:
            print(line)

    def print_attack_msg(self):
        for line in self.attack_msg:
            print(line)

    def print_debate_msg(self):
        for line in self.debate_msg:
            print(line)

    def print_reassurance_msg(self):
        for line in self.reassurance_msg:
            print(line)

    def handle_attack(self):
        self.print_attack_msg()

    def handle_debate(self):
        self.print_debate_msg()

    def handle_reassurance(self):
        self.print_reassurance_msg()

class Crab(Enemy):
    def __init__(self):
        intro = ['\nA crab approaches you!']
        outro = ['\nThe tired crab scurries away.']
        a_msg = []
        d_msg = []
        r_msg = []
        a_msg_2 = ''
        dmg_list = [50, 0, 10]

        super().__init__('Crab', intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list)

class Philosopher(Enemy):
    def __init__(self):
        intro = [
            '\nA philosopher approaches you, saying "I will convince you to not dig up that',
            'buried treasure! It\'s unnecessary, you see, because I already know what',
            'the meaning of life is!"'
            ]
        outro = ['\nThe philosopher is too tired to continue trying to convince you.',
                 'They walk away slowly, saying something about Plato\'s allegory of the cave.'
            ]
        a_msg = []
        d_msg = []
        r_msg = []
        a_msg_2 = ''
        dmg_list = [10, 50, 0]

        super().__init__('Philosopher', intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list)

class ExistentialCrisis(Enemy):
    def __init__(self):
        intro = [
            '\nYou are plagued by an existential crisis! What if you discover that',
            'you\'re current beliefs are wrong?'
            ] 
        outro = ['\nYou are relieved of your existential crisis!']
        a_msg = []
        d_msg = []
        r_msg = []
        a_msg_2 = ''
        dmg_list = [0, 10, 50]

        super().__init__('Existential Crisis', intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list)

class BoltzmannBrain(Enemy):
    def __init__(self):
        intro = [
            '\nSuprisingly, a floating Boltzmann brain approaches you!',
            'It says to you, from within your own brain, "Yes, I did spontaneously',
            'pop into existence and I\'m going to stop you!',
            '\nYou\'re not sure how any of this is even possible.'
            ]
        outro = ['\nThe Boltzmann brain vanishes from existence.',
                'You\'re still confused by the whole encounter.'     
            ]
        a_msg = []
        d_msg = []
        r_msg = []
        a_msg_2 = ''
        dmg_list = [20, 100, 0]

        super().__init__('Botzmann Brain', intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list)