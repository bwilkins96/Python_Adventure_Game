# Enemy classes for the Adventure Game project

class Enemy:
    'An enemy parent class designed for the Adventure Game project'

    def __init__(self, name, intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list):
        """
        Produces an instance of the enemy class that stores name, intro,
        outro, messages related to player attacks, an attacking message,
        and a list of taken damages corresponding to types of player attacks

        This initialization is handled within child classes
        """
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
        "Returns enemy's name"
        return self.name
    
    def get_energy(self):
        "Returns enemy's energy"
        return self.energy
    
    def get_attacker_msg(self):
        "Returns enemy's attacking message"
        return self.attacker_msg
    
    def get_damage_list(self):
        "Returns a copy of the enemy's damage list"
        return self.damage_list[:]
    
    def add_energy(self, amt):
        "Adds amount to enemy's energy"
        self.energy += amt

        if self.energy > 100:
            self.add_energy = 100
    
    def reduce_energy(self, amt):
        "Reduces enemy's energy by amount"
        self.energy -= amt

        if self.energy < 0:
            self.energy = 0
    
    def print_intro(self):
        "Prints enemy's intro"
        for line in self.introduction:
            print(line)

    def print_outro(self):
        "Prints enemy's outro"
        for line in self.outro:
            print(line)

    def print_attack_msg(self):
        "Prints enemy's response to player attack"
        for line in self.attack_msg:
            print(line)

    def print_debate_msg(self):
        "Prints enemy's response to player debate"
        for line in self.debate_msg:
            print(line)

    def print_reassurance_msg(self):
        "Prints enemy's response to player reassurance"
        for line in self.reassurance_msg:
            print(line)

    def handle_attack(self):
        "Handles attack from player"
        self.print_attack_msg()
        self.reduce_energy(self.get_damage_list()[0])

    def handle_debate(self):
        "Handles debate from player"
        self.print_debate_msg()
        self.reduce_energy(self.get_damage_list()[1])

    def handle_reassurance(self):
        "Handles reassurance from player"
        self.print_reassurance_msg()
        self.reduce_energy(self.get_damage_list()[2])
    
    def attack_player(self, player):
        "Handles enemy's attack of player"
        print(self.get_attacker_msg())

        if self.get_name() == 'Botzmann Brain':
            player.reduce_energy(20)
        else:
            player.reduce_energy(10)

# Child enemy classes
class Crab(Enemy):
    'A crab enemy child class'

    def __init__(self):
        """
        Produces an instance of a crab enemy
        e.g. Crab()
        """
        intro = ['\nA crab approaches you!']
        outro = ['The tired crab scurries away.']
        a_msg = ['You attack the crab, which appears to considerably reduce its energy.']
        d_msg = ['You attempt to debate with the crab, but it is as determined as ever to attack.']
        r_msg = ['You attempt to reassure the crab, which suprisingly seems to slightly reduce its energy.']
        a_msg_2 = '\nThe crab snaps at you with its claws, reducing your energy by 10.'
        dmg_list = [50, 0, 10]

        super().__init__('Crab', intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list)

class Philosopher(Enemy):
    'A philosopher enemy child class'

    def __init__(self):
        """
        Produces an instance of a philosopher enemy
        e.g. Philosopher()
        """
        intro = [
            '\nA philosopher approaches you, saying "I will convince you to not dig up that',
            'buried treasure! It\'s unnecessary, you see, because I already know what',
            'the meaning of life is!"'
            ]
        outro = [
            'The philosopher is too tired to continue trying to convince you.',
            'They walk away slowly, saying something about Plato\'s allegory of the cave.'
            ]
        a_msg = [
            'You attempt to attack the philosopher, but they effortlessly dodge all your attacks.',
            'The philosopher makes a comment about it being rude to attack people.',
            'However, it does appear that the philosopher has lost some energy.'
            ]
        d_msg = [
            'You debate with the philosopher, pointing out logical fallacies in their arguments.',
            'You even manage to stump the philosopher at times, moderately reducing their energy.'
            ]
        r_msg = [
            'You attempt to reassure the philosopher, telling them that, if they are correct,',
            'then finding the treasure should pose no issue to their argument.',
            'This appears to have no effect on the philosopher.'
        ]
        a_msg_2 = '\nThe philosopher makes nonstop arguments for their position,\nreducing your energy by 10.'
        dmg_list = [10, 50, 0]

        super().__init__('Philosopher', intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list)

class ExistentialCrisis(Enemy):
    'An existential crisis enemy child class'

    def __init__(self):
        """
        Produces an instance of an existential crisis enemy
        e.g. ExistentialCrisis()
        """
        intro = [
            '\nYou are plagued by an existential crisis! What if you discover that',
            'your current beliefs are wrong?'
            ] 
        outro = ['You are relieved of your existential crisis!']
        a_msg = [
            'You go to attack your existential crisis, but realize that it\'s',
            'probably a bad idea to attack something in your own brain.'     
            ]
        d_msg = [
            'You debate with your existential crisis, slightly reducing its power over you.'
        ]
        r_msg = [
            'You reassure yourself that it will be okay regardless of the outcome of finding the treasure.',
            'This considerably reduces the energy of your existential crisis.'
            ]
        a_msg_2 = '\nThe existential crisis keeps pestering you, reducing your energy by 10.'
        dmg_list = [0, 10, 50]

        super().__init__('Existential Crisis', intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list)

class BoltzmannBrain(Enemy):
    'A Boltzman brain enemy child class'

    def __init__(self):
        """
        Produces an instance of a Boltzman brain enemy
        e.g. BoltzmanBrain()
        """
        intro = [
            '\nSuprisingly, a floating Boltzmann brain approaches you!',
            'It says to you, from within your own brain, "Yes, I did spontaneously',
            'pop into existence and I\'m going to stop you!"',
            'You\'re not sure how any of this is even possible.'
            ]
        outro = [
            'The Boltzmann brain vanishes from existence.',
            'You\'re still confused by the whole encounter.'     
            ]
        a_msg = ['You attack the floating brain, causing some reduction in its energy.']
        d_msg = [
            'You debate with the brain, pointing out the high improbability of its existence.',
            'This seems to immediately reduce the brain\'s energy to zero.'
            ]
        r_msg = ['You attempt to reassure the floating brain, but it does not appear to appreciate your efforts.']
        a_msg_2 = '\nThe floating brain hits you with psychic waves emmiting out of it,\nreducing your energy by 20!'
        dmg_list = [20, 100, 0]

        super().__init__('Boltzmann Brain', intro, outro, a_msg, d_msg, r_msg, a_msg_2, dmg_list)