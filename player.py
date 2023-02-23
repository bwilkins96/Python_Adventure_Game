# Player class

class Player:
    def __init__(self, name):
        self.name = name
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

    def add_energy(self, amt):
        self.energy += amt

    def add_trinket(self, amt):
        self.pages += amt